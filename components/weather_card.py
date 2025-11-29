import flet as ft
from config import settings
from utils.helpers import get_weather_icon, get_color

def create_weather_card():
    """Crea y retorna la tarjeta de información del clima"""
    # Contenedor principal
    weather_card = ft.Container(
        width=settings.CARD_WIDTH,
        padding=20,
        border_radius=settings.CARD_BORDER_RADIUS,
        bgcolor=get_color(settings.CARD_BG_COLOR),
        visible=False,
        animate=ft.Animation(settings.ANIMATION_DURATION, "easeOut")
    )
    
    # Elementos de la tarjeta
    city_name = ft.Text(size=24, weight=ft.FontWeight.BOLD)
    country = ft.Text(size=16, color=get_color("GREY_700"))
    temperature = ft.Text(size=48, weight=ft.FontWeight.BOLD)
    description = ft.Text(size=18, color=get_color("BLUE_700"))
    
    # Icono del clima
    weather_icon = ft.Container(
        width=80,
        height=80,
        alignment=ft.alignment.center
    )
    
    # Información adicional
    feels_like = ft.Text(size=14)
    humidity = ft.Text(size=14)
    pressure = ft.Text(size=14)
    wind_speed = ft.Text(size=14)
    
    # Diseño de la tarjeta
    weather_card.content = ft.Column([
        ft.Row([city_name, country], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            weather_icon,
            ft.Column([
                temperature,
                description
            ])
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        ft.Column([
            feels_like,
            humidity,
            pressure,
            wind_speed
        ], spacing=5)
    ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    return {
        'card': weather_card,
        'elements': {
            'city_name': city_name,
            'country': country,
            'temperature': temperature,
            'description': description,
            'weather_icon': weather_icon,
            'feels_like': feels_like,
            'humidity': humidity,
            'pressure': pressure,
            'wind_speed': wind_speed
        }
    }

def update_weather_card(weather_elements, data):
    """Actualiza la tarjeta del clima con nuevos datos"""
    from utils.helpers import get_color
    from config import settings
    
    weather_elements['city_name'].value = data['city']
    weather_elements['country'].value = data['country']
    weather_elements['temperature'].value = f"{data['temperature']}°C"
    weather_elements['description'].value = data['description']
    weather_elements['feels_like'].value = f"Sensación térmica: {data['feels_like']}°C"
    weather_elements['humidity'].value = f"Humedad: {data['humidity']}%"
    weather_elements['pressure'].value = f"Presión: {data['pressure']} hPa"
    weather_elements['wind_speed'].value = f"Viento: {data['wind_speed']} m/s"
    
    # Configurar icono
    icon_code = data['icon']
    weather_elements['weather_icon'].content = ft.Icon(
        name=get_weather_icon(icon_code),
        size=40,
        color=get_color(settings.ACCENT_COLOR)
    )