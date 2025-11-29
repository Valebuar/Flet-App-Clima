import requests
from config import settings

class WeatherService:
    def __init__(self, use_mock_data=False):
        self.api_key = settings.API_KEY
        self.base_url = settings.BASE_URL
        self.use_mock_data = use_mock_data
    
    def get_weather(self, city_name):
        # Si estamos usando datos mock, retornarlos directamente
        if self.use_mock_data:
            return self.get_mock_weather(city_name)
            
        try:
            params = {
                'q': city_name,
                'appid': self.api_key,
                'units': settings.UNITS,
                'lang': settings.LANGUAGE
            }
            
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                return {
                    'success': True,
                    'data': {
                        'city': data['name'],
                        'country': data['sys']['country'],
                        'temperature': round(data['main']['temp']),
                        'feels_like': round(data['main']['feels_like']),
                        'description': data['weather'][0]['description'].title(),
                        'humidity': data['main']['humidity'],
                        'pressure': data['main']['pressure'],
                        'wind_speed': data['wind']['speed'],
                        'icon': data['weather'][0]['icon']
                    }
                }
            else:
                return {
                    'success': False,
                    'error': data.get('message', 'Error desconocido')
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Error de conexión: {str(e)}'
            }
    
    def get_mock_weather(self, city_name):
        """Datos de prueba para desarrollo"""
        import random
        temperatures = [20, 22, 25, 18, 28, 30]
        descriptions = ["Soleado", "Parcialmente nublado", "Nublado", "Lluvioso", "Tormentoso"]
        
        return {
            'success': True,
            'data': {
                'city': city_name.title(),
                'country': 'AR',
                'temperature': random.choice(temperatures),
                'feels_like': random.choice(temperatures) + 2,
                'description': random.choice(descriptions),
                'humidity': random.randint(40, 90),
                'pressure': random.randint(1000, 1020),
                'wind_speed': round(random.uniform(1.0, 10.0), 1),
                'icon': '02d'
            }
        }