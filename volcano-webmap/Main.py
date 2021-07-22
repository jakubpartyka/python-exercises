import folium
import pandas

fg = folium.FeatureGroup(name='My map')


def create_info(row):
    return 'Name: {name}\nLocation: {loc}\nType: {type}\nElevation: {elev}\nStatus:'\
           ' {status}\nNo.: {number}\ncoordinates: {lat},{lon}'.format(name=row['NAME'], loc=row['LOCATION'],
                                             type=row['TYPE'], elev=row['ELEV'],
                                             status=row['STATUS'], number=row['NUMBER'],
                                             lat=row['LAT'], lon=row['LON'])


df = pandas.read_csv('data/Volcanoes.txt')
print(df.iloc[:2])

map = folium.Map(location=[38, -110], zoom_start=5, tiles="Stamen Terrain")

for index, row in df.iterrows():
    lat = row['LAT']
    lon = row['LON']
    info = create_info(row)
    fg.add_child(folium.Marker(location=[lat, lon],
                               popup=info,
                               icon=folium.Icon(color='red')))

map.add_child(fg)

map.save('Map1.html')
