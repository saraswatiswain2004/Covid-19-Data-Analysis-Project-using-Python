import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path ="/content/covid_19_clean_complete.csv"
df = pd.read_csv(file_path)

country = "India"   # Change to any country (e.g., "US", "Brazil", "Italy")
data = df[df["Country/Region"] == country].copy()

data["Date"] = pd.to_datetime(data["Date"])
data.fillna(0, inplace=True)

if "Confirmed" in data.columns and "Deaths" in data.columns and "Recovered" in data.columns:
    data["Active"] = data["Confirmed"] - data["Deaths"] - data["Recovered"]

data["Confirmed_7d"] = data["Confirmed"].rolling(7).mean()
data["Deaths_7d"] = data["Deaths"].rolling(7).mean()
data["Recovered_7d"] = data["Recovered"].rolling(7).mean()

plt.figure(figsize=(12,6))
plt.plot(data["Date"], data["Confirmed_7d"], label="Confirmed (7d avg)")
plt.plot(data["Date"], data["Deaths_7d"], label="Deaths (7d avg)")
plt.plot(data["Date"], data["Recovered_7d"], label="Recovered (7d avg)")
plt.title(f"Covid-19 Trends in {country}")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.show()

plt.figure(figsize=(12,6))
plt.plot(data["Date"], data["Active"], color="orange", label="Active Cases")
plt.title(f"Active Covid-19 Cases in {country}")
plt.xlabel("Date")
plt.ylabel("Active Cases")
plt.legend()
plt.show()

data.to_csv(f"covid19_{country.lower()}_processed.csv", index=False)
print(f"Processed data saved as covid19_{country.lower()}_processed.csv")
