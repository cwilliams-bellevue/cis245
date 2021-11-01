#!/usr/bin/env python3

import requests
import math
import os

#weather report class
class WeatherReport:
 	
    #tuple for supported modes
    modes = ('ByName', 'ByZip')
    #initialize some vars
    key = None
    data = None

    #helper function to retreive or prompt for key
    @staticmethod
    def readAPIToken():
        try:
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
            print("Some unhandled error ocurred: %s " % (ex))
            return(None)
        return(resp)
		
    #call weather by city endpoint
    @staticmethod
    def getInfoByName(key, cname):
        try:
            resp = requests.get("https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" % (cname, key))
        except Exception as ex:
            print("Some unhandled error ocurred: %s " % (ex))
            return(None)
        return(resp)


    #format json results into output
    def printWeather(self):
        if self.data == None:
            raise ValueError("No weather data!")
            return None
        if self.data.status_code != 200:
            print("Results not found for location.")
            return None
        json = self.data.json()
        location = json['name']
        weather = json['weather'][0]
        current = weather['description']
        mn = json['main']
        temp = float(mn['temp'])
        fahrenheit = (temp - 273.15) * ( 9 / 5 ) + 32
        fahrenheit = math.floor(fahrenheit)
        print("doing output")
        print("Current weather in %s is %s with a temperature of %0.0f degrees Fahrenheit." % (location, current, fahrenheit))
        return True


    #initialize based on type
    def __init__(self, data, mode='ByZip'):
        self.info = None
        if mode not in self.modes:
            raise ValueError("Invalid mode passed to WeatherReport!")
        self.key = WeatherReport.readAPIToken()
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
