import streamlit as st
from joblib import dump, load
import numpy as np
import pandas as pd


def main():
    st.title("Titanic Passenger Survival Prediction Model")
    html_temp = """
    <div style="background-color:teal ;padding:20px">
    </div>
    """

    st.subheader('Enter Your Age')
    AGE = st.number_input('Age')


    st.subheader('Enter Your Ticket Price in $')
    FARE = st.slider('Fare', 0.0, 520.0)


    st.subheader('Choose Your Gender')
    S = st.radio('Gender', options=('Female','Male','Transgenger','Prefer not to say'))
    if S == 'Female':
        SEX = 1

    elif S == 'Male':
        SEX = 0

    elif S == 'Transgenger':
        SEX = 0.5

    elif S == 'Prefer not to say':
        SEX = 0.5



    st.subheader('Choose Passenger Class')
    C = st.radio('P-class',options=('1st','2nd','3rd'))

    if C == '1st':
        Pc = 1

    elif C == '2nd':
        Pc = 2

    elif C == '3rd':
        Pc = 3

    
    st.subheader('Choose Port of Boarding the Titanic')
    E = st.selectbox('Embarkment' ,options=('Cherbourg', 'Queenstown', 'Southampton'))
    if E == 'Cherbourg':
        EMB = 1

    elif E == 'Queenstown':
        EMB = 2 

    elif E == 'Southampton':
        EMB = 0 


    st.subheader('No. of Siblings/Spouses Aboard the Ship')
    SibSp = st.number_input('Siblings or Spouses')


    st.subheader('No. of Parents/Children Aboard the Ship')
    Parch = st.number_input('Parents or Children')

    


if __name__=='__main__':
    main()
