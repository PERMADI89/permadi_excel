import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import json

st.set_page_config(page_title="Permadi Excel", layout="wide")

# Ambil kredensial dari secrets
service_account_info = json.loads(st.secrets["google_service_account"])
creds = Credentials.from_service_account_info(service_account_info)

# Buka Spreadsheet
gc = gspread.authorize(creds)
sheet = gc.open_by_key("1Ex_gkuZC8r6qNSt-VvB2trJ1efqQGdKHWbW4tFmfbJ4")
worksheet = sheet.get_worksheet(0)

# Ambil dan tampilkan data
data = worksheet.get_all_records()
df = pd.DataFrame(data)

st.title("📊 Data dari Google Spreadsheet")
st.dataframe(df, use_container_width=True)
