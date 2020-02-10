# mathsPython
Fun with maths using Python codes !!

# Code to export Data from Mongodb to JSON
mongoexport --db BharathMaths --collection MultiplicativePersistence --out data.json

# Code to export Data from Mongodb to csv
mongoexport --db=BharathMaths --collection=MultiplicativePersistence --type=csv --fields=Number,Steps --out=data.csv

# Sort the Data in Mongodb
use BharathMaths
db.MultiplicativePersistence.aggregate([{$sort : { Steps : -1} }],{allowDiskUse: true})

### Bharath C