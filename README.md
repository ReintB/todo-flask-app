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

## Upload ke GitHub

GitHub digunakan sebagai tempat menyimpan source code. GitHub Pages tidak dapat menjalankan Flask karena hanya mendukung website statis.

```powershell
git add .
git commit -m "Update deployment guide"
git push origin main
```

## Publish dengan PythonAnywhere

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

PythonAnywhere menyediakan filesystem persisten untuk aplikasi kecil seperti ini, sehingga database SQLite tetap tersimpan. URL publik akan berbentuk `https://USERNAME.pythonanywhere.com`.
