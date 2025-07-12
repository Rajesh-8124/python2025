import pywhatkit
import streamlit as st

number = st.text_input("Enter recevier's phone number (with countary code) ")
massage = st.text_input("Enter massage ")
t1 = st.selectbox("select hour", [i for i in range(24)])
t2 = st.selectbox("select minute ", [j for j in range(60)])

if st.button("send massage"):
    if number and massage:
        try:
            pywhatkit.sendwhatmsg(number, massage, t1, t2,20,True, 15)
            st.success("message sent successfully")
        except Exception as e:
            st.error(f"Failed tosent massage: {e}")

    else:
        (st.error("Please enter both phone number and message."))

