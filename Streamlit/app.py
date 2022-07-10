import streamlit as st 
import pandas as pd 

data = {
    "Series_1":[1,3,4,5,7],
    "Series_2":[10,60,80,90,100]
}

df = pd.DataFrame(data)

st.title("First Streamlit")
st.subheader("Streamlit is elite")
st.write(""" 
Awesome app!
""")
st.write(df)