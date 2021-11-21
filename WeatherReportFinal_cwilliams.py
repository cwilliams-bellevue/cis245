#!/usr/bin/env python3
# cis245 final projects
# Christopher Williams
# chrwilliams2@my365.bellevue.edu
# final version

#use requests, math, and os modules
import requests
import math
import os

#global for API key during session
glblOWMAPIKey = None

#weather report class
class WeatherReport:
 	
    #tuple for supported modes of querying api
    modes = ('ByName', 'ByZip')
    #initialize some vars
    key = None
    data = None

    #helper function to retreive or prompt for key
    #key should be stored in $HOME/.openweathermap.key
    #if not, we will prompt for key
    #change also made to work on Windows as well as Linux
    #detecting OS and using USERPROFILE instead of HOME
    @staticmethod
    def readAPIToken():
        try:
            if os.name == "nt":
                 path = "%s\.openweathermap.key" % (os.environ['USERPROFILE'])
            else:
                 path = "%s/.openweathermap.key" % (os.environ['HOME'])
            fi = open(path,'r')
            line = fi.readline()
            fi.close()
            line = line.strip()
        except:
            print("Cannot open secret key file ~/.openweathermap.key")
            line = input("Since key wasn't found please enter an API key: ")
        finally:
            key = line
        return(key)

    #call weather by zip code endpoint
    @staticmethod
    def getInfoByZip(key, zipc):
        try:
            resp = requests.get("https://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=%s" % (zipc, key))
        except Exception as ex:
            print("While connecting to OpenWeatherMap, some unhandled error ocurred: %s " % (ex))
            return(None)
        return(resp)
		
    #call weather by city endpoint
    @staticmethod
    def getInfoByName(key, cname):
        try:
            resp = requests.get("https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (cname, key))
        except Exception as ex:
            print("While connecting to OpenWeatherMap, some unhandled error ocurred: %s " % (ex))
            return(None)
        return(resp)


    #format json results into output
    def printWeather(self):
        global glblOWMAPIKey
        if self.data == None:
            raise ValueError("No weather data was returned by OpenWeatherMap!")
            return None
        #if we get a 401 the key is probably bad, blank out any key in memory and ask again
        if self.data.status_code == 401:
            print("OpenWeatherMap authentication failed. Key may be invalid.")
            glblOWMAPIKey = None
            return None
        #otherwise we probably have no data for that location
        if self.data.status_code != 200:
            print("OpenWeatherMap results were not found for specified location.")
            return None
        json = self.data.json()
        location = json['name']
        weather = json['weather'][0]
        current = weather['description']
        mn = json['main']
        temp = float(mn['temp'])
        fahrenheit = (temp - 273.15) * ( 9 / 5 ) + 32
        fahrenheit = math.floor(fahrenheit)
        print("\nYour Weather Report...")
        print("Current weather in %s is %s with a temperature of %0.0f degrees Fahrenheit.\n" % (location, current, fahrenheit))
        return True


    #initialize based on type
    def __init__(self, data, mode='ByZip'):
        global glblOWMAPIKey
        self.info = None
        if mode not in self.modes:
            raise ValueError("Invalid mode passed to WeatherReport!")
        #if key isn't already stored in global var, we'll read it or prompt for it
        if glblOWMAPIKey == None:
            self.key = WeatherReport.readAPIToken()
            glblOWMAPIKey = self.key
        else:
            self.key = glblOWMAPIKey
        if mode == 'ByZip':
             self.data = WeatherReport.getInfoByZip(self.key,data)
        if mode == 'ByName':
             self.data = WeatherReport.getInfoByName(self.key,data)
        if self.data == None:
             print("Weather API Connection Failed.")
        else:
             print("Weather API Connection Succeeded.")


# main function, entry point for app
def main():
    #loop for weather reports until done
    while True:
        #choose by city or by zip code
        inch = None
        while inch != "1" and inch != "2":
            inch = input("Do you want to enter a city name or zip code for your weather report?\n1...City Name\n2...Zip Code\nEnter 1 or 2: ")

        #invoke object with city name
        if inch == "1":
            city = input("Enter city name: ")
            try:
                wrep = WeatherReport(city,mode='ByName')
                wrep.printWeather()
            except Exception as exc:
                print("Error ocurred calling Weather API: %s" % (exc))


        #invoke object with zip code
        if inch == "2":
            zip = input("Enter zip code: ")
            try:
                wrep = WeatherReport(zip)
                wrep.printWeather()
            except Exception as exc:
                print("Error ocurred calling Weather API: %s " % (exc))

        again = None 

        #ask if we run another
        while again != "y" and again != "n":
            again = input("Do you want another weather report?\ny...yes\nn...no\nEnter y or n: ")
        if again == "n":
            print("Bye.")
            exit(0)

  
  
# make sure main is called if __name__ passed to interpreter is __main__
if __name__=="__main__":
    main()
