import streamlit as st
import pickle
import pandas as pd
from datetime import datetime

# Load the trained model
model = pickle.load(open("flight_rf.pkl", "rb"))

st.title("✈️ Flight Fare Prediction System")

# Input fields
dep_date = st.date_input("Departure Date")
dep_time = st.time_input("Departure Time")

arr_date = st.date_input("Arrival Date")
arr_time = st.time_input("Arrival Time")

# Combine date and time into datetime
date_dep = datetime.combine(dep_date, dep_time)
date_arr = datetime.combine(arr_date, arr_time)

Total_stops = st.selectbox("Total Stops", [0, 1, 2, 3, 4])

airline = st.selectbox("Airline", [
    'Jet Airways', 'IndiGo', 'Air India', 'Multiple carriers',
    'SpiceJet', 'Vistara', 'GoAir',
    'Multiple carriers Premium economy', 'Jet Airways Business',
    'Vistara Premium economy', 'Trujet'
])

source = st.selectbox("Source", ['Delhi', 'Kolkata', 'Mumbai', 'Chennai'])

destination = st.selectbox("Destination", [
    'Cochin', 'Delhi', 'New_Delhi', 'Hyderabad', 'Kolkata'
])

# Extract datetime components
Journey_day = date_dep.day
Journey_month = date_dep.month
Dep_hour = date_dep.hour
Dep_min = date_dep.minute
Arrival_hour = date_arr.hour
Arrival_min = date_arr.minute
dur_hour = abs(Arrival_hour - Dep_hour)
dur_min = abs(Arrival_min - Dep_min)

# Airline encoding
airline_list = [
    'Air India', 'GoAir', 'IndiGo', 'Jet Airways', 'Jet Airways Business',
    'Multiple carriers', 'Multiple carriers Premium economy', 'SpiceJet',
    'Trujet', 'Vistara', 'Vistara Premium economy'
]
airline_encoding = [1 if airline == name else 0 for name in airline_list]

# Source encoding
source_dict = {'Delhi': [1, 0, 0, 0], 'Kolkata': [0, 1, 0, 0],
               'Mumbai': [0, 0, 1, 0], 'Chennai': [0, 0, 0, 1]}
s_Delhi, s_Kolkata, s_Mumbai, s_Chennai = source_dict.get(source, [0, 0, 0, 0])

# Destination encoding
destination_dict = {
    'Cochin': [1, 0, 0, 0, 0],
    'Delhi': [0, 1, 0, 0, 0],
    'Hyderabad': [0, 0, 1, 0, 0],
    'Kolkata': [0, 0, 0, 1, 0],
    'New_Delhi': [0, 0, 0, 0, 1]
}
d_Cochin, d_Delhi, d_Hyderabad, d_Kolkata, d_New_Delhi = destination_dict.get(destination, [0, 0, 0, 0, 0])

# Predict button
if st.button("Predict Fare"):
    features = [[
        Total_stops,
        Journey_day,
        Journey_month,
        Dep_hour,
        Dep_min,
        Arrival_hour,
        Arrival_min,
        dur_hour,
        dur_min,
        *airline_encoding,
        s_Chennai,
        s_Delhi,
        s_Kolkata,
        s_Mumbai,
        d_Cochin,
        d_Delhi,
        d_Hyderabad,
        d_Kolkata,
        d_New_Delhi
    ]]

    prediction = model.predict(features)
    output = round(prediction[0], 2)
    st.success(f"Your Flight price is ₹{output}")
