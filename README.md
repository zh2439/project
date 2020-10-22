# Squirrel-Tracker
Squirrel Tracker is a web application developed with Django framework which tracks the squirrels in Central Park and allow users to view, update and add squirrel sightings. 

# Description
  - **Import/export data**: use management commands to import data from "rows.csv" and export in csv format
  - **Homepage**: at '/',a homepage to describe the application with links to other pages
  - **Map**: at'/map',a map to plot 100 chosen sightings. https://leafletjs.com/ library was used for plotting
  - **All Sightings**: at '/sightings/',a page to see unique ID and Date of each squirrel sighting with links to view & update, add a sighting and other pages
  - **View & Update sighting**: at'/sightings/\<unique-squirrel-id\>',a form page to check and edit each sighting and save to the "All Sightings", with links to other pages
  - **Add a sighting**: at'/sightings/add',a form page to create a sighting, and save to the "All Sightings" ,with links to other pages
  - **Stats**: at'/sightings/stats',a page to describe the data of all the sightings,with links to other pages
  
# Group Name and Section
Zizhen & Xiran, Section 1

# List of UNIs
UNIs: [zh2439, xx2368]

# Link to the server
-	'http://<your_ip_address>/' to the homepage
