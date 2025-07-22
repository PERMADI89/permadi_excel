import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Scope akses
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Ambil kredensial dari secrets
service_account_info = dict(st.secrets["google_service_account"])
creds = Credentials.from_service_account_info(service_account_info, scopes=scope)
client = gspread.authorize(creds)

# Spreadsheet ID kamu
SPREADSHEET_ID = "1Ex_gkuZC8r6qNSt-VvB2trJ1efqQGdKHWbW4tFmfbJ4"

# Load & tampilkan data
sheet = client.open_by_key(SPREADSHEET_ID)
worksheet = sheet.sheet1
data = worksheet.get_all_records()
df = pd.DataFrame(data)

st.title("📊 Data dari Google Spreadsheet")
st.dataframe(df)
