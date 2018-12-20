from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# engine = create_engine("sqlite:///Resources/hawaii.sqlite")

engine = create_engine("sqlite:///" + r"C:\Users\nsita\Dropbox\UCB\data-analytics\Homework\Homework 8\Resources\hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# We can view all of the classes that automap found
Base.classes.keys()
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)
conn = engine.connect()
date_list = []
prcp_list = []
temp_list = []
for instance in session.query(Measurement):
#     print(instance.date,instance.prcp)
    date_list.append(instance.date)
    prcp_list.append(instance.prcp)
    temp_list.append(instance.tobs)
# Design a query to retrieve the last 12 months of precipitation data and plot the results

# print(year_data)
# Calculate the date 1 year ago from today
# now = dt.datetime.now()
# todays_date = now.strftime("%Y-%m-%d")
# year_from_now = todays_date - 
# conn = engine.connect()
max_date = pd.read_sql("select date from measurement",conn)
# conn.close()
max_date = max_date.values.tolist()
max_date = max(max_date)
max_date = ''.join(max_date)
# print(max_date)
year,month,day = max_date.split('-')
# print(f"year:{year},month{month},day{day}")
days_to_subtract = 365
year_from_max = datetime(int(year),int(month),int(day)) - timedelta(days=days_to_subtract)
# print(year_from_max)
# Perform a query to retrieve the data and precipitation scores
# conn = engine.connect()
year_data = pd.read_sql(f"select * from measurement where date >= '{year_from_max}'",conn)
# conn.close()
# year_data = pd.read_sql(f"select * from measurement where date >= '2017-06-04'",conn)
# # Save the query results as a Pandas DataFrame and set the index to the date column
# print(year_data)
year_data = year_data[["date","prcp"]]
year_data = year_data.set_index("date")
# Sort the dataframe by date
year_data = year_data.sort_values("date")
# year_data = year_data.reset_index()
# year_data = year_data[[date,"prcp"]]
# year_data
year_data.head(20)
# len(year_data)
# Use Pandas Plotting with Matplotlib to plot the data
year_data.plot(kind="bar", figsize=(20,10), width = 3.5)
# plt.ylim(0,7)
# Rotate the xticks for the dates
plt.xticks(rotation=90)
# plt.axis('off')
# ax1 = plt.axes()
x_axis = plt.axes().axes.get_xaxis()
x_axis.set_visible(False)
plt.xlabel("date")
plt.savefig("precipitationgraph.png")
# plt.show()
# Use Pandas to calcualte the summary statistics for the precipitation data
year_data.describe()
# How many stations are available in this dataset?
# conn = engine.connect()
all_data = pd.read_sql("select * from measurement", conn)
# conn.close()
nunique = all_data.nunique()
nunique = nunique.to_dict()
nunique['station']
# What are the most active stations?
# List the stations and the counts in descending order.
most_active_station = all_data.groupby("station").count()

most_active_station_dict = most_active_station["id"].sort_values(ascending = False)
most_active_station["id"].sort_values(ascending = False)
most_active_station_dict = pd.DataFrame(most_active_station_dict)
most_active_station_dict = most_active_station_dict.to_dict()
most_active_station_dict
# Using the station id from the previous query, calculate the lowest temperature recorded, 
# highest temperature recorded, and average temperature most active station?
USC00519281 = pd.read_sql("select * from measurement where station = 'USC00519281'",conn)
USC00519281
USC00519281 = USC00519281[["tobs"]]
USC00519281_max = USC00519281.max().tolist()
USC00519281_min = USC00519281.min().tolist()
USC00519281_avg = USC00519281.mean().tolist()

to_list = (USC00519281_min,USC00519281_max,USC00519281_avg)
to_list
# records = []
# for value in to_list:
#     print(items)
# Choose the station with the highest number of temperature observations.
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram
highest_number_temp = all_data[["station","tobs"]]
highest_number_temp = highest_number_temp.groupby("station").count()
highest_number_temp = highest_number_temp.sort_values(by="tobs",ascending=False)
highest_number_temp
USC00519281_tobs = pd.read_sql(f"select date,tobs from measurement where station = 'USC00519281' and date >= '{year_from_max}'",conn)
# USC00519281_tobs
USC00519281_tobs_dict = USC00519281_tobs.to_dict(orient="records")
USC00519281_tobs_dict
USC00519281_tobs.plot(kind='hist')
# Write a function called `calc_temps` that will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
def calc_temps(start_date, end_date):
#     tmin = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
#     tavg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
#     tmax = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    """TMIN, TAVG, and TMAX for a list of dates.
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    toreturn = session.query(\
    func.min(Measurement.tobs),\
    func.avg(Measurement.tobs),\
    func.max(Measurement.tobs)).\
    filter(Measurement.date >=start_date).\
    filter(Measurement.date <=end_date).\
    all()
