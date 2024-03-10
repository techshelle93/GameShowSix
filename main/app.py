import streamlit as st
import pandas as pd
import time
from PIL import Image
import json
import requests



st.set_page_config(page_title="GameShow6", page_icon=":trophy:", layout="wide")

st.title("Welcome to Game Show Six Contestants")






df = pd.DataFrame(
    [
     {"Dear Mamma": "100", "url": "https://1drv.ms/i/s!AgrwevlpCkT5gson4UCiSO7pwUXqPQ?e=AGnRzM", "is_widget": True, "Who is that Urban legend":  "100", "url1": "https://1drv.ms/i/s!AgrwevlpCkT5gspJgUtRRkLEJKX6DA?e=n8szYG","is_widget0":  True,"What is that Condition": "100", "url2": "https://1drv.ms/i/s!AgrwevlpCkT5gspVWJKzbNCGMKGUHg?e=zHFCAa", "is_widget1":  True, "What's that Profession?": "100","url3": "https://1drv.ms/i/s!AgrwevlpCkT5gspdD6hPN0xzh_LTzQ?e=6BIzmi", "is_widget2": True},
     {"Dear Mamma": "200", "url": "https://1drv.ms/v/s!AgrwevlpCkT5gsoqX3X9k1RQiC69Lw?e=ObVnrh","is_widget":  True, "Who is that Urban legend":  "200", "url1": "https://1drv.ms/i/s!AgrwevlpCkT5gspNRRqeUWF6pdqjoQ?e=8hdDg5","is_widget0":  True, "What is that Condition": "200", "url2": "https://1drv.ms/i/s!AgrwevlpCkT5gspWo4u0iXEdc9Q9Ow?e=swsTNe", "is_widget1": True,"What's that Profession?": "200","url3": "https://1drv.ms/i/s!AgrwevlpCkT5gspe-1vvHsiiDikemQ?e=LuFRPK", "is_widget2": True},
     {"Dear Mamma": "300", "url": "https://1drv.ms/i/s!AgrwevlpCkT5gsotTP6W1I_Z7kBgPg?e=QeQRrB","is_widget": True, "Who is that Urban legend": "300", "url1": "https://1drv.ms/i/s!AgrwevlpCkT5gspOqYxx1YddE_KX2g?e=oo1N26","is_widget0":   True, "What is that Condition": "300", "url2": "https://1drv.ms/i/s!AgrwevlpCkT5gspXrBXvHTKAR_90DA?e=feR75V", "is_widget1":  True, "What's that Profession?": "300", "url3": "https://1drv.ms/i/s!AgrwevlpCkT5gspfqSUN5SHOXbvhEA?e=FJS7GO","is_widget2": True},
     {"Dear Mamma": "400", "url": "https://1drv.ms/i/s!AgrwevlpCkT5gsosgmVxrPUUCtPp0g?e=6ohcfH", "is_widget":  True, "Who is that Urban legend": "400", "url1": "https://1drv.ms/i/s!AgrwevlpCkT5gspPL44rhgkTd-OxTg?e=IBopzP", "is_widget0":  True, "What is that Condition": "400", "url2": "https://1drv.ms/i/s!AgrwevlpCkT5gspY_9pfaa6EaQnq7g?e=uv0OBZ",  "is_widget1":  True, "What's that Profession?": "400","url3": "https://1drv.ms/i/s!AgrwevlpCkT5gspnAsdsKO4hlZcncA?e=PdQtRr", "is_widget2": True},
     {"Dear Mamma": "500", "url":"https://1drv.ms/i/s!AgrwevlpCkT5gsou3VkcdFVh5JlIPg?e=TFnUKd", "is_widget":  True, "Who is that Urban legend": "500", "url1": "https://1drv.ms/i/s!AgrwevlpCkT5gspQcDynF-f4-wCsfg?e=dxwtZn", "is_widget0":  True, "What is that Condition": "500", "url2": "https://1drv.ms/i/s!AgrwevlpCkT5gspZMcPwVI0zIT3zlA?e=yRk98H", "is_widget1": True, "What's that Profession?": "500","url3": "https://1drv.ms/i/s!AgrwevlpCkT5gspgy722T_UTy45E_w?e=IXCxlY", "is_widget2": True},
     {"Dear Mamma": "600",  "url": "https://1drv.ms/i/s!AgrwevlpCkT5gsovjgnTdiTnmEKt_w?e=De7Y38", "is_widget":  True, "Who is that Urban legend": "600", "url1": "https://1drv.ms/i/s!AgrwevlpCkT5gspRxsd562mAwQy0nw?e=asFc1j", "is_widget0": True, "What is that Condition": "600", "url2": "https://1drv.ms/i/s!AgrwevlpCkT5gspaz1Wp2cX_SnL1GQ?e=qdUqW2", "is_widget1": True, "What's that Profession?": "600","url3": "https://1drv.ms/v/s!AgrwevlpCkT5gspjGQJtD59B2WU4pw", "is_widget2":  True},
     {"Dear Mamma": "700", "url": "https://1drv.ms/i/s!AgrwevlpCkT5gsowzlaHVYjQFUAiew?e=9FL1Zr", "is_widget":  True, "Who is that Urban legend": "700", "url1": "https://1drv.ms/i/s!AgrwevlpCkT5gspTLCoMAcu9IRAbMA?e=j5IBqh", "is_widget0":  True, "What is that Condition": "700", "url2": "https://1drv.ms/i/s!AgrwevlpCkT5gspbJvOFrBP5QKLpiA?e=MZOzKM", "is_widget1": True, "What's that Profession?": "700", "url3": "https://1drv.ms/v/s!AgrwevlpCkT5gspmuxaVPpyUSrO_FQ", "is_widget2": True},
     {"Dear Mamma": "800","url":  "https://1drv.ms/v/s!AgrwevlpCkT5gso3PRgkmrqCzwIMAA?e=VTixwj", "is_widget":  True, "Who is that Urban legend": "800", "url1":"https://1drv.ms/i/s!AgrwevlpCkT5gspU7T8skNK_eA2y0g?e=zKncyq","is_widget0":  True, "What is that Condition": "800", "url2": "https://1drv.ms/i/s!AgrwevlpCkT5gspcn3LNnuselOjkRg?e=61viXh", "is_widget1": True, "What's that Profession?": "800", "url3": "https://1drv.ms/v/s!AgrwevlpCkT5gspozyNgbxrDHOuBlw?e=TG84w3", "is_widget2":  True}


    ]
)


edited_df = st.data_editor(
    df,
column_config={
        "url": st.column_config.LinkColumn("Media", display_text="Media"),
        "url1": st.column_config.LinkColumn("Media1", display_text="Media"),
        "url2": st.column_config.LinkColumn("Media2", display_text="Media"),
        "url3": st.column_config.LinkColumn("Media3", display_text="Media"),
        "is_widget": st.column_config.LinkColumn("is_widget"),
        "is_widget0": st.column_config.LinkColumn("is_widget0"),
        "is_widget1": st.column_config.LinkColumn("is_widget1"),
        "is_widget2": st.column_config.LinkColumn("is_widget2"),
        "is_widget": "ChosenA",
        "is_widget0": "ChosenB",
        "is_widget1": "ChosenC",
        "is_widget2": "ChosenD"
},

hide_index=True,
)



