from time import sleep

import flet
from flet import Page, Text, colors, WindowDragArea, Container, IconButton, icons, Column, Row, FloatingActionButton, \
    FilledButton, TextField, ButtonStyle, ElevatedButton, Stack

nombreApp = "Binary Tree"

def main(page: Page):
    page.title = nombreApp
    page.theme_mode = "dark"
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    Inicio = [
        WindowDragArea(
            Container(
                Text(nombreApp, text_align="center", style="titleMedium", color=colors.BLUE_300),
                bgcolor="#FFEA9E",
                padding=10,
                border_radius=5),
            expand=True),
        IconButton(
            icons.CLOSE,
            on_click=lambda _: page.window_close())
    ]
    row = Row(spacing=0,controls=Inicio)
    page.add(
        row,
        Container(
            width=page.width,
            height=page.height,
            bgcolor=colors.WHITE,
            expand=True,
            border_radius=5,
            padding=10
        ),
        Row(spacing=20,controls=[
            ElevatedButton(
                text="Agregar Nodo",
                icon="add",
                style=ButtonStyle(bgcolor="#2F3894",color="#f5fafe")),
            ElevatedButton(
                text="Eliminar Nodo",
                icon="remove",
                disabled=True),
            TextField(label="Valor del Nodo",
                      keyboard_type="number",
                      filled=True,
                      border="underline",
                      border_color=colors.BLUE_300)]
            )
    )

flet.app(target=main)