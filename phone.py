import streamlit as st
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("Your twilio account SID")
auth_token = os.getenv("Twilio auth tocken")

from_number = os.getenv("Twilio phone number")

st.set_page_config(page_title="Voice Caller", page_icon="📱")
st.title("Twilio Voice Call Sender")

st.markdown("Send a **voice call** with your custom message using Twilio.")

reciver = st.text_input("Recipient Number (with country code)", "+91")
message_text = st.text_area("Message to Speak", "Hello! This is a test voice call from Streamlit app.")

if st.button(" Make Call"):
    if not all([account_sid, auth_token, from_number, reciver]):
        st.error("Missing Twilio credentials or phone number.")
    elif not message_text.strip():
        st.warning("Please enter a message to speak.")
    else:
        try:
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                twiml=f'<Response><Say voice="alice">{message_text}</Say></Response>',
                to=reciver,
                from_=from_number
            )

            st.success(f" Call initiated! SID: {call.sid}")

            latest_call = client.calls(call.sid).fetch()
            st.subheader(" Call Details")
            st.text(f"Status      : {latest_call.status}")
            st.text(f"Start Time  : {latest_call.start_time}")
            st.text(f"End Time    : {latest_call.end_time}")
            st.text(f"To          : {latest_call.to}")
            st.text(f"From        : {latest_call._from}")
            st.text(f"Duration    : {latest_call.duration} seconds")

            if hasattr(latest_call, "error_code") and latest_call.error_code:
                st.error(f" Error Code: {latest_call.error_code}")
            else:
                st.success(" No error code  call successful or in progress.")

        except Exception as e:
            st.error(f" Failed to make the call: {str(e)}")