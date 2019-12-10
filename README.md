## ZIP Code mapping for NYC using the 311 dataset

This repository documents a basic webapp for visualizing habitable ZIP codes in New York City based on user-selected criteria dependant on the range of complaints from 311 callers. 

The project utilizes the [*311 Service Requests from 2010 to Present*](https://nycopendata.socrata.com/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/) dataset hosted by [NYC Open Data](https://opendata.cityofnewyork.us/). This dataset logs 21M rows of complaints with 36 columns indicating complaint time, type, zip code, geographical location, responsible civic authority, whether the complaint was addressed, etc. 

The user picks 5 filters in order of importance for their housing search from a drop-down listing all 36 columns available in the data, and hits submit. The home page redirects to a choropleth map of NYC with the relevant ZIP codes highlighted. The map is generated using [```folium```](https://python-visualization.github.io/folium/), a visualization library based on ```leaflet.js```. 
