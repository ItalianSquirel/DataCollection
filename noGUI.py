import csv

def save_data():
    date = input("Enter the date: ")
    time = input("Enter the time: ")
    location = input("Enter the location tag: ")
    photo_link = input("Enter the Google photo link: ")
    latitude = input("Enter the latitude: ")
    longitude = input("Enter the longitude: ")
    water_meter = input("Enter the water meter model: ")
    ph = input("Enter the pH: ")
    temperature = input("Enter the temperature (Celsius): ")
    tds = input("Enter the TDS (ppm): ")
    salinity = input("Enter the salinity (ppt): ")
    conductivity = input("Enter the conductivity (pS/cm): ")
    co2_level = input("Enter the CO2 level: ")
    pm25_reading = input("Enter the PM2.5 (ug/L) reading: ")
    pm25_filename = input("Enter the name of the PM2.5 file: ")
    voc_meter = input("Enter the VOC meter: ")
    voc_filename = input("Enter the name of the VOC meter file: ")
    notes = input("Enter additional notes/comments: ")

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

# Prompt for data entry and save
save_data()
