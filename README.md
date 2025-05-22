# Simple FastAPI Chat Platform

Platform chat sederhana berbasis FastAPI dengan WebSocket.  
Memungkinkan chat antar pengguna berdasarkan nomor ID (contoh: 107, 108).  

---

## Fitur

- Login menggunakan nomor ID
- Chat realtime dengan WebSocket
- Sistem kontak berdasarkan nomor ID pengguna
- UI sederhana dan mudah dipahami
- Bisa dijalankan di VPS dengan subdomain tersendiri

---

## Persyaratan

- Python 3.8+
- VPS Ubuntu/Debian
- NGINX (untuk reverse proxy)
- Certbot (opsional, untuk SSL)

---

## Instalasi

1. Clone repository ini:

   ```bash
   git clone https://github.com/username/repo-chat-app.git
   cd repo-chat-app
