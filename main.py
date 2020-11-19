from tkinter import *

import requests

root = Tk()
root.geometry('400x400')
root.config(bg="grey")
def test_function(entry):
	print("This is the entry:", entry)


def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		wind = weather['wind']['speed']
		humidity = weather['main']['humidity']
		clouds = weather['clouds']['all']
		if show_weather:
			final_str = 'Place: %s \nWeather: %s \nTemperature: %s \nWind Speed: %s \nHumidity: %s \nCloud Cover %s'% (name, desc, temp, wind, humidity, clouds)


	except:
		final_str = 'There was a problem'

	return final_str


def get_weatherM(city):
	weather_key = '181489a8df6dc65ef7036a5a8dfb60e5'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	parameters = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
	response = requests.get(url, params=parameters)
	weather = response.json()

	label['text'] = format_response(weather)

frame =Frame(root,bg="grey", bd=25)
frame.pack(side=TOP)

entrybox = Entry(frame)
entrybox.pack(side=TOP)

show_weather = Button(frame,text="Weather",command=lambda: get_weatherM(entrybox.get()))
show_weather.pack(side=TOP)

lower_frame = Frame(root, bg='Grey', bd=10)
lower_frame.pack(side=BOTTOM)

label = Label(lower_frame)
label.pack(side=TOP)

root.mainloop()