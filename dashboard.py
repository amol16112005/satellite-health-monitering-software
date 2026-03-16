import streamlit as st
import pandas as pd
from anomaly_detection import detect_anomalies, diagnose_issue

st.set_page_config(page_title="Satellite Mission Control", layout="wide")

st.title("🚀 AI-Based Satellite Digital Twin Monitoring System")

st.write("Real-time spacecraft telemetry monitoring with anomaly detection and root-cause diagnosis")

data = pd.read_csv("telemetry.csv")

data = detect_anomalies(data)

temp = data["temperature"].iloc[-1]
battery = data["battery"].iloc[-1]
solar = data["solar_current"].iloc[-1]

# DIGITAL TWIN PANEL

st.header("Satellite Digital Twin")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric("Thermal System", f"{temp} °C")

with col2:
    st.metric("Battery Voltage", f"{battery} V")

with col3:
    st.metric("Solar Output", f"{solar} A")

# TELEMETRY GRAPHS

st.header("Telemetry Visualization")

col1,col2,col3 = st.columns(3)

with col1:
    st.line_chart(data[["temperature"]])
    st.caption("Thermal System")

with col2:
    st.line_chart(data[["battery"]])
    st.caption("Power System")

with col3:
    st.line_chart(data[["solar_current"]])
    st.caption("Solar System")

# SUBSYSTEM STATUS

st.header("Subsystem Monitoring")

col1,col2,col3 = st.columns(3)

with col1:
    if temp > 45:
        st.error("Thermal subsystem overheating")
    else:
        st.success("Thermal subsystem nominal")

with col2:
    if battery < 3.7:
        st.warning("Battery voltage low")
    else:
        st.success("Power subsystem stable")

with col3:
    if solar < 1.5:
        st.warning("Solar output reduced")
    else:
        st.success("Solar subsystem nominal")

# HEALTH SCORE

health = 100

if temp > 45:
    health -= 30

if battery < 3.7:
    health -= 20

if solar < 1.5:
    health -= 20

st.header("Satellite Health")

st.metric("Overall Health Score", f"{health}%")

# AI ANOMALY DETECTION

st.header("AI Anomaly Detection")

anomalies = data[data["anomaly"] == -1]

if anomalies.empty:
    st.success("AI reports normal satellite behaviour")

else:

    for i,row in anomalies.iterrows():

        st.error(f"Anomaly detected at time step {row['time']}")

        problems = diagnose_issue(row)

        for p in problems:
            st.write("Cause:",p)

        solutions = {

        "Thermal system overheating":
        "Reduce onboard processor load or activate thermal control system",

        "Battery voltage drop":
        "Switch spacecraft to power-saving mode",

        "Solar panel output low":
        "Adjust satellite orientation toward sun"
        }

        for p in problems:
            st.write("Recommended action:",solutions[p])

# TELEMETRY TABLE

st.header("Telemetry Data")

st.write(data)