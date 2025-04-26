import streamlit as st
st.title("Hotel Tanvik")
st.title("Tip Generator")
bill=st.number_input("Enter bill amount")
if bill<1000:
    tip=(bill*2)/100
elif bill<=5000:
    tip=(bill*5)/100
else:
    tip=(bill*7)/100
if st.button("submit"):
    st.write("The Tip is :",tip)
    
