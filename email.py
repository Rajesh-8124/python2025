import smtplib
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="E:\Important\Personal\one.env")

From = os.getenv("Email_sender")
# here Email sender is the email address of sender which is stored in the one.env file.
password = os.getenv("Email_app_password")

st.title("📨 Email sender app")

Sub = st.text_input("Enter subject:")
To = st.text_input("Enter receiver's email:")
msg =  st.text_input("Enter message:")

text = f"Subject: {Sub}\n\n{msg}"

if st.button("Send Email"):
    try:
        with smtplib.SMTP("smtp.gmail.com",587) as server:
            server.starttls()
            server.login(From,password="your app password")
            server.sendmail(from_addr=From,to_addrs=To, msg=text)
        st.success("✅ Email sent successfully!")
    except Exception as e:
        st.error(f"❌ Failed to send email: {e}")