# Streamlit Form to Google Sheets

A simple Streamlit web app to input data and save it to Google Sheets.

## Setup

1. Create a Google Service Account and enable Google Sheets & Drive API.
2. Share your target spreadsheet with the service account email.
3. Add your JSON credentials to Streamlit Cloud Secrets.
4. Replace `SPREADSHEET_ID` in `app.py` with your actual spreadsheet ID.

## Deploy

Use [Streamlit Cloud](https://streamlit.io/cloud) and link to your GitHub repository.