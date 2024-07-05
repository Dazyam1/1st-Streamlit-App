import streamlit as st
import time as t
st.image("stream1.png")


#Title
st.title("Welcome to Streamlt")

#Header
st.header("Machine Learrning")

#sub Header
st.subheader("Linear Regression")

#Information
st.info("This is the Information ")

#warning Message
st.warning("Wrong Password")

#Success
st.success("You have a Grade")

#write
st.write("Employee Name")
st.write("range(50)")
#Markdown
st.markdown("# Markdown")
st.markdown(":moon:")

#text
st.text("My name is KT")

#Caption
st.caption("Caption is here")

#To display a mathmatical eqation
st.latex(r''' a+b x^2+c''')

#Widget

#checkbox
st.button("Click")

#Radio widget
st.radio("Pick your gender",["Male", "Female", "Others"])

#select box
st.selectbox("Pick your course",["ML", "Cloud", "Cyber Security"]) 

#Multiselect
st.multiselect("Choose the dept",["Content", "Sales", "Marketing", "UI/UX", "Web Design"])

#select_slider
st.select_slider("Rating", ["Bad", "Good", "Excellent", "Outstanding", "Great"])

#slider
st.slider("Pick a Number",0,100)

#Number input
st.number_input("Enter a Number",0,100)

#text input
st.text_input("Enter Your email Address here")

#date input
st.date_input("Opening ceremony")

#Time input
st.time_input("Hey Whats the timing")

# Text area
st.text_area("Welcome to My streamlit website")

# file uploader
st.file_uploader("Upload your file / folder")

st.color_picker("color")

st.progress(90)

#spinner
with st.spinner("just wait"):
    t.sleep(1)

#balloons
st.balloons(  )

#sidebar
st.sidebar.title("Important Information")
st.sidebar.text_input("Mail Address")
st.sidebar.text_input("Password")
st.sidebar.button("Submit")
st.sidebar.radio("professional Expert",["Student","Working","Others"])

# data Visualisation
import pandas as pd
import numpy as np
st.title("bar chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("Line Chart")
st.line_chart(data)
st.title("Area Chart")
st.area_chart(data)