import streamlit as st
import numpy as np

st.title("Healthcare Anomaly Detection ")

st.header("Enter Patient Vitals")

heart_rate = st.number_input("Heart Rate")
blood_pressure = st.number_input("Blood Pressure")
temperature = st.number_input("Temperature")
spo2 = st.number_input("SpO2")

if st.button("Check Status"):

    vitals = np.array([heart_rate, blood_pressure, temperature, spo2])

    score = np.sum([
        heart_rate < 60 or heart_rate > 100,
        blood_pressure < 80 or blood_pressure > 140,
        temperature < 36 or temperature > 38,
        spo2 < 95
    ])


    if score == 0:
        result = "LOW"
    elif score <= 2:
        result = "MEDIUM"
    else:
        result = "HIGH"

    st.success(f"Health Condition: {result}")


data = {
    "Heart Rate":[72,95,120],
    "Blood Pressure":[120,140,160],
    "Temperature":[36.5,37.2,39],
    "SpO2":[98,96,90]
}

import pandas as pd

df = pd.DataFrame(data)

st.write("Patient Data Table")
st.dataframe(df)

st.write("Average Values")

st.write("Heart Rate Mean:",df["Heart Rate"].mean())
st.write("Temperature Mean:",df["Temperature"].mean())


import os

folder = "patient_records"

if st.button("Create Patient Folder"):

    if not os.path.exists(folder):
        os.mkdir(folder)
        st.success("Folder Created")
    else:
        st.warning("Folder Already Exists")

files = os.listdir()

st.write("Files in System")
st.write(files)
{
  "code": "import streamlit as st\nimport numpy as np\n\nst.title('Healthcare Anomaly Detection - NumPy')\n\nst.header('Enter Patient Vitals')\n\nheart_rate = st.number_input('Heart Rate', key='hr')\nblood_pressure = st.number_input('Blood Pressure', key='bp')\ntemperature = st.number_input('Temperature', key='temp')\nspo2 = st.number_input('SpO2', key='spo2')\n\nif st.button('Check Status'):\n    vitals = np.array([heart_rate, blood_pressure, temperature, spo2])\n\n    score = np.sum([\n        heart_rate < 60 or heart_rate > 100,\n        blood_pressure < 80 or blood_pressure > 140,\n        temperature < 36 or temperature > 38,\n        spo2 < 95\n    ])\n\n    if score > 0:\n        st.error('Abnormal Vitals Detected')\n    else:\n        st.success('Patient Vitals Normal')"
}

