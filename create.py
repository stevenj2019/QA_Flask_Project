from application import db
from application.models import Locations, Admin, Contact

db.drop_all()
db.create_all()

with open("Tooling/office_location_data.csv", "r") as Data:
    for line in Data:
        DATASTREAM = line.split(',')
        print(DATASTREAM)
        Location_Data = Locations(
            first_line = DATASTREAM[0], 
            second_line = DATASTREAM[1],
            city = DATASTREAM[2],
            post_code = DATASTREAM[3],  
        )
        db.session.add(Location_Data)

db.session.commit()
