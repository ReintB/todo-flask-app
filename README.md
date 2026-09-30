# To-Do List Flask App

Aplikasi To-Do List sederhana dengan Flask dan SQLite.

## Menjalankan lokal

```powershell
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py app.py
```

Buka `http://127.0.0.1:5000`.

## Deploy ke Render

Proyek ini sudah menyediakan `render.yaml`. Setelah repository di-upload ke GitHub:

1. Masuk ke [Render](https://render.com) dan login dengan GitHub.
2. Pilih **New > Blueprint**.
3. Pilih repository ini.
4. Konfirmasi konfigurasi dari `render.yaml` dan deploy.
5. Render akan memberikan URL publik.

Database SQLite berada di `instance/todo.db`. Pada paket Render gratis, filesystem bersifat sementara sehingga data dapat hilang ketika service di-redeploy atau restart. Untuk data yang persisten, gunakan PythonAnywhere atau pindahkan database ke PostgreSQL.

## Deploy ke PythonAnywhere

Pada Bash Console PythonAnywhere:

```bash
git clone https://github.com/USERNAME/NAMA-REPOSITORY.git
cd NAMA-REPOSITORY
pip install --user -r requirements.txt
```

Buat Web App Flask baru. Pada file WSGI PythonAnywhere, gunakan:

```python
import sys
sys.path.insert(0, "/home/USERNAME/NAMA-REPOSITORY")
from app import app as application
```

Simpan, lalu klik **Reload**.
