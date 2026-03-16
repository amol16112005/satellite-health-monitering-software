import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):

    model = IsolationForest(contamination=0.15, random_state=42)

    features = data[["temperature","battery","solar_current"]]

    data["anomaly"] = model.fit_predict(features)

    return data


def diagnose_issue(row):

    issues = []

    if row["temperature"] > 45:
        issues.append("Thermal system overheating")

    if row["battery"] < 3.7:
        issues.append("Battery voltage drop")

    if row["solar_current"] < 1.5:
        issues.append("Solar panel output low")

    return issues 