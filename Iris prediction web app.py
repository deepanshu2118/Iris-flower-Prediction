import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/LENOVO/OneDrive/Desktop/some project with streamlit/Iris_project/Iris.pkl', 'rb'))

def Iris_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return 'setosa'
    elif (prediction[0]==1):
        return "versicolor"
    else:
        return "virginica"


def main():
    st.title('Iris Classification')
    st.image("Iris_flower.png","Iris flower")

    SepalLegthCm=st.slider('SepalLegthCm:',min_value=0.0,max_value=10.0,step=0.1)
    PetalWidthCm=st.slider('PetalWidthCm:',min_value=0.0,max_value=10.0,step=0.1)

    Irisity=''

    if st.button('Iris test result'):
        Irisity=Iris_prediction([SepalLegthCm,PetalWidthCm])

    st.success(Irisity)


if __name__=='__main__':
    main()