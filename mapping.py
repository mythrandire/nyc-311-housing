from sodapy import Socrata

client = Socrata("data.cityofnewyork.us", "iBBb7XdJQQL5zLxWTKQyP8fVN",
                 username="plm2130@columbia.edu", password="hHfa29h7pWmyR6g7e7")

LIMIT = 50000
client.timeout = 500
results = client.get("erm2-nwe9", limit=LIMIT)
raw_311_df = pd.DataFrame.from_records(results)
zip_311_df = raw_311_df.filter(items=['created_date', 'complaint_type', 'incident_zip', 'status'])
no_nan_df = zip_311_df.dropna()
no_nan_df.reset_index(drop=True, inplace=True)
no_nan_df.head(LIMIT)

import os
import folium
import pandas as pd
import cgi

form = cgi.FieldStorage()
searchterm =  form.getvalue('searchbox')

testing_for = 'Street Condition'

save_as = 'NYC_zipMap.html'
geoJson_path = 'NYCgeo.json'
#data_path = '~/Downloads/erm2-nwe9.csv'

geoJson = pd.read_json(geoJson_path)
data = no_nan_df
#data = pd.read_csv(data_path)

#geoJson['features'][1]['properties']['postalCode']  
#df.loc[df['column_name'] == some_value]
# appending-- df = df.append({'User_ID': 23, 'UserName': 'Riti', 'Action': 'Login'}, ignore_index=True)

number_of_zipCodes = len(geoJson['features'])
zips = {}
# make a list of the zip codes in the data and see if there are repeats
for region in range(number_of_zipCodes):
    zipcode = geoJson['features'][region]['properties']['postalCode']
    try:
        #works if there is already this zip in the dict
        zips[zipcode] = zips[zipcode] + 1
    except:
        #works if there isn't this zip in the dict yet
        zips[zipcode] = 1
    pass

df = pd.DataFrame(columns=['ZipCode', testing_for])

for call in range(len(data)):
    zipcode = int(data['incident_zip'][call])
    incident = data['complaint_type'][call]
    
    if zipcode > 0: # This is only true for data with a zipcode
        zipcode = str(zipcode)
        if incident == testing_for:
            try: 
                df.at[df.loc[df["ZipCode"]==zipcode].index[0], testing_for] = df.at[df.loc[df["ZipCode"]==zipcode].index[0], testing_for] + 1
            except:
                df = df.append({'ZipCode': zipcode, testing_for: 1}, ignore_index=True)
                #Zip code exists
            pass
        pass
    pass

center_coord = [40.701412, -74.017116]

m = folium.Map(center_coord, zoom_start=11)

#folium.GeoJson(geoJson_path, style_function=lambda feature: {
#        'fillColor': '#ffff00',
#        'color': 'black',
#        'weight': 2,
#        'dashArray': '.5,5'
#    }).add_to(m)

choropleth = folium.Choropleth(
    geo_data=geoJson_path,
    name='choropleth',
    data=df,
    columns=["ZipCode", testing_for],
    key_on= 'feature.properties.postalCode',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name=testing_for
).add_to(m)

folium.LayerControl().add_to(m)

m.save(os.path.join(save_as))