#     print(toreturn)
#     toreturn = toreturn[0]
#     TMIN = toreturn[0]
#     TAVE = toreturn[1]
#     TMAX = toreturn[2]
# #     print(TMIN, TAVE, TMAX)
    return toreturn
print(calc_temps('2012-02-28', '2012-03-05'))
# Use your previous function `calc_temps` to calculate the tmin, tavg, and tmax 
# for your trip using the previous year's data for those same dates.
print(max_date)
max_date = str(max_date)
year_from_max = str(year_from_max.date())
to_bar_chart = calc_temps(year_from_max,max_date)
# print(to_bar_chart)
convert_to_individual = to_bar_chart[0]
TMIN = convert_to_individual[0]
TAVG = convert_to_individual[1]
TMAX = convert_to_individual[2]

tavg_frame = pd.DataFrame({"Trip Avg Temp":[TAVG]})
print(tavg_frame)
tavg_frame.plot(kind="bar",width=.3,yerr=(TMAX-TMIN),figsize=(5,10))
# print(TMIN,TAVE,TMAX)
# Plot the results from your previous query as a bar chart. 
plt.title("Trip Avg Temp")
plt.legend('')
# plt.xticks(ticks='')
plt.xlabel("Avg Temp")
# plt.bar(x="",height=TAVG,width=.01,yerr=(TMAX-TMIN))
# plt.figure(figsize=(10,4))
# Use "Trip Avg Temp" as your Title
# Use the average temperature for the y value
plt.ylabel("Average Temperature")
# Use the peak-to-peak (tmax-tmin) value as the y error bar (yerr)

plt.tight_layout()
plt.savefig("BarChart.jpg")
# plt.show()
# Calculate the rainfall per weather station for your trip dates using the previous year's matching dates.
# Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation
start_date = '2012-02-28'
end_date = '2012-03-05'

# rainfall_per_station = session.query(Measurement.station,\
#                                     func.sum(Measurement.prcp)).\
#                                     filter(Measurement.date >=start_date).\
#                                     filter(Measurement.date <=end_date).\
#                                     group_by(Measurement.station).\
#                                     order_by(func.sum(Measurement.prcp).desc()).\
#                                     all()


measurement_table = pd.read_sql(f"select * from measurement where date between '{start_date}' and '{end_date}'", conn)
station_table = pd.read_sql('select * from station', conn)


# rainfall_per_station
# rainfall_per_station
measurement_table = measurement_table[["station","prcp"]]
station_table = station_table[["station","name","latitude","longitude","elevation"]]
measurement_table_grouped = measurement_table.groupby("station").sum()
measurement_table_grouped = measurement_table_grouped.sort_values(by="prcp", ascending=False)

# print(measurement_table_grouped.head())
# print(station_table.head())
measurement_table_grouped

station_table
measurement_station_merged = measurement_table_grouped.merge(station_table, how='inner',on="station")
measurement_station_merged = measurement_station_merged[["station","name","latitude","longitude","elevation","prcp"]]
measurement_station_merged_dict = measurement_station_merged.to_dict(orient='records')
# print(measurement_station_merged_dict)




from flask import Flask, jsonify

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    return jsonify(measurement_station_merged_dict)

@app.route("/api/v1.0/stations")
def stations():
    
    return jsonify(most_active_station_dict)

@app.route("/api/v1.0/tobs")
def tobs():
    
    return jsonify(USC00519281_tobs_dict)

@app.route("/api/v1.0/<string:start>")
def start():
    # to_retun = calc_temps(start,max_date)
    # convert_to_individual = to_retun[0]
    # TMIN = convert_to_individual[0]
    # TAVG = convert_to_individual[1]
    # TMAX = convert_to_individual[2]

    # start_date_only_dict = pd.DataFrame({"Temp Min":[TMIN],
    #             "Temp Max":[TMAX],
    #             "Temp Average":[TAVG]})
    # start_date_only_dict = start_date_only_dict.to_dict()

    return start

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    to_retun = calc_temps(start,end)
    convert_to_individual = to_retun[0]
    TMIN = convert_to_individual[0]
    TAVG = convert_to_individual[1]
    TMAX = convert_to_individual[2]

    start_end_date_dict = pd.DataFrame({"Temp Min":[TMIN],
                "Temp Max":[TMAX],
                "Temp Average":[TAVG]})
    start_end_date_dict = start_end_date_dict.to_dict()
    return jsonify(start_end_date_dict)


@app.route("/")
def welcome():
    return (
        f"Welcome to the Homework 8 Flask API<br/>"
        f"Available Routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/start<br>"
        f"/api/v1.0/start/end<br>"

    )


if __name__ == "__main__":
    app.run(debug=True)
