from time import sleep

import AvlAdapter
import flet
from flet import Page, Text, colors, WindowDragArea, Container, IconButton, icons, Column, Row, FloatingActionButton, \
    FilledButton, TextField, ButtonStyle, ElevatedButton, Stack, theme, padding, border_radius, GridView

nombreApp = "Binary Tree 🌲"
tree = AvlAdapter.AvlAdapter()


def main(page: Page):
    page.title = nombreApp
    page.bgcolor = "#2E2A52"
    page.padding = padding.only(top=0,bottom=10)
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.window_full_screen = False
    page.window_resizable = False

    def agregarEvent(e):
        tree.insertar(int(textField.value))
        textField.value = ''
        recorridos.controls[0].value = f"Recorrido Inorden: {tree.inorden()}"
        recorridos.controls[1].value = f"Recorrido Preorden: {tree.preorden()}"
        recorridos.controls[2].value = f"Recorrido Postorden: {tree.postorden()}"
        page.update()


    Inicio = [
        Text(nombreApp,
             text_align="center",
             style="titleLarge",
             expand=True),
        IconButton(
            icons.CLOSE,
            on_click=lambda _: page.window_close())
    ]
    textField = TextField(label="Valor del Nodo",
                          keyboard_type="number",
                          filled=True,
                          border="underline",
                          border_color="#05F29B",
                          icon=icons.ACCOUNT_TREE
                          )
    agregarBtn =  ElevatedButton(
                    text="Agregar Nodo",
                    icon="add",
                    style=ButtonStyle(bgcolor="#02FBAC",color="#1B1537"),
                    on_click=agregarEvent)
    recorridos = Column(spacing=10, controls=[
                    Text(f"Recorrido Inorden: {tree.inorden()}", text_align="center", color="#F2F2F2",style="titleMedium"),
                    Text(f"Recorrido Preorden: {tree.preorden()}", text_align="center", color="#F2F2F2",style="titleMedium"),
                    Text(f"Recorrido Postorden: {tree.postorden()}", text_align="center", color="#F2F2F2",style="titleMedium")
                    ]
                )
    nodos = GridView()
    row = Row(spacing=0,controls=Inicio,alignment="spaceBetween")
    page.add(
        Container(
            row,
            bgcolor="#1D1840",
            padding=10,
            border_radius= border_radius.only(topLeft=0,topRight=0,bottomRight=20,bottomLeft=20),
            expand=False),
        Container(
            content=nodos,
            width=page.window_max_width,
            height=page.window_max_height,
            bgcolor="#F2F2F2",
            expand=True,
            border_radius=5,
            padding=10,
            margin=12
        ),
        Container(
            Row(spacing=20,controls=[
                agregarBtn,
                ElevatedButton(
                    text="Eliminar Nodo",
                    icon="remove",
                    disabled=True),
                textField,
                recorridos]),
            margin=10
        )
    )

flet.app(target=main)