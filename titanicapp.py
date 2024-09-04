#Code for GitHub
import streamlit as st
import pickle

#Set the title and an image for the web app
st.title("Welcome to Franck's App :ship:")
st.image('image.png')

#Load the pre-trained model
with open('titanicpickle.pkl', 'rb') as pickle_file:
    pickle_load_file = pickle.load(pickle_file)

#Function to make predictions
def PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    prediction = pickle_load_file.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])
    print(prediction) #0/1
    return prediction

def main():
    st.title('Titanic Prediction App!')
    #The following code creates the input fields, that will be used by the user
    #for data entry for prediction
    # Pclass = st.text_input('Passenger Class')
    # Sex = st.text_input('Sex')
    # Age = st.text_input('Age')
    # SibSp = st.text_input('SibSp')
    # Parch = st.text_input('Parch')
    # Fare = st.text_input('Fare')
    # Embarked = st.text_input('Embarked')

    Pclass = st.number_input('Passenger Class (1, 2, 3)', min_value=1, max_value=3, step=1)
    Sex = st.text_input('Sex')
    Age = st.number_input('Age', min_value=0.42, max_value=80.0, step=0.01)
    SibSp = st.number_input('Number of Siblings/Spouses Aboard', min_value=0, step=1)
    Parch = st.number_input('Number of Parents/Children Aboard', min_value=0, step=1)
    Fare = st.number_input('Passenger Fare', min_value=0.0, step=0.01)
    Embarked = st.text_input('Embarked')
    result = ""

    #This code ensures that when the button 'Predict' is clicked, the PredictionFunction
    #which is defined above is called to make the prediction and store in the variable
    #'result'
    if st.button('Predict'):
        #age = "30" + 2 = error
        #age = 30 + 2 = 32

        #Convert inputs to appropriate data types
        Pclass = int(Pclass)
        Age = float(Age)
        SibSp = int(SibSp)
        Parch = int(Parch)
        Fare = float(Fare)

        result = PredictionFunction(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
    st.success(f"The output is: {result}")

#Calling the main function to execute the code in its body
main()



