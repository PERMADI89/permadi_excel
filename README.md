# ✅ Streamlit Form ke Google Spreadsheet

Form input sederhana dengan Streamlit yang menyimpan data ke Google Sheets.

---

## Cara Setup

1. Upload semua file ini ke GitHub
2. Deploy ke [Streamlit Cloud](https://streamlit.io/cloud)
3. Tambahkan ke `Secrets`:

```
GSHEET_CREDS = """
{ paste seluruh isi JSON credentials kamu di sini }
"""
```

> Spreadsheet kamu harus di-share ke:
```
streamlit-gsheet@streamlit-form-466606.iam.gserviceaccount.com
```

---

## Kolom di Spreadsheet

- Timestamp
- Nama
- Email
- Aktivitas