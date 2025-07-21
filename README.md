# Streamlit Input Form ke Google Spreadsheet

Web sederhana berbasis Streamlit untuk menginput data ke Google Spreadsheet.

## ✅ Fitur

- Input Nama, Email, dan Aktivitas
- Tersimpan otomatis ke tab **Data** dalam Spreadsheet

## 🛠 Cara Deploy

1. Buat file `creds.json` dari Google Cloud Service Account
2. Ambil Spreadsheet ID dari URL: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit`
3. Share spreadsheet ke email service account sebagai **Editor**
4. Di Streamlit Cloud, tambahkan `GSHEET_CREDS` di **Secrets** seperti ini:

```
GSHEET_CREDS = '''
{ JSON DARI FILE creds.json }
'''
```

5. Jalankan aplikasi di Streamlit Cloud