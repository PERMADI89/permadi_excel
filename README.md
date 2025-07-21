# Streamlit Form ke Google Spreadsheet

Web Streamlit untuk menginput data ke Google Spreadsheet secara langsung.

---

## 📌 Cara Setup

1. Ganti file `app.py` dengan Spreadsheet ID kamu.
2. Share spreadsheet ke email berikut sebagai Editor:
   ```
   streamlit-gsheet@streamlit-form-466606.iam.gserviceaccount.com
   ```
3. Di [Streamlit Cloud](https://streamlit.io/cloud):
   - Masuk Settings → Secrets
   - Tambahkan Secret `GSHEET_CREDS` dari file `GSHEET_CREDS_streamlit.txt`

---

## Kolom Spreadsheet:
- Timestamp
- Nama
- Email
- Aktivitas