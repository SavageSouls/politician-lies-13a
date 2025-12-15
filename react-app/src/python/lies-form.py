import streamlit as st

st.set_page_config(page_title="Lies page", layout="wide")
st.title("Lies from")

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

    submit = st.form_submit_button()
    if submit:
        st.success("Ok")
    else:
        st.error("Please fill out the form fields.")