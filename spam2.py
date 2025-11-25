import streamlit as st
import pandas as pd

import joblib
model=joblib.load("spam_clf.pkl")

st.set_page_config(layout="wide")


st.sidebar.image("flag.jpg")
st.sidebar.title("ℹ️About us")
st.sidebar.text("Pannkaj A Singh")
st.sidebar.title("📞Contact us")
st.sidebar.text("88010431227")


# Custom CSS
st.markdown("""
    <style>

    /* Main Title */
    .full-width-title {
        width: 100%;
        display: block;
        text-align: center;
        font-size: 48px;
        font-weight: 900;
        color: #ffffff;               /* Title Font Color */
        background: #ff5733;          /* Title Background */
        padding: 20px 0;
        border-radius: 10px;
        margin-bottom: 25px;
    }

    /* Sub-Heading Style (Single Msg, Bulk Msg) */
    .sub-heading {
        font-size: 30px;
        font-weight: 800;
        color: #4a90e2;               /* Heading Font Color */
        background: #e8f1ff;          /* Heading Background Color */
        padding: 10px 15px;
        border-radius: 8px;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    </style>
""", unsafe_allow_html=True)


# MAIN TITLE
st.markdown('<div class="full-width-title">Spam Classifier Project</div>', unsafe_allow_html=True)

# SUB HEADINGS  




col1,col2=st.columns([1.5,2],gap="medium")
with col1:
    st.markdown('<div class="sub-heading"><center>Single Message Prediction</center></div>', unsafe_allow_html=True)
    st.text_area("Enter your single message here")

    if st.button("Predict"):
        result=model.predict([text])
        if result=="spam":
            st.error("Spam")
        else:
            st.success("yes")
with col2:
    st.markdown('<div class="sub-heading"><center>Bulk Message Prediction</center></div>', unsafe_allow_html=True)
    file=st.file_uploader("select file containg bulk msg", type=["txt","csv"])
    if file!=None:
        df=pd.read_csv(file.name,header=None,names=["msg"])
        place=st.empty()
        place.dataframe(df)
        if st.button("Predict",key="b2"):
            df["result"]=model.predict(df.msg)
            place.data_editor(df)
            
    