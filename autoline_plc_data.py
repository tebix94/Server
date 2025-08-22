import os
import threading
import time
from python_modules.kv_plc import *

# PLC names list
plc_names = ('Loading cable',
             'Gasket assembly A',
             'UV & Trim A',
             'IMLA assembly A',
             'IMLA welding A',
             'Shield welding A',
             'Gasket assembly B',
             'UV & Trim B',
             'IMLA assembly B',
             'IMLA welding B',
             'Shield welding B',
             'Hipot and marking',
             'Unloading'
             )

# Instance line 1 PLC's

plc_l1 = []

plc_l1.append(kv_plc_tcp_socket('192.168.0.10', 8501, 3)) 
plc_l1.append(kv_plc_tcp_socket('192.168.0.20', 8501, 3))
plc_l1.append(kv_plc_tcp_socket('192.168.0.30', 8501, 3))
plc_l1.append(kv_plc_tcp_socket('192.168.0.40', 8501, 3))
plc_l1.append(kv_plc_tcp_socket('192.168.0.50', 8501, 3))
plc_l1.append(kv_plc_tcp_socket('192.168.0.60', 8501, 3))
plc_l1.append(kv_plc_tcp_socket('192.168.0.120', 8501, 3))
plc_l1.append(kv_plc_tcp_socket('192.168.0.130', 8501, 3))
plc_l1.append(kv_plc_tcp_socket('192.168.0.140', 8501, 3))
plc_l1.append(kv_plc_tcp_socket('192.168.0.150', 8501, 3))
plc_l1.append(kv_plc_tcp_socket('192.168.0.160', 8501, 3))
plc_l1.append(kv_plc_tcp_socket('192.168.0.170', 8501, 3))
plc_l1.append(kv_plc_tcp_socket('192.168.0.190', 8501, 3))

# Instance line 2 PLC's

plc_l2 = []

plc_l2.append(kv_plc_tcp_socket('192.168.0.12', 8501, 3)) 
plc_l2.append(kv_plc_tcp_socket('192.168.0.22', 8501, 3))
plc_l2.append(kv_plc_tcp_socket('192.168.0.32', 8501, 3))
plc_l2.append(kv_plc_tcp_socket('192.168.0.42', 8501, 3))
plc_l2.append(kv_plc_tcp_socket('192.168.0.52', 8501, 3))
plc_l2.append(kv_plc_tcp_socket('192.168.0.62', 8501, 3))
plc_l2.append(kv_plc_tcp_socket('192.168.0.122', 8501, 3))
plc_l2.append(kv_plc_tcp_socket('192.168.0.132', 8501, 3))
plc_l2.append(kv_plc_tcp_socket('192.168.0.142', 8501, 3))
plc_l2.append(kv_plc_tcp_socket('192.168.0.152', 8501, 3))
plc_l2.append(kv_plc_tcp_socket('192.168.0.162', 8501, 3))
plc_l2.append(kv_plc_tcp_socket('192.168.0.172', 8501, 3))
plc_l2.append(kv_plc_tcp_socket('192.168.0.192', 8501, 3))

# Instance line 3 PLC's

plc_l3 = []

plc_l3.append(kv_plc_tcp_socket('192.168.0.14', 8501, 3)) 
plc_l3.append(kv_plc_tcp_socket('192.168.0.24', 8501, 3))
plc_l3.append(kv_plc_tcp_socket('192.168.0.34', 8501, 3))
plc_l3.append(kv_plc_tcp_socket('192.168.0.44', 8501, 3))
plc_l3.append(kv_plc_tcp_socket('192.168.0.54', 8501, 3))
plc_l3.append(kv_plc_tcp_socket('192.168.0.64', 8501, 3))
plc_l3.append(kv_plc_tcp_socket('192.168.0.124', 8501, 3))
plc_l3.append(kv_plc_tcp_socket('192.168.0.134', 8501, 3))
plc_l3.append(kv_plc_tcp_socket('192.168.0.144', 8501, 3))
plc_l3.append(kv_plc_tcp_socket('192.168.0.154', 8501, 3))
plc_l3.append(kv_plc_tcp_socket('192.168.0.164', 8501, 3))
plc_l3.append(kv_plc_tcp_socket('192.168.0.174', 8501, 3))
plc_l3.append(kv_plc_tcp_socket('192.168.0.194', 8501, 3))

# Instance line 4 PLC's

plc_l4 = []

plc_l4.append(kv_plc_tcp_socket('192.168.0.16', 8501, 3)) 
plc_l4.append(kv_plc_tcp_socket('192.168.0.26', 8501, 3))
plc_l4.append(kv_plc_tcp_socket('192.168.0.36', 8501, 3))
plc_l4.append(kv_plc_tcp_socket('192.168.0.46', 8501, 3))
plc_l4.append(kv_plc_tcp_socket('192.168.0.56', 8501, 3))
plc_l4.append(kv_plc_tcp_socket('192.168.0.66', 8501, 3))
plc_l4.append(kv_plc_tcp_socket('192.168.0.126', 8501, 3))
plc_l4.append(kv_plc_tcp_socket('192.168.0.136', 8501, 3))
plc_l4.append(kv_plc_tcp_socket('192.168.0.146', 8501, 3))
plc_l4.append(kv_plc_tcp_socket('192.168.0.156', 8501, 3))
plc_l4.append(kv_plc_tcp_socket('192.168.0.166', 8501, 3))
plc_l4.append(kv_plc_tcp_socket('192.168.0.176', 8501, 3))
plc_l4.append(kv_plc_tcp_socket('192.168.0.196', 8501, 3))

