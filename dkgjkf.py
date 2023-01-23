from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import requests
from PIL import ImageTk, Image


def test_function(entry):
	print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
	try:
		name = weather['location']['name']
		temp = weather['current']['temperature']

		final_str = u'Current temperature in %s is %d℃' % (name, temp)
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

HEIGHT = 0
WIDTH = 0
my_font = 'Verdana' , 10,
main_color = '#E5E3F5'
highlight_color = '#E0BEF4'
paddings = {'padx': 5, 'pady': 5, 'ipadx': 100, 'ipady': 5}

style = ttk.Style(root)
current_theme = style.theme_use('clam')

title = root.title('Weather')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,)
canvas.grid(column=4, row=5)

background_img = tk.PhotoImage(file= r'img\2102.i518.009_sky_cloud_evening_illustration.png')
background_label = tk.Label(root, image=background_img)
background_label.grid(column=1, row=1, columnspan=4, rowspan=5)

frame = tk.Frame(root, bg=highlight_color, bd=5)
frame.grid(column=2, row=2, columnspan=2)

#intro = tk.Label(frame, text="Enter a city: ")
#intro.grid(column=0.65, row=1)

city_entry = tk.Entry(frame)
city_entry.focus()
city_entry.grid(column=2, row=2, **paddings)

button = tk.Button(frame, text="Get Weather", bg =main_color, font=(my_font), command=lambda: get_weather(city_entry.get()))
button.grid(column=3, row=2)

lower_frame = tk.Frame(root, bg='blue', bd=10)
lower_frame.grid(column=2, row=2, columnspan=2, rowspan=2, sticky=EW)

label = tk.Label(lower_frame, bg=main_color)
label.grid(column=2, row=2, columnspan=2, rowspan=2, **paddings, sticky=EW)
root.mainloop()