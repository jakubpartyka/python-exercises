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

fg.add_child(folium.GeoJson(data=open('data/world.json', 'r', encoding='utf-8-sig').read()))

map.add_child(fg)

map.save('Map1.html')

























=============================
import random

from PIL import Image, ImageColor


def color(x_cord, y_cord, c=0):
    if c == 0:
        col = 'white'
    else:
        col = 'black'
    im.putpixel((x_cord, y_cord), ImageColor.getcolor(col, '1'))  # or whatever color you wish


# width and height of output image
w = 24000
h = 24000
total_pixels = w * h

log = True  # if true print a line every 1%

im = Image.new('1', (w, h))  # create the Image of size 1 pixel

counter = 0  # count how many pixels were drawn
percent_completed = 0   # total progress in percent

for x in range(w):
    for y in range(h):
        counter = counter + 1

        # log progress
        if log and counter % (total_pixels/100) == 0:
            percent_completed = percent_completed + 1
            print(percent_completed, "% done")

        # decide on pixel color
        k = random.randint(0, 1)
        color(x, y, k)

im.save('24000.png')  # or any image format
