import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///database.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tablesx
Base.prepare(engine, reflect=True)

# Save reference to the table
#Fact = Base.classes.merged_file
metadata = MetaData()
metadata.reflect(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    print(len(Base.classes))
    print("lol")
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )

 


if __name__ == '__main__':
    app.run(debug=True)
