import streamlit as st
import pickle
import pandas as pd
import datetime
from PIL import Image


def main():
    
    st.title("Flight Ticket Price Predictor")
    image = Image.open('airplane.jpg')
    st.image(image, width = 700)
    
    

    #source

    source = st.selectbox('Source City',['Bangalore','Chennai','Delhi','Kolkata','Mumbai','Hyderabad','Ahmedabad'])

    if (source == "Bangalore"):
        Source_Bangalore = 1
        Source_Chennai = 0
        Source_Delhi = 0
        Source_Hyderabad = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
    elif (source == 'Chennai'):
        Source_Bangalore = 0
        Source_Chennai = 1
        Source_Delhi = 0
        Source_Hyderabad = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
    elif (source == 'Delhi'):
        Source_Bangalore = 0
        Source_Chennai = 0
        Source_Delhi = 1
        Source_Hyderabad = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
    elif (source == 'Kolkata'):
        Source_Bangalore = 0
        Source_Chennai = 0
        Source_Delhi = 0
        Source_Hyderabad = 0
        Source_Kolkata = 1
        Source_Mumbai = 0
    elif (source == 'Mumbai'):
        Source_Bangalore = 0
        Source_Chennai = 0
        Source_Delhi = 0
        Source_Hyderabad = 0
        Source_Kolkata = 0
        Source_Mumbai = 1
    elif (source == 'Hyderabad'):
        Source_Bangalore = 0
        Source_Chennai = 0
        Source_Delhi = 0
        Source_Hyderabad = 1
        Source_Kolkata = 0
        Source_Mumbai = 0
    else:
        Source_Bangalore = 0
        Source_Chennai = 0
        Source_Delhi = 0
        Source_Hyderabad = 0
        Source_Kolkata = 0
        Source_Mumbai = 0


    #destination

    destination = st.selectbox("Destination City",['Bangalore','Chennai','Delhi','Kolkata','Mumbai','Hyderabad','Ahmedabad'])

    if (destination == "Bangalore"):
        Destination_Bangalore = 1
        Destination_Chennai = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 0
        Destination_Mumbai = 0
    elif (destination == 'Chennai'):
        Destination_Bangalore = 0
        Destination_Chennai = 1
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 0
        Destination_Mumbai = 0
    elif (destination == 'Delhi'):
        Destination_Bangalore = 0
        Destination_Chennai = 0
        Destination_Delhi = 1
        Destination_Hyderabad = 0
        Destination_Kolkata = 0
        Destination_Mumbai = 0
    elif (destination == 'Kolkata'):
        Destination_Bangalore = 0
        Destination_Chennai = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 1
        Destination_Mumbai = 0
    elif (destination == 'Mumbai'):
        Destination_Bangalore = 0
        Destination_Chennai = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 0
        Destination_Mumbai = 1
    elif (destination == 'Hyderabad'):
        Destination_Bangalore = 0
        Destination_Chennai = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 1
        Destination_Kolkata = 0
        Destination_Mumbai = 0
    else:
        Destination_Bangalore = 0
        Destination_Chennai = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 0
        Destination_Mumbai = 0


    #airline

    airline = st.selectbox('Airline',['AirAsia','AkasaAir','AllianceAir','GO FIRST','Indigo','SpiceJet','StarAir','Vistara','Air India'])

    if (airline == 'AirAsia'):

        Airline_AirAsia = 1
        Airline_AkasaAir = 0
        Airline_AllianceAir = 0
        Airline_GOFIRST = 0 
        Airline_Indigo = 0
        Airline_SpiceJet = 0
        Airline_StarAir = 0
        Airline_Vistara = 0
    
    elif (airline == 'AkasaAir'):

        Airline_AirAsia = 0
        Airline_AkasaAir = 1
        Airline_AllianceAir = 0
        Airline_GOFIRST = 0 
        Airline_Indigo = 0
        Airline_SpiceJet = 0
        Airline_StarAir = 0
        Airline_Vistara = 0
    elif (airline == 'AllianceAir'):

        Airline_AirAsia = 0
        Airline_AkasaAir = 0
        Airline_AllianceAir = 1
        Airline_GOFIRST = 0 
        Airline_Indigo = 0
        Airline_SpiceJet = 0
        Airline_StarAir = 0
        Airline_Vistara = 0
    elif (airline == 'GO FIRST'):

        Airline_AirAsia = 0
        Airline_AkasaAir = 0
        Airline_AllianceAir = 0
        Airline_GOFIRST = 1 
        Airline_Indigo = 0
        Airline_SpiceJet = 0
        Airline_StarAir = 0
        Airline_Vistara = 0
    elif (airline == 'Indigo'):

        Airline_AirAsia = 0
        Airline_AkasaAir = 0
        Airline_AllianceAir = 0
        Airline_GOFIRST = 0 
        Airline_Indigo = 1
        Airline_SpiceJet = 0
        Airline_StarAir = 0
        Airline_Vistara = 0
    elif (airline == 'SpiceJet'):

        Airline_AirAsia = 0
        Airline_AkasaAir = 0
        Airline_AllianceAir = 0
        Airline_GOFIRST = 0 
        Airline_Indigo = 0
        Airline_SpiceJet = 1
        Airline_StarAir = 0
        Airline_Vistara = 0
    elif (airline == 'StarAir'):

        Airline_AirAsia = 0
        Airline_AkasaAir = 0
        Airline_AllianceAir = 0
        Airline_GOFIRST = 0 
        Airline_Indigo = 0
        Airline_SpiceJet = 0
        Airline_StarAir = 1
        Airline_Vistara = 0
    elif (airline == 'Vistara'):

        Airline_AirAsia = 0
        Airline_AkasaAir = 0
        Airline_AllianceAir = 0
        Airline_GOFIRST = 0 
        Airline_Indigo = 0
        Airline_SpiceJet = 0
        Airline_StarAir = 0
        Airline_Vistara = 1
    elif (airline == 'Air India'):

        Airline_AirAsia = 0
        Airline_AkasaAir = 0
        Airline_AllianceAir = 0
        Airline_GOFIRST = 0 
        Airline_Indigo = 0
        Airline_SpiceJet = 0
        Airline_StarAir = 0
        Airline_Vistara = 0


    #journey day
    st.sidebar.subheader("Select Departure")
    m = pd.to_datetime("today").month
    d = pd.to_datetime("today").day
    y = pd.to_datetime("today").year
    dep = st.sidebar.date_input("Day" , datetime.date(y,m,d))

    day = dep.strftime('%A')

    if (day == 'Sunday'):
        day_in = 6
    elif (day == 'Monday'):
        day_in = 0
    elif (day == 'Tuesday'):
        day_in = 1
    elif (day == 'Wednesday'):
        day_in = 2
    elif (day == 'Thursday'):
        day_in = 3
    elif (day == 'Friday'):
        day_in = 4
    elif (day == 'Saturday'):
        day_in = 5


    #Departure time

    dept_time = st.sidebar.selectbox("Departure time",['Between 12 AM - 5 AM','Between 5 AM - 12 PM','Between 12 PM - 4 PM','Between 4 PM - 7 PM','Between 7 PM - 10 PM','Between 10 PM - 12 AM'])

    if (dept_time == 'Between 12 AM - 5 AM'):
        dep = 0
    elif (dept_time == 'Between 5 AM - 12 PM'):
        dep = 1
    elif (dept_time == 'Between 12 PM - 4 PM'):
        dep = 2
    elif (dept_time == 'Between 4 PM - 7 PM'):
        dep = 3
    elif (dept_time == 'Between 7 PM - 10 PM'):
        dep = 4
    elif (dept_time == 'Between 10 PM - 12 AM'):
        dep = 5

    #Arrival time

    arr_time = st.sidebar.selectbox("Arrival time",['Between 12 AM - 5 AM','Between 5 AM - 12 PM','Between 12 PM - 4 PM','Between 4 PM - 7 PM','Between 7 PM - 10 PM','Between 10 PM - 12 AM'])

    if (arr_time == 'Between 12 AM - 5 AM'):
        arr = 0
    elif (arr_time == 'Between 5 AM - 12 PM'):
        arr = 1
    elif (arr_time == 'Between 12 PM - 4 PM'):
        arr = 2
    elif (arr_time == 'Between 4 PM - 7 PM'):
        arr = 3
    elif (arr_time == 'Between 7 PM - 10 PM'):
        arr = 4
    elif (arr_time == 'Between 10 PM - 12 AM'):
        arr = 5
    
   
    
    #days_left

    days_left = st.slider('Days before the Journey',0,50,3)

    #total stops

    stops = st.selectbox('No of Stops',["Non Stop","Single Stop","2+ Stops"])
    

    if (stops == 'Non Stop'):
        stops_inp = 0
    elif (stops == 'Single Stop'):
        stops_inp = 1
    else:
        stops_inp = 2

    
    #class
    
    classes = st.selectbox("Class",["Economy","Premium Economy","Business","First Class"])
    
    if (classes == "Economy"):
        class_inp = 0
    elif (classes == 'Premium Economy'):
        class_inp = 1
    elif (classes == 'Business'):
        class_inp = 2
    else:
        class_inp = 3


    
    #duration
    duration = st.sidebar.number_input('Duration in hours') #find it from arr and dest 


    
    #load model

    model = pickle.load(open('Airplane_model.pkl','rb'))
    scaler = pickle.load(open('Scaler.pkl','rb'))


    #features

    features = [stops_inp,class_inp,days_left,day_in,dep,arr,duration,
                Airline_AirAsia,Airline_AkasaAir,Airline_AllianceAir,
                Airline_GOFIRST,Airline_Indigo,Airline_SpiceJet,Airline_StarAir,Airline_Vistara,
                Source_Bangalore,Source_Chennai,Source_Delhi,Source_Hyderabad,Source_Kolkata,Source_Mumbai,
                Destination_Bangalore,Destination_Chennai,Destination_Delhi,Destination_Hyderabad,Destination_Kolkata,Destination_Mumbai]

    #prediction
    ok = st.button('PREDICT')

    if ok:
        pred = model.predict(scaler.transform([features]))

        for i in pred:
            st.write("Your Ticket Charge is :", round(i,3), 'INR')
            st.write("*Happy and Safe Journey..*")
 
main()


 
    
    








    
    


















       

