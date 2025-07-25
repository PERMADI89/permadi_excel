import os
import json
from google.oauth2.service_account import Credentials
import gspread


# Function untuk load dan cek login user
import ast

def load_users():
    users_raw = st.secrets["users"]
    return ast.literal_eval(users_raw)

def login_user(username, password):
    users = load_users()
    return any(u["username"]==username and u["password"]==password for u in users)

# Koneksi ke Google Sheets
@st.cache_resource
def connect_gsheet():
    credentials_dict = json.loads(st.secrets["GOOGLE_CREDENTIALS_JSON"])
    creds = Credentials.from_service_account_info(credentials_dict)
    client = gspread.authorize(creds)
    spreadsheet_id = st.secrets["SPREADSHEET_ID"]
    return client.open_by_key(spreadsheet_id).sheet1

# — Mulai aplikasi —
SPREADSHEET_ID = "1Ex_gkuZC8r6qNSt-VvB2trJ1efqQGdKHWbW4tFmfbJ4"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Streamlit Apps – Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(username, password):
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Username atau password salah.")
else:
    sheet = connect_gsheet()
    st.sidebar.title("Menu")
    menu = st.sidebar.radio("", ["Input Data","Rekap Data","Logout"])

    if menu == "Input Data":
        st.header("📝 Form Input Data")
        nama = st.text_input("Nama")
        email = st.text_input("Email")
        umur = st.number_input("Umur", 1, 120)
        divisi = st.selectbox("Divisi", ["IT","HRD","Finance","Marketing"])
        aktivitas = st.text_area("Aktivitas")

        if st.button("Kirim"):
            if nama and email:
                sheet.append_row([nama, email, umur, divisi, aktivitas])
                st.success("✅ Data berhasil dikirim ke Google Sheets!")
            else:
                st.warning("Nama dan email wajib diisi!")

    elif menu == "Rekap Data":
        st.header("📋 Rekap Data")
        data = sheet.get_all_values()
        if len(data) > 1:
            st.dataframe(data[1:], columns=data[0], use_container_width=True)
        else:
            st.info("Belum ada data.")

    elif menu == "Logout":
        st.session_state.logged_in = False
        st.rerun()
