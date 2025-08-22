const express = require('express');
const os = require('os');
const path = require('path');
const app = express();
const PORT = 3000;

// Función para obtener IP local
function getLocalIP() {
  const interfaces = os.networkInterfaces();
  for (const name in interfaces) {
    for (const net of interfaces[name]) {
      if (net.family === 'IPv4' && !net.internal) {
        return net.address;
      }
    }
  }
  return 'localhost';
}

// 👉 Servir archivos estáticos de la carpeta "public"
app.use(express.static(path.join(__dirname, 'public')));

// Ruta principal → sirve el index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Iniciar servidor en todas las interfaces
app.listen(PORT, '0.0.0.0', () => {
  const ip = getLocalIP();
  console.log(`Servidor corriendo en:
   - http://localhost:${PORT}
   - http://${ip}:${PORT}`);
});
