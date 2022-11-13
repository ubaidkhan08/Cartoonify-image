import streamlit as st
from joblib import dump, load
import numpy as np

log_model = load('Multi_class_log_model.joblib')

def classify(sepal_length, sepal_width, petal_length, petal_width):
    inputs=np.array([[sepal_length, sepal_width, petal_length, petal_width]]).reshape(1, -1)
    prediction=log_model.predict(inputs)
    pred = '{}'.format(prediction)
    return(pred)


    
def main():
    st.title("Plant Species Prediction Model")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Iris Classification</h2>
    </div>
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    sepal_length=st.slider('Select Sepal Length', 0.0, 10.0)
    sepal_width=st.slider('Select Sepal Width', 0.0, 10.0)
    petal_length=st.slider('Select Petal Length', 0.0, 10.0)
    petal_width=st.slider('Select Petal Width', 0.0, 10.0)
    inputs=np.array([[sepal_length, sepal_width, petal_length, petal_width]]).reshape(1, -1)
   

    if st.button('Classify'):
        output=classify(sepal_length, sepal_width, petal_length, petal_width)
        st.success('The species of the plant is {}'.format(output[1:-1]))
       
     
if __name__=='__main__':
    main()
