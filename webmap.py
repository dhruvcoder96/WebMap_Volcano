import folium
import pandas
df1 = pandas.read_csv("Volcanoes-USA.txt")
map1= folium.Map(location=[48.7767982,-121.8109970],zoom_start=5,tiles="Stamen Terrain")
for lati,longi,name,elev,type1 in zip(df1['LAT'],df1['LON'],df1['NAME'],df1['ELEV'],df1['TYPE']):
		if elev>=0 and elev<=1500:
			c = 'green'
			markicon='glyphicon glyphicon-ok-sign'
		elif elev>1500 and elev<=2500:
			c= 'orange'
			markicon='glyphicon glyphicon-remove-sign'
		else:
			c='red'
			markicon='glyphicon glyphicon-warning-sign'
			str1= name+"\n"+type1;
		map1.add_child(folium.Marker(location=[lati,longi],popup=str1,icon=folium.Icon(color=c)))
map1.save("test.html")
