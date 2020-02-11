# Inspiration

* http://mathworld.wolfram.com/MultiplicativePersistence.html
* https://www.youtube.com/watch?v=Wim9WJeDTHQ&t=744s

# Code to export Data from Mongodb to JSON
```shell
mongoexport --db BharathMaths --collection MultiplicativePersistence --out data.json
```

# Code to export Data from Mongodb to csv
```shell
mongoexport --db=BharathMaths --collection=MultiplicativePersistence --type=csv --fields=Number,Steps --out=data.csv
```

# Sort the Data in Mongodb
```javascript
use BharathMaths;
db.MultiplicativePersistence.aggregate([{$sort : { Steps : -1} }],{allowDiskUse: true})
```
### Bharath C