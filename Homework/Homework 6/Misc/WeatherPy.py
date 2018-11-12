
# coding: utf-8

# # WeatherPy
# ----
#
# ### Analysis
# * As expected, the weather becomes significantly warmer as one approaches the equator (0 Deg. Latitude). More interestingly, however, is the fact that the southern hemisphere tends to be warmer this time of year than the northern hemisphere. This may be due to the tilt of the earth.
# * There is no strong relationship between latitude and cloudiness. However, it is interesting to see that a strong band of cities sits at 0, 80, and 100% cloudiness.
# * There is no strong relationship between latitude and wind speed. However, in northern hemispheres there is a flurry of cities with over 20 mph of wind.
#
# ---
#
# #### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time

# Dependencies
import openweathermapy.core as owm

# Import API key
from api_keys import api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# ## Generate Cities List

# In[ ]:


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name

    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


# ### Perform API Calls
# * Perform a weather check on each city using a series of successive API calls.
# * Include a print log of each city as it'sbeing processed (with the city number and city name).
#

# In[ ]:

lat = []
lng = []
nl = "\n"
columns =["City","Cloudiness","Country","Date","Humidity","Lat","Lng","Max Temp","Wind Speed"]
city_weather_data = pd.DataFrame(index=index,columns=columns) 

def parseinformation():
        city_name = response["name"]
        cloudiness = response["clouds"]["all"]
        country = response["sys"]["country"]
        date = response["dt"]
        humidity = response["coord"]["lat"]
        lat = response["coord"]["lat"]
        lng = response["coord"]["lon"]
        max_temp = response["main"]["temp"]
        wind_speed = response["wind"]["speed"]
        print(f"Processing {city_name}: {nl} cloudiness: {cloudiness},{nl} country: {country}")



for city in cities:
        # print(city)
        # Save config information
        url = "http://api.openweathermap.org/data/2.5/weather?"
        query_url = url + "appid=" + api_key + "&q=" + str(city)
        # Create settings dictionary with information we're interested in
        #     settings = {"units": "metric", "appid": api_key}
        params = {"appid": api_key, "q": city}
        # Get current weather
        #     current_weather_paris = owm.get_current(city, **settings)
        #     print(f"Current weather object for {city}: {current_weather_paris}.")
        # # Build URL using the Google Maps API
        response = requests.get(query_url, params=params)
        #     print(response.url)
        response = response.json()
        try:
                 parseinformation()
        except:
                pass
                print(f"Passed city")


#     city_name = response["name"]
#     cloudiness = response["clouds"]["all"]
#     country = response["sys"]["country"]
#     date = response["dt"]
#     humidity = response["coord"]["lat"]
#     lat = response["coord"]["lat"]
#     lng = response["coord"]["lon"]
#     max_temp = response["main"]["temp"]
#     wind_speed = response["wind"]["speed"]
#     print(f"Processing {city_name}: {nl} cloudiness: {cloudiness},{nl} country: {country}")


#     print(lat)
#     print(lng)
#     print(lat_lngs)
#     print(response)


# ### Convert Raw Data to DataFrame
# * Export the city data into a .csv.
# * Display the DataFrame

# ### Plotting the Data
# * Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.
# * Save the plotted figures as .pngs.

# #### Latitude vs. Temperature Plot

# #### Latitude vs. Humidity Plot

# #### Latitude vs. Cloudiness Plot

# #### Latitude vs. Wind Speed Plot
