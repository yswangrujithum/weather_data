# Weather Analysis
The project that analyzing the weather in Hawaii. We are looking at the level of precipitation and temperature in certain area in Hawaii. 
## Getting started
The following programs are required to run the project in your local machine. 
### Available Resources
* Measurement CSV file
* Stations CSV file
### Requirement
* Python 3.3
* sqlalchemy

``` pip install SQLAlchemy```

* matplotlib
* numpy
* pandas
* datetime
* flask

``` pip install Flask```

### Break Down of the Project
#### Jupyter Notebook
Reflect the table into SQLAlchemy ORM

```engine = create_engine("sqlite:///Resources/hawaii.sqlite")```

Exploring the climate from created engine and use the matplotlib to plot the obtained data based on specific date

```data_df.plot("date","prcp")```

Exploring the climate based on specific date on specific location

```year_data_high_temp = session.query(Measurement.date,Measurement.tobs).filter(Measurement.station == 'USC00519397', Measurement.date > '2016-08-22').all()```

Exploring the temperature based on the specific date and specific location using the function called 'calc_temp'

```temp_data = calc_temps(start_date,end_date)```

#### Flask Routes
Another technique to obtain JSON information from the data.

```app = Flask(__name__)```

### Author
Yanin Swangrujithum 

