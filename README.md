# Squirrel-Tracker
Squirrel Tracker is a web application developed with Django framework which tracks the squirrels in Central Park and allows users to view, update and add squirrel sightings. 

## Description

### Management Commands
  - **Import data**: use management commands to import data from "squirrel_data.csv"-- 2018 Central Park Squirrel Census. The file path should be specified. Sightings with duplicate Squirrel Unique IDs will only be imported once.
```sh
python manage.py import_squirrel_data /path/to/file.csv
```

  - **Export data**: use management commands to export data in csv format. The file path should be specified.
```sh
python manage.py export_squirrel_data /path/to/file.csv
```
### Web Pages
  - **Homepage**: at '/',a homepage to describe the application with links to other pages
  - **Map**: at'/map',a map to plot 100 chosen sightings. https://leafletjs.com/ library was used for plotting
  - **All sightings**: at '/sightings/',a page to see unique ID and date of each squirrel sighting with links to view & update, add a sighting and other pages
  - **View & Update sighting**: at'/sightings/\<unique-squirrel-id\>',a form page to check and edit each sighting and save it to "All sightings", with links to other pages
  - **Add a sighting**: at'/sightings/add',a form page to create a sighting, and save it to "All sightings" ,with links to other pages
  - **Stats**: at'/sightings/stats',a page to describe the data of all the sightings,with links to other pages
  
## Group Name and Section
- Zizhen & Xiran, Section 1

## List of UNIs
- UNIs: [zh2439, xx2368]

## Link to the server
-	The project is not deployed

