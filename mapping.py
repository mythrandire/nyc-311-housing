import os
import folium
save_as = 'NYC_zipMap.html'
geoJson_path = 'NYCgeo.json'

center_coord = [40.701412, -74.017116]

m = folium.Map(center_coord, zoom_start=11)

folium.GeoJson(geoJson_path, style_function=lambda feature: {
        'fillColor': '#ffff00',
        'color': 'black',
        'weight': 2,
        'dashArray': '.5,5'
    }).add_to(m)

m.save(os.path.join(save_as))