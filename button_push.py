import RPi.GPIO as GPIO
import time
import requests

def post():
	URL = "http://maps.googleapis.com/maps/api/geocode/json"
	location = "Elmhurst, IL"
	PARAMS = {'address':location}
	r = requests.get(url = URL, params = PARAMS)
	data = r.json()
	latitude = data['results'][0]['geometry']['location']['lat']
	longitude = data['results'][0]['geometry']['location']['lng']
	formatted_address = data['results'][0]['formatted_address']
	print("Latitude: " + str(latitude))
	print("Longitude: " + str(longitude))
	print("Address: " + str(formatted_address))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

held = False
while True:
	input_state = GPIO.input(10)
	if(input_state == True and held == False):
		print("Button pressed")
		post()
		time.sleep(0.5)
		held = True
	held = input_state

GPIO.cleanup()
