# Import Dependencies
import numpy as np
import datetime as dt
from datetime import date
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# Flask Setup

app = Flask(__name__)

# Flask Routes
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Dates and observations of rain fall from last year."""
    results = session.query(Measurement.date,Measurement.prcp)\
    .filter(Measurement.date > '2016-08-22').all()
    data = list(np.ravel(results))
    return jsonify(data)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset"""
    results = session.query(Station.station, Station.name).all()
    data = list(np.ravel(results))
    return jsonify(data)

@app.route("/api/v1.0/tobs")
def temp():
    """Return a JSON list of Temperature observation for the previous year"""
    results = session.query(Measurement.date, Measurement.tobs)\
    .filter(Measurement.date > '2016-08-22').all()
    data = list(np.ravel(results))
    return jsonify(data)

@app.route("/api/v1.0/<start>")
def start(start):
    """Return a JSON list of the minimum temperature, the average temperature,\
    and the max temperature for a given start date"""
    
    year, month, day = map(int, start.split('-'))
    date_start = dt.date(year, month, day)
    results = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),\
                            func.avg(Measurement.tobs)).filter(Measurement.date >= date_start).all()
    data = list(np.ravel(results))
    return jsonify(data)

@app.route("/api/v1.0/<start>/<end>")
def range_temp(start,end):
    """Return a JSON list of the minimum temperature, the average temperature,\
    and the max temperature for the given range"""
    year, month, day = map(int, start.split('-'))
    date_start = dt.date(year, month, day)
    year2, month2, day2 = map(int, end.split('-'))
    date_end = dt.date(year2, month2, day2)
    
    results = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),\
                            func.avg(Measurement.tobs)).filter(Measurement.date >= date_start).filter(Measurement.date <= date_end).all()
    data = list(np.ravel(results))
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)