import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import json

def connect_to_gsheet():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    creds_dict = json.loads(st.secrets["GSHEET_CREDS"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key("arsa madina")
    worksheet = sheet.worksheet("Data")
    return worksheet

st.title("Form Input ke Google Spreadsheet")

with st.form("input_form"):
    nama = st.text_input("Nama")
    email = st.text_input("Email")
    aktivitas = st.text_area("Aktivitas")
    submit = st.form_submit_button("Kirim")

if submit:
    ws = connect_to_gsheet()
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ws.append_row([waktu, nama, email, aktivitas])
    st.success("Data berhasil dikirim ke Google Spreadsheet!")
