# -----------------------
# Demonstrate how to get information by API
# A way to get weather information by the location of the user
#
# Blezyl Santos
# version 4.16.2020
# -----------------------
import requests

#
# Asks user for city and country code. Inputs data into URL and calls
# printData to print weather information
#
def byCity():
    city = input("Enter City: ")
    country = input("Enter the country code: (ex. us, uk,...)")
    url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid=a132363b5c1d6175b68237a11d631b7c&units=metric'.format(
        city, country)
    printData(url)


#
# Inputs data from ip address into URL and calls printData to print weather information
#
def byGeo():
    webIp = requests.get('https://ipinfo.io/')
    webIpdata = webIp.json()
    location = webIpdata['loc'].split(',')
    lat = location[0]
    lon = location[1]

    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=a132363b5c1d6175b68237a11d631b7c&units=metric'.format(
        lat, lon)
    printData(url)


#
# Asks user for Zipcode and country code. Inputs data into URL and calls
# printData to print weather information
#
def byZip():
    zipcode = input('Enter Zipcode: ')
    country = input("Enter the country code: (ex. us, uk,...): ")
    url = 'http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid=a132363b5c1d6175b68237a11d631b7c&units=metric'.format(
        zipcode, country)
    printData(url)


#
#
# :param url: url to get the information on weather
#
def printData(url):
    data = requests.get(url).json()
    # declares variables of the information from the data
    loc = data['name'] + ", " + data['sys']['country']
    temp = data['main']['temp']
    windspeed = data['wind']['speed']
    desc = data['weather'][0]['description']
    # prints the variables
    print()
    print('Location: {}'.format(loc))
    print("Tempreture: {} celcius".format(temp))
    print("WindSpeed: {}m/s".format(windspeed))
    print("Description: {}".format(desc))
    print()

#
# Main function. Requests user how they would want to obtain weather
# information from 3 options. Calls the corresponding function and repeats
# until user's choice is 4 (quit).
#
def main():
    print("Welcome to the Weather Chanel")
    print("Objective:")
    print(" Introduction to working with API on python")
    choice = None
    while choice != 4:
        print()
        print('Select method of finding Location')
        print('1. By City')
        print('2. By Geographic Coordinates')
        print('3. By Zipcode')
        print('4. Quit')
        choice = input("Enter choice: ")
        choice = int(choice)
        while (choice < 1) or (choice > 4):
            print('ERROR, Incorrect input')
            choice = input("Enter choice: ")
            choice = int(choice)

        if choice == 1:
            byCity()
        elif choice == 2:
            byGeo()
        elif choice == 3:
            byZip()


if __name__ == '__main__':
    main()
