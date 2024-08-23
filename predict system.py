import pandas as pd 
import numpy as np
import pickle
loaded_model = pickle.load(open('C:/Users/LENOVO/OneDrive/Desktop/some project with streamlit/Iris_project/Iris.pkl', 'rb'))

input_data=(4.6,0.3)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
    print('setosa')
elif (prediction[0]==1):
    print("versicolor")
else:
    print("virginica")