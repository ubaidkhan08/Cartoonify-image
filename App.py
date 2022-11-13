import streamlit as st
from joblib import dump, load
import numpy as np
import pandas as pd


def main():
   
    st.title("Natural Gas Prediction Model!")
    html_temp = """
    <div style="background-color:teal ;padding:20px">
    </div>
    """
    
    st.subheader('Crude Oil Price')
    COP = st.number_input('(in Dollars)')


    st.subheader('US Dollar Index')
    USDI = st.number_input('Enter')


    st.subheader('Texas Temperature')
    TT = st.slider('(In Fahrenheit)', 0.0, 110.0)


    st.subheader('California Temperature')
    CT = st.slider('(In Fahrenheit)', 0.0, 105.0)

    
    st.subheader('Natural Gas Production in the USA')
    NGP = st.number_input('(in Trillion cubic feet)')


    st.subheader('GDP of USA')
    GDP = st.number_input('(in Billion Dollars)')


    st.subheader('US Natural Gas Reserves')
    NGR = st.number_input('(in Trillion cubic feet)',key=0)

    st.subheader('US Natural Gas Consumption')
    NGC = st.number_input('(in Trillion cubic feet)',key=1)

    st.subheader('US Natural Gas Imports')
    NGI = st.number_input('(in Trillion cubic feet)',key=2)
    
    if st.button('Predict Natural Gas Price'):
        output= classify(COP,USDI,TT,CT,NGP,GDP,NGR,NGC,NGI)
        #st.success()
        st.success(output)

        
def classify(COP,USDI,TT,CT,NGP,GDP,NGR,NGC,NGI):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()

    inputs = [[COP,USDI,TT,CT,NGP,GDP,NGR,NGC,NGI]]

    from joblib import dump, load
    log_model = load('naturalgas_predict.joblib')
    predictionn = ((log_model.predict([inputs[0]])))
    predictionnn = round(predictionn[0],3)
    return('Predicted Price: {}').format(predictionnn)
    
    
if __name__=='__main__':
    main()
