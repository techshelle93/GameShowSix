import streamlit as st

import time

import requests
from streamlit_lottie import st_lottie

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


st.write("---")
url = requests.get(
        "https://lottie.host/c2601f72-f4f5-4054-b767-b87a466cd3c4/X7kLbX11HR.json")
url_json = dict()
if url.status_code == 200:
        url_json = url.json()
else:
         print("Error in the URL")

st_lottie(url_json, height=150, width=160, key='fighting')