# Instance line 5 PLC's

plc_l5 = []

plc_l5.append(kv_plc_tcp_socket('192.168.0.18', 8501, 3)) 
plc_l5.append(kv_plc_tcp_socket('192.168.0.28', 8501, 3))
plc_l5.append(kv_plc_tcp_socket('192.168.0.38', 8501, 3))
plc_l5.append(kv_plc_tcp_socket('192.168.0.48', 8501, 3))
plc_l5.append(kv_plc_tcp_socket('192.168.0.58', 8501, 3))
plc_l5.append(kv_plc_tcp_socket('192.168.0.68', 8501, 3))
plc_l5.append(kv_plc_tcp_socket('192.168.0.128', 8501, 3))
plc_l5.append(kv_plc_tcp_socket('192.168.0.138', 8501, 3))
plc_l5.append(kv_plc_tcp_socket('192.168.0.148', 8501, 3))
plc_l5.append(kv_plc_tcp_socket('192.168.0.158', 8501, 3))
plc_l5.append(kv_plc_tcp_socket('192.168.0.168', 8501, 3))
plc_l5.append(kv_plc_tcp_socket('192.168.0.178', 8501, 3))
plc_l5.append(kv_plc_tcp_socket('192.168.0.198', 8501, 3))

# Instance line 6 PLC's

plc_l6 = []

plc_l6.append(kv_plc_tcp_socket('192.168.0.70', 8501, 3)) 
plc_l6.append(kv_plc_tcp_socket('192.168.0.71', 8501, 3))
plc_l6.append(kv_plc_tcp_socket('192.168.0.72', 8501, 3))
plc_l6.append(kv_plc_tcp_socket('192.168.0.73', 8501, 3))
plc_l6.append(kv_plc_tcp_socket('192.168.0.74', 8501, 3))
plc_l6.append(kv_plc_tcp_socket('192.168.0.75', 8501, 3))
plc_l6.append(kv_plc_tcp_socket('192.168.0.76', 8501, 3))
plc_l6.append(kv_plc_tcp_socket('192.168.0.77', 8501, 3))
plc_l6.append(kv_plc_tcp_socket('192.168.0.78', 8501, 3))
plc_l6.append(kv_plc_tcp_socket('192.168.0.79', 8501, 3))
plc_l6.append(kv_plc_tcp_socket('192.168.0.80', 8501, 3))
plc_l6.append(kv_plc_tcp_socket('192.168.0.81', 8501, 3))
plc_l6.append(kv_plc_tcp_socket('192.168.0.82', 8501, 3))

# Initialize CT lists
ct_l1 = [0] * len(plc_l1)
ct_l2 = [0] * len(plc_l2)
ct_l4 = [0] * len(plc_l4)
ct_l5 = [0] * len(plc_l5)
ct_l6 = [0] * len(plc_l6)

# Initialize lights dictionaries
lights_l1 = [{'green': 0, 'red': 0, 'yellow': 0} for _ in range(len(plc_l1))]
lights_l2 = [{'green': 0, 'red': 0, 'yellow': 0} for _ in range(len(plc_l2))]
lights_l4 = [{'green': 0, 'red': 0, 'yellow': 0} for _ in range(len(plc_l4))]
lights_l5 = [{'green': 0, 'red': 0, 'yellow': 0} for _ in range(len(plc_l5))]
lights_l6 = [{'green': 0, 'red': 0, 'yellow': 0} for _ in range(len(plc_l6))]

# Update functions
def update_ct_single(plc_line, ct_line):
    try:
        for plc, ct in zip(plc_line, ct_line):
            ct = float(plc.read('DM', 88)) / 10.
    except Exception as e:
        print(f'update_ct_single() error: {e}')

def update_status_lights(plc, lights):
    try:
        [lights['green'], lights['red'], lights['yellow']]= plc.multi_read('R', 40005, 3)
    except Exception as e:
        print(f'update_status_lights() error: {e}')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    # Fetch cycle time values
    for plc_line_list, ct_line_list in zip([plc_l1,
                                            plc_l2,
                                            plc_l4,
                                            plc_l5,
                                            plc_l6],
                                            [ct_l1,
                                             ct_l2,
                                             ct_l4,
                                             ct_l5,
                                             ct_l6,]):
        threads = []
        for plc_line, ct_line in zip(plc_line_list, ct_line_list):
            t = threading.Thread(target=update_ct_single, args=(plc_line, ct_line))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

    for name, ct in zip(plc_names, ct_l4):
        print(f'{name}: {ct} seconds')

    # Fetch status lights values
    for plc_list, lights_list in [
        (plc_l1, lights_l1),
        (plc_l2, lights_l2),
        (plc_l4, lights_l4),
        (plc_l5, lights_l5),
        (plc_l6, lights_l6)
    ]:
        threads = []  # Create a new list for each batch
        for plc, lights in zip(plc_list, lights_list):
            t = threading.Thread(target=update_status_lights, args=(plc, lights))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

    print(lights_l6[11]['yellow'])

    time.sleep(0.25)