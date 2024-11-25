class WeatherDataFetcher:
    """Handles fetching weather data for a given city."""
    
    def __init__(self):
        # Simulated weather data
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
    
    def fetch(self, city):
        """Fetches weather data for the specified city."""
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, {})


class DataParser:
    """Handles parsing of weather data."""
    
    @staticmethod
    def parse(data):
        """Parses the provided weather data."""
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"


class UserInterface:
    """Handles user interaction and main application logic."""
    
    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = DataParser()
    
    def display_weather(self, city):
        """Displays the basic weather forecast for a city."""
        data = self.fetcher.fetch(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse(data)
            print(weather_report)
    
    def get_detailed_forecast(self, city):
        """Provides a detailed weather forecast for a city."""
        data = self.fetcher.fetch(city)
        return self.parser.parse(data)
    
    def run(self):
        """Runs the main application loop."""
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                print("Goodbye!")
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = None
                self.display_weather(city)
            if forecast:
                print(forecast)


if __name__ == "__main__":
    app = UserInterface()
    app.run()
