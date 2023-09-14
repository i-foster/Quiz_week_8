import matplotlib.pyplot as plt
import sqlite3


years = []
co2 = []
temp = []

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 


conn = sqlite3.connect("climate.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM climate_data")
rows = cursor.fetchall()

# Populate the lists with data
for row in rows:
    Year, C02, Temperature = row
    years.append(Year)
    co2.append(CO2)
    tempp.append(temperature)