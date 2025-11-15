import numpy as np
import pandas as pd
import streamlit as st
import joblib
#lets load all the instances required over here
with open ('transformer.joblib','rb') as file:
    transformer = joblib.load(file)

#lets load the model

with open ('final_model.joblib','rb') as file:
    model = joblib.load(file)


st.title('INN Hotel Group')
st.header(':blue[This application will predict the chances of booking cancellation]')



#Lest take input from the user

amonth = st.slider('Select your Month of Arrival',min_value=1,max_value=12)
wkd_lambda = (lambda x:
              0 if x == 'Mon' else
              1 if x == 'Tue' else
              2 if x == 'Wed' else
              3 if x == 'Thu' else
              4 if x == 'Fri' else
              5 if x == 'Sat' else
              6 )

awkd = wkd_lambda(st.selectbox('Select your weekday of Arrival',['Mon','Tue','Wed','Thu','Fri','Sat','Sun']))
dwkd = wkd_lambda(st.selectbox('Select your weekday of Departure',['Mon','Tue','Wed','Thu','Fri','Sat','Sun']))
wkend = st.number_input('How many weekend nights are there in stay?',min_value=0)
wk = st.number_input('How many week nights are there in stay?',min_value=0)
totn = wkend + wk
mkt = (lambda x:0 if x == 'offline' else 1)(st.selectbox('Mode of Booking',['Online','Offline']))
lt = st.number_input('How many days prior the booking was made',min_value=0)
price = st.number_input('what is the average price per room',min_value=0)
adults = st.number_input('Number of Adults',min_value=0)
spcl = st.selectbox('select the number of special request made',[0,1,2,3,4,5])
park = (lambda x:0 if x == 'No' else 1)(st.selectbox('If Parking Space Needed',['Yes','No']))


#Transform the data
lt_t,price_t = transformer.transform([[lt,price]])[0]

#Create the input list
input_list = [lt_t,spcl,price_t,adults,wkend,park,wk,mkt,amonth,awkd,totn,dwkd]

# Make prediction

prediction = model.predict_proba([input_list])[:,1][0]

#Lets show the probability
if st.button('Predict'):
    st.success(f'Cancellation Chances: {round(prediction,4)*100}%')