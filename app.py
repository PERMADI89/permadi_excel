import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Konfigurasi
SPREADSHEET_ID = "PASTE_SPREADSHEET_ID_KAMU"

# Scope dan auth
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("service_account.json", scopes=scope)
client = gspread.authorize(creds)

# Load data dari spreadsheet
sheet = client.open_by_key(SPREADSHEET_ID)
worksheet = sheet.sheet1
data = worksheet.get_all_records()
df = pd.DataFrame(data)

# Tampilkan di Streamlit
st.title("Data dari Google Spreadsheet")
st.dataframe(df)
