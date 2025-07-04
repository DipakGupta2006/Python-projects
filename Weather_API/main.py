import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            condition = data["current_condition"][0]
            temp = condition["temp_C"]
            wind = condition["windspeedKmph"]
            desc = condition["weatherDesc"][0]["value"]

            print(f"\n🌤️ Weather in {city.title()}")
            print(f"📝 Condition: {desc}")
            print(f"🌡️ Temperature: {temp}°C")
            print(f"💨 Wind Speed: {wind} km/h\n")
        else:
            print(f"❌ Error: Received status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ An error occurred: {e}")

while True:
    choice = input("🔁 Enter a city name (or type 1 to quit): ").strip().lower()
    if choice == "1":
        print("👋 Thanks for using the Weather API!")
        break
    else:
        get_weather(choice)
