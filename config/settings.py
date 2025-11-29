import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Configuración de la API
API_KEY = os.getenv("OPENWEATHER_API_KEY", "ffc8657b0f8efd14efdeac03d2825879")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
UNITS = os.getenv("UNITS", "metric")
LANGUAGE = os.getenv("LANGUAGE", "es")

# Configuración de la aplicación
APP_TITLE = os.getenv("APP_TITLE", "App del Clima")
THEME_MODE = os.getenv("THEME_MODE", "light")

# Configuración de la UI
CARD_WIDTH = 350
CARD_BORDER_RADIUS = 15
ANIMATION_DURATION = 600

# Configuración de colores
PRIMARY_COLOR = "BLUE_900"
SECONDARY_COLOR = "BLUE_600"
ACCENT_COLOR = "ORANGE_500"
CARD_BG_COLOR = "BLUE_50"