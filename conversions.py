def fahrenheitToCelsius(fahrenheitTemperature):
	celsius = (fahrenheitTemperature - 32.0) * (5.0/9.0)
	return celsius

def celsiusToFahrenheit(celsiusTemperature):
	fahrenheit = celsiusTemperature * (9.0 / 5.0) + 32
	return fahrenheit

def celsiusToKelvin(kelvinTemperature):
	kelvin = (kelvinTemperature + 273.15)
	return kelvin

def showMenu():
	print "A: Convert celsius to fahrenheit"
	print "B: Convert fahrenheit to celsius"
	print "C: Convert celsius to kelvin"
	print "X: Exit"

showMenu()
option = raw_input("Option: ")


while option != "X":
	if option == "A" or option == "B" or option == "C":
		value = float(input("Number to convert: "))
		if option == "A":
			print(celsiusToFahrenheit(value))
		elif option == "B":
			print(fahrenheitToCelsius(value))
		elif option == "C":
			print(celsiusToKelvin(value))
	else:
		print "Please enter a valid option."
	
	showMenu()
	option = raw_input("Option: ")