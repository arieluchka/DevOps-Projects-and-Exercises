# Python Exercise: Weather Data with OpenWeatherMap API

This exercise introduces you to working with APIs (Application Programming Interfaces) using Python. You will use the OpenWeatherMap API to fetch real-time weather data for different cities. This task will help you understand how to send API requests, handle responses, and process data in Python.

## Prerequisites

- Sign up for an API key at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to authenticate your API requests.
- If you've never worked with JSON, go over this [video](https://www.youtube.com/watch?v=-51jxlQaxyA) to get the basics of it.
- Install the `requests` library using pip if you haven't yet:
  
    `pip install requests`

## What is an API?

An API is a set of rules that allows one piece of software application to interact with another. It facilitates the communication between two software applications using a set of definitions and protocols.

Introduction to API videos:

[Video 1](https://www.youtube.com/watch?v=s7wmiS2mSXY)

[Video 2](https://www.youtube.com/watch?v=6STSHbdXQWI)

## Python and APIs

In Python, the `requests` library is commonly used to send all kinds of HTTP requests. It is an easy-to-use library that allows Python programs to interact with web services.

## External Resources

- [Python `requests` library documentation](https://docs.python-requests.org/en/master/)
- [OpenWeatherMap API documentation](https://openweathermap.org/api)
  - [You would use the API by city name](https://openweathermap.org/current#name:~:text=for%20this%20functionality.-,Built%2Din%20API%20request%20by%20city%20name,-You%20can%20call)
- [Real Python Tutorial on APIs](https://realpython.com/python-api/)

## Getting Started

Before you begin, you need to sign up for an API key at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to authenticate your API requests. (no need to input credit card info)

After that, go to [API keys](https://home.openweathermap.org/api_keys) and copy the Default key. You will use this key to send API requests.

## Exercise Objectives

Complete the following mini-exercises to enhance your understanding of working with APIs in Python:

### Exercise 1: Fetch Weather by City

**Objective:** Create a function that returns the current weather data for a specified city.

**Task:**
- Write a function named `get_weather_by_city` that takes a city name as an argument and returns the weather data as a JSON.
- This [article](https://realpython.com/python-api/#calling-your-first-api-using-python:~:text=Enough%20talking%E2%80%94it%E2%80%99s%20time%20to%20make%20your%20first%20API%20call!%20For%20the%20first%20example%2C%20you%E2%80%99ll%20be%20calling%20a%20popular%20API%20for%20generating%20random%20user%20data.) will help you make your first API calls.
- [Here](https://openweathermap.org/current#name:~:text=for%20this%20functionality.-,Built%2Din%20API%20request%20by%20city%20name,-You%20can%20call) you can read about API by city

### Exercise 2: Extract Temperature

**Objective:** Extract the temperature from the weather data.

**Task:**
- Develop a function named `get_temperature` that accepts weather data JSON and returns the current temperature in Celsius.

### Exercise 3: Determine Weather Condition

**Objective:** Identify the general weather condition (like clear, clouds, rain).

**Task:**
- Create a function called `get_weather_condition` that takes the weather data JSON and returns the main weather condition.

### Exercise 4: Convert Temperature

**Objective:** Convert the temperature from Kelvin to Celsius and Fahrenheit.

**Task:**
- Implement a function named `convert_temperature` that takes a temperature in Kelvin and returns it in both Celsius and Fahrenheit.

### Exercise 5: Wind Speed and Direction

**Objective:** Retrieve and format wind speed and direction.

**Task:**
- Write a function named `get_wind` that extracts and returns wind speed in km/h and wind direction in degrees from the weather data JSON.

---

Try to search the temprature and weather of different cities you know like `Tel aviv`, `Rehovot` and `Eilat`, and see what result are you getting!

---

## Solutions

<details>
<summary> Exercise 1 answer </summary>

```python
def get_weather_by_city(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    return response.json()
```

</details>

<details>
<summary> Exercise 2 answer </summary>

```python
def get_temperature(weather_data):
    kelvin = weather_data['main']['temp']
    celsius = kelvin - 273.15
    return celsius
```

</details>

<details>
<summary> Exercise 3 answer </summary>

```python
def get_weather_condition(weather_data):
    return weather_data['weather'][0]['main']
```

</details>

<details>
<summary> Exercise 4 answer </summary>

```python
def convert_temperature(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * 9/5 + 32
    return celsius, fahrenheit
```

</details>

<details>
<summary> Exercise 5 answer </summary>

```python
def get_wind(weather_data):
    speed_kmh = weather_data['wind']['speed'] * 3.6
    direction = weather_data['wind']['deg']
    return speed_kmh, direction
```
</details>

<details>
<summary> Full possible answer with Usage </summary>

```python
import requests

def get_weather_by_city(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    return response.json()

def get_temperature(weather_data):
    kelvin = weather_data['main']['temp']
    celsius = kelvin - 273.15
    return celsius

def get_weather_condition(weather_data):
    return weather_data['weather'][0]['main']

def convert_temperature(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * 9/5 + 32
    return celsius, fahrenheit

def get_wind(weather_data):
    speed_kmh = weather_data['wind']['speed'] * 3.6
    direction = weather_data['wind']['deg']
    return speed_kmh, direction


api_key = "your_api_key_here"
city_weather = get_weather_by_city("Berlin", api_key)
print("Temperature:", get_temperature(city_weather))
print("Weather Condition:", get_weather_condition(city_weather))
print("Wind:", get_wind(city_weather))
```

</details>

