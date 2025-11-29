import flet as ft
from config import settings
from utils.helpers import get_color

def create_search_bar(on_search_click):
    """Crea y retorna la barra de búsqueda"""
    city_input = ft.TextField(
        label="Ingresa una ciudad",
        hint_text="Ej: Madrid, Buenos Aires, México",
        text_size=14,
        border_color=get_color("BLUE_400"),
        focused_border_color=get_color("BLUE_700"),
        expand=True
    )
    
    search_button = ft.ElevatedButton(
        text="Buscar Clima",
        icon=ft.Icons.SEARCH,
        on_click=on_search_click,
        style=ft.ButtonStyle(
            color=get_color("WHITE"),
            bgcolor=get_color(settings.SECONDARY_COLOR),
            padding=10
        )
    )
    
    return {
        'input': city_input,
        'button': search_button,
        'container': ft.Row([
            city_input,
            search_button
        ], alignment=ft.MainAxisAlignment.CENTER)
    }