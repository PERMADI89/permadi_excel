import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Koneksi ke Google Sheet
def connect_to_gsheet():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key("SPREADSHEET_ID")  # ganti dengan ID asli
    worksheet = sheet.worksheet("Data")
    return worksheet

# Form Input
st.title("Formulir Input Data")

with st.form("data_form"):
    nama = st.text_input("Nama")
    email = st.text_input("Email")
    aktivitas = st.text_area("Aktivitas")
    submitted = st.form_submit_button("Kirim")

if submitted:
    worksheet = connect_to_gsheet()
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    worksheet.append_row([tanggal, nama, email, aktivitas])
    st.success("Data berhasil dikirim!")
