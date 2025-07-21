# Streamlit Form ke Google Spreadsheet

Formulir berbasis Streamlit untuk input data ke Google Spreadsheet.

---

## 🚀 Cara Deploy ke Streamlit Cloud

1. Upload semua file ke GitHub (kecuali creds.json)
2. Ganti `ISI_SPREADSHEET_ID_DI_SINI` di `app.py` dengan Spreadsheet ID kamu
3. Share spreadsheet kamu ke email di `client_email` (dari creds.json) sebagai **Editor**
4. Masuk ke https://streamlit.io/cloud → Settings → Secrets → tambahkan:

```
GSHEET_CREDS = '''
(Paste seluruh isi file creds.json kamu di sini)
'''
```

> ⚠️ Jangan ubah isi `private_key`, Streamlit akan mengurus `\n` otomatis

---

## 📝 Kolom Spreadsheet:
- Timestamp
- Nama
- Email
- Aktivitas

---