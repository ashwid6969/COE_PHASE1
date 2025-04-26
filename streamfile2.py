import streamlit as st
st.title("This is sample program")
num1=st.number_input("Enter num1",min_value=0,step=1)
num2=st.number_input("Enter num2")
if st.button("submit"):
    st.write("Total: ",num1+num2)
dob=st.date_input("select DOB")

'''st.success("")
st.error("")'''
