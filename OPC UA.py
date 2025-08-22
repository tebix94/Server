import socket
import tkinter as tk

# === CONFIGURACIONES PLC (mismas que tu ejemplo) ==================================================================================
PLC_IP = '192.168.0.18'
PLC_PORT = 8501
POLL_MS = 250             # intervalo de sondeo (ms)

# Dispositivos a leer (ajusta libremente)
DEVICES = ["R30004","R40005", "R40006", "R40007"]

# === FUNCIONES PLC ===============================================================================================================
def plc_read(addr: str) -> str:
    """
    Lee usando el formato EXACTO que indicaste: 'RD <addr>\\r'
    Abre y cierra la conexión en cada lectura (estilo "request/response").
    """
    cmd = f"RD {addr}\r"
    with socket.create_connection((PLC_IP, PLC_PORT), timeout=3) as s:
        s.sendall(cmd.encode("ascii"))
        return s.recv(64).decode("ascii", errors="ignore").strip()

def plc_write(addr: str, value: int | str):
    """
    Mantengo tu firma y estilo por si luego quieres escribir.
    """
    cmd = f"WR {addr} {value}\r"
    with socket.create_connection((PLC_IP, PLC_PORT), timeout=3) as s:
        s.sendall(cmd.encode("ascii"))

def parse_bit_response(resp: str) -> int | None:
    """
    Extrae 0/1 de respuestas típicas:
    'OK 0', 'OK 1', '0', '1', 'OK0', 'OK1' (con o sin CR/LF).
    """
    if not resp:
        return None
    t = resp.strip().upper()
    parts = t.split()
    # Busca un '0' o '1' como último token confiable
    for token in reversed(parts):
        if token in ("0", "1"):
            return int(token)
    # Por si viene pegado sin espacio: 'OK0'/'OK1'
    if t.endswith("0"):
        return 0
    if t.endswith("1"):
        return 1
    return None

def read_bit(addr: str) -> int | None:
    try:
        resp = plc_read(addr)
        return parse_bit_response(resp)
    except Exception:
        return None

# === UI TKINTER ==================================================================================================================
root = tk.Tk()
root.title("Monitor de Bits (RD simple)")

main = tk.Frame(root, padx=14, pady=14)
main.pack(fill="both", expand=True)

status_lbl = tk.Label(main, text="Estado: listo", font=("Arial", 10))
status_lbl.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

hdr1 = tk.Label(main, text="Dispositivo", font=("Arial", 11, "bold"))
hdr2 = tk.Label(main, text="Valor", font=("Arial", 11, "bold"))
hdr1.grid(row=1, column=0, sticky="w", padx=(0, 10))
hdr2.grid(row=1, column=1, sticky="w")

device_labels = {}  # addr -> Label de valor

for i, dev in enumerate(DEVICES, start=2):
    tk.Label(main, text=dev, font=("Arial", 11)).grid(row=i, column=0, sticky="w", padx=(0, 10), pady=2)
    val_lbl = tk.Label(
        main, text="?", font=("Arial", 14, "bold"),
        width=10, pady=4, relief="groove", bd=2, bg="gray85"
    )
    val_lbl.grid(row=i, column=1, sticky="w", pady=2)
    device_labels[dev] = val_lbl

def update_label(dev: str, value: int | None):
    lbl = device_labels[dev]
    if value is None:
        lbl.config(text="?", bg="gray85", fg="black")
    elif value == 1:
        lbl.config(text="1 (ON)", bg="green", fg="white")
    else:
        lbl.config(text="0 (OFF)", bg="red", fg="white")

def poll():
    """
    Lee cada bit con 'RD <addr>\\r' (una conexión por lectura, igual que tu estilo).
    Si alguna lectura falla, el valor queda '?' para ese dispositivo.
    """
    any_error = False
    for dev in DEVICES:
        val = read_bit(dev)
        if val is None:
            any_error = True
        update_label(dev, val)

    if any_error:
        status_lbl.config(text="Estado: alguna lectura falló (reintentando...)", fg="red")
    else:
        status_lbl.config(text="Estado: OK", fg="green")

    root.after(POLL_MS, poll)

root.after(POLL_MS, poll)
root.mainloop()
