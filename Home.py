import streamlit as st
import pandas as pd

st.set_page_config("wide")

col1,col2= st.columns([3,4])

with col1:
    st.image("images/Photo.png", width=300)
with col2:
    st.title("Adeiye Oluwasegun")
    content = """
    I am a graduate of University of Lagos(B.sc Geophysics) and currently undertaking my masters in Data Science Management
     at the Rome business School (Nigeria). I am a python programmer with key interest in the use of the application 
     in data analysis and modelling.
     Do drop a comment of your thoughts after your review
    """
    st.info(content)

content2 = """"Do view some of my projects done with python below.Thanks"""

st.write(content2)

col3,col4 = st.columns([3,3])

df = pd.read_csv("data.csv"
                     , sep=";")
with col3:
    for index,row in df[0:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Project link]({row['url']})")

with col4:
    for index,row in df[11:21].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[Project link]({row['url']})")


