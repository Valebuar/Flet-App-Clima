import flet as ft

def get_weather_icon(icon_code):
    """Mapea códigos de iconos de OpenWeatherMap a iconos de Material"""
    icon_map = {
        '01d': ft.Icons.WB_SUNNY,
        '01n': ft.Icons.NIGHTLIGHT_ROUND,
        '02d': ft.Icons.WB_CLOUDY,
        '02n': ft.Icons.CLOUD,
        '03d': ft.Icons.CLOUD,
        '03n': ft.Icons.CLOUD,
        '04d': ft.Icons.CLOUD_QUEUE,
        '04n': ft.Icons.CLOUD_QUEUE,
        '09d': ft.Icons.GRAIN,
        '09n': ft.Icons.GRAIN,
        '10d': ft.Icons.WATER_DROP,
        '10n': ft.Icons.WATER_DROP,
        '11d': ft.Icons.FLASH_ON,
        '11n': ft.Icons.FLASH_ON,
        '13d': ft.Icons.AC_UNIT,
        '13n': ft.Icons.AC_UNIT,
        '50d': ft.Icons.FOGGY,
        '50n': ft.Icons.FOGGY,
    }
    return icon_map.get(icon_code, ft.Icons.WB_SUNNY)

def get_color(color_name):
    """Obtiene color de ft.Colors por nombre"""
    return getattr(ft.Colors, color_name, ft.Colors.BLUE_900)