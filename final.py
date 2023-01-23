from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import requests
from PIL import ImageTk, Image

HEIGHT = 500
WIDTH = 600
my_font = 'Verdana' , 10,
main_color = '#EDEBF9'
highlight_color = '#DDDAFD'

bg_dict = {
	'sunny' : 'img/day.jpg',
	'rainy' : 'img/rain.png',
	'cloudy' : 'img/sky.png',
	'night' : 'img/night.jpg',
}

def test_function(entry):
	print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
	try:
		name = weather['location']['name']
		temp = weather['current']['temperature']
		feels = weather['current']['feelslike']
		humid = weather['current']['humidity']
		description = weather['current']['weather_descriptions']

		final_str = u'Current weather in %s is %s. \n The temperature in is %d℃. \n Feels like %d℃. \n Humidity is %d '% (name, description, temp, feels, humid)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_weather(city):
	weather_key = 'e93d65e58ffc3cb71c4aed0632fac109'
	url = 'http://api.weatherstack.com/current'
	params = {
        'access_key': weather_key, 
        'query': city, 
        'units': 'm'
     }
	api_response = requests.get(url, params=params)
	api_weather = api_response.json()

	label['text'] = format_response(api_weather)

root = tk.Tk()

style = ttk.Style(root)
current_theme = style.theme_use('clam')


title = root.title('Weather')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,)
canvas.pack()

background_img = tk.PhotoImage(file= r'img/sky.png')
background_label = tk.Label(root, image=background_img)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg=main_color, bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

#intro = tk.Label(frame, text="Enter a city: ")
#intro.place(relwidth=0.65, relheight=1)

city_entry = tk.Entry(frame, borderwidth=10, relief=FLAT)
city_entry.focus()
city_entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, bd=0, text="Get Weather", bg =highlight_color, font=(my_font), command=lambda: get_weather(city_entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg=highlight_color, bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg=main_color)
label.place(relwidth=1, relheight=1)
root.mainloop()