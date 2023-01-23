import json
from tkinter import *
from tkinter import ttk
import requests

root = Tk()

#set theme
s = ttk.Style()
s.theme_use('clam')
#Tkinter widgets
title = root.title('Weather')
root.minsize(600, 400) # width, height
root.configure(background= '#80c1ff')
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Enter a city: ").grid(column=0, row=0)
city_entry = ttk.Entry(frm).grid(column=0, row=1)

#backend

params = {
    'access_key': 'e93d65e58ffc3cb71c4aed0632fac109',
    'query': city_entry or 'drachten',
    'units': 'm',
}

def get_weather(query):
    params = {
        'access_key': 'e93d65e58ffc3cb71c4aed0632fac109',
        'query': query or 'drachten',
        'units': 'm',
    }

api_result = requests.get('http://api.weatherstack.com/current', params)
api_response = api_result.json()

print(api_result.status_code)
print(api_response)
print(u'Current temperature in %s is %d℃' % (api_response['location']['name'], api_response['current']['temperature']))

with open("params.json", "w") as f:
    json.dump(params, f)

with open("api_response.json", "w") as f:
    json.dump(api_response, f)

#buttons
ttk.Button(frm, text='Get Weather', command= lambda: get_weather(city_entry)).grid(column=1, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)

#close window loop
root.mainloop()

