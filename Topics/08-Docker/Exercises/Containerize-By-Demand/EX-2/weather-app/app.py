from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = {}
    if request.method == 'POST':
        city = request.form['city']
        api_key = '90f53b85ef468f04c927cd4f2d01c4f7'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            weather = {
                'city': city,
                'temperature': round(data['main']['temp'] - 273.15, 2),
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
