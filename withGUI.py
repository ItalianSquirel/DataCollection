import tkinter as tk
import csv

def save_data():
    date = entry_date.get()
    time = entry_time.get()
    location = entry_location.get()
    photo_link = entry_photo_link.get()
    latitude = entry_latitude.get()
    longitude = entry_longitude.get()
    water_meter = entry_water_meter.get()
    ph = entry_ph.get()
    temperature = entry_temperature.get()
    tds = entry_tds.get()
    salinity = entry_salinity.get()
    conductivity = entry_conductivity.get()
    co2_level = entry_co2_level.get()
    pm25_reading = entry_pm25_reading.get()
    pm25_filename = entry_pm25_filename.get()
    voc_meter = entry_voc_meter.get()
    voc_filename = entry_voc_filename.get()
    notes = entry_notes.get()

    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        
        # Check if the file is empty
        if file.tell() == 0:
            writer.writerow(['Date', 'Time', 'Location', 'Photo Link', 'Latitude',
                             'Longitude', 'Water Meter', 'pH', 'Temperature (C)',
                             'TDS (ppm)', 'Salinity (ppt)', 'Conductivity (pS/cm)',
                             'CO2 Level', 'PM2.5 (ug/L) Reading', 'Name of PM2.5 File',
                             'VOC Meter', 'Name of VOC Meter File',
                             'Additional Notes/Comments'])
        
        writer.writerow([date, time, location, photo_link, latitude, longitude,
                         water_meter, ph, temperature, tds, salinity, conductivity,
                         co2_level, pm25_reading, pm25_filename, voc_meter,
                         voc_filename, notes])
    print("Data saved successfully!")

# Create the GUI
window = tk.Tk()
window.title("Data Entry Form")

# Labels
labels = ['Date', 'Time', 'Location', 'Photo Link', 'Latitude', 'Longitude',
          'Water Meter', 'pH', 'Temperature (C)', 'TDS (ppm)', 'Salinity (ppt)',
          'Conductivity (pS/cm)', 'CO2 Level', 'PM2.5 (ug/L) Reading',
          'Name of PM2.5 File', 'VOC Meter', 'Name of VOC Meter File',
          'Additional Notes/Comments']

for i in range(len(labels)):
    label = tk.Label(window, text=labels[i])
    label.grid(row=i+1, column=0, sticky="e")

# Entry fields
entry_date = tk.Entry(window)
entry_date.grid(row=1, column=1)

entry_time = tk.Entry(window)
entry_time.grid(row=2, column=1)

entry_location = tk.Entry(window)
entry_location.grid(row=3, column=1)

entry_photo_link = tk.Entry(window)
entry_photo_link.grid(row=4, column=1)

entry_latitude = tk.Entry(window)
entry_latitude.grid(row=5, column=1)

entry_longitude = tk.Entry(window)
entry_longitude.grid(row=6, column=1)

entry_water_meter = tk.Entry(window)
entry_water_meter.grid(row=7, column=1)

entry_ph = tk.Entry(window)
entry_ph.grid(row=8, column=1)

entry_temperature = tk.Entry(window)
entry_temperature.grid(row=9, column=1)

entry_tds = tk.Entry(window)
entry_tds.grid(row=10, column=1)

entry_salinity = tk.Entry(window)
entry_salinity.grid(row=11, column=1)

entry_conductivity = tk.Entry(window)
entry_conductivity.grid(row=12, column=1)

entry_co2_level = tk.Entry(window)
entry_co2_level.grid(row=13, column=1)

entry_pm25_reading = tk.Entry(window)
entry_pm25_reading.grid(row=14, column=1)

entry_pm25_filename = tk.Entry(window)
entry_pm25_filename.grid(row=15, column=1)

entry_voc_meter = tk.Entry(window)
entry_voc_meter.grid(row=16, column=1)

entry_voc_filename = tk.Entry(window)
entry_voc_filename.grid(row=17, column=1)

entry_notes = tk.Entry(window)
entry_notes.grid(row=18, column=1)

# Save button
save_button = tk.Button(window, text="Save", command=save_data)
save_button.grid(row=19, column=0, columnspan=2, pady=10)

window.mainloop()
