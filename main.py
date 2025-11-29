import flet as ft
from config import settings
from services.weather_service import WeatherService
from components.search_bar import create_search_bar
from components.weather_card import create_weather_card, update_weather_card
from utils.helpers import get_color

def main(page: ft.Page):
    # Configuración de la página
    page.title = settings.APP_TITLE
    page.theme_mode = getattr(ft.ThemeMode, settings.THEME_MODE.upper())
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Determinar si usar datos reales o mock
    use_mock_data = settings.API_KEY == "ffc8657b0f8efd14efdeac03d2825879"
    
    # Servicios
    weather_service = WeatherService(use_mock_data=use_mock_data)
    
    # Componentes de la UI
    title = ft.Text(
        settings.APP_TITLE,
        size=28,
        weight=ft.FontWeight.BOLD,
        color=get_color(settings.PRIMARY_COLOR)
    )
    
    # Barra de búsqueda
    search_components = create_search_bar(lambda _: search_weather())
    search_container = search_components['container']
    city_input = search_components['input']
    
    # Tarjeta del clima
    weather_components = create_weather_card()
    weather_card = weather_components['card']
    weather_elements = weather_components['elements']
    
    # Indicador de carga
    progress_ring = ft.ProgressRing(visible=False)
    
    # Mensaje de error
    error_message = ft.Text(
        color=get_color("RED"),
        size=16,
        text_align=ft.TextAlign.CENTER,
        visible=False
    )
    
    # Mensaje informativo si estamos usando mock data
    info_message = ft.Text(
        color=get_color("ORANGE_700"),
        size=12,
        text_align=ft.TextAlign.CENTER,
    )
    
    def search_weather():
        city = city_input.value.strip()
        if not city:
            show_error("Por favor ingresa una ciudad")
            return
        
        # Mostrar carga
        progress_ring.visible = True
        error_message.visible = False
        weather_card.visible = False
        page.update()
        
        # Obtener datos del clima
        result = weather_service.get_weather(city)
        
        # Ocultar carga
        progress_ring.visible = False
        
        if result['success']:
            update_weather_card(weather_elements, result['data'])
            error_message.visible = False
            weather_card.visible = True
        else:
            show_error(f"No se pudo obtener el clima: {result['error']}")
        
        page.update()
    
    def show_error(message):
        error_message.value = message
        error_message.visible = True
        weather_card.visible = False
    
    # Diseño principal
    page.add(
        ft.Column([
            title,
            ft.Container(height=10), # Pequeño espacio bajo el título
            info_message,
            ft.Container(content=search_container, width=settings.CARD_WIDTH),
            progress_ring,
            error_message,
            weather_card
        ], 
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.ADAPTIVE
        )
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)