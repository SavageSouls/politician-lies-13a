import streamlit as st
import requests

st.set_page_config(page_title="Lies page", layout="wide")
st.title("Lies from")

def eventHandler(event):
    print(event)
    # TODO - implement event handler

with st.form(key="my-form"):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Politician")
        politician_name = st.text_input("Name", placeholder="Johnny Laser")
        age = st.number_input("Age", min_value=18, step=1)
    with col2:
        st.subheader("Party")
        party_name = st.selectbox("Name", ["F*desz", "T*sza", "D*Ká", "MKFKP" ,"MHP"])
        color = st.color_picker("Color")
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Lie")
        lie_date = st.date_input("Date", "today")
        lie = st.text_area("Lie")
    with col4:
        st.subheader("Review")
        consent = st.checkbox("Yes, I really want to store these data!")

    submit = st.form_submit_button(on_click=eventHandler)
    if submit:
        if consent and len(politician_name)>=1:
            form_data_dict = {"politician_name":politician_name, "age":age, "color":color, "lie_date":lie_date, "lie":lie}
            print(f"form_data_dict: {form_data_dict}")
            
            res = requests.post(url="https://")
            print(res)
            print(f"res.status_code: {res.status_code}")
            print(f"res.ok: {res.text}")
            
            st.success("Ok")
        else:
            st.error("Please fill out the form fields.")
    else:
        st.error("Please fill out the form fields.")