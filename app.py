import streamlit as st
st.title('calculate your bmi')
wt = st.number_input('Enter your weight in kgs')
h = st.number_input('Enter your height in Ms')
bmi = wt/h**2
if h == 0:
    bmi = 0
else:
    bmi = wt/h**2
    


st.success(f'your bmi is {bmi} kg/cm^2')