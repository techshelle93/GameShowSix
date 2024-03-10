import streamlit as st

import time

import requests


st.set_page_config(page_title="GameShow6", page_icon=":trophy:", layout="centered")

st.title("Welcome to Game Show Six Contestants")
def update_timer():
    remaining_time = 120  # 2 minutes
    while remaining_time > 0:
        remaining_time -= 1
        if remaining_time == 100:
            st.error("Almost One minute!")
        if remaining_time == 60:
                    st.error("One minute remaining!")
        time.sleep(1)

if st.button("Start Timer"):
    update_timer()



