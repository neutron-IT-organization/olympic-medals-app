from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://api.olympics.kevle.xyz/medals"

def fetch_medals_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return data['results']
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

@app.route('/')
def index():
    medals_data = fetch_medals_data()
    return render_template('index.html', medals_data=medals_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

