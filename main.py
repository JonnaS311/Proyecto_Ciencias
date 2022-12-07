import Avl
import flet
from flet import Page, Text, Container, icons, Row, ButtonStyle, padding, border_radius, IconButton

nombreApp = "Binary Tree 🌲"


def main(page: Page):
    page.title = nombreApp

    page.bgcolor = "#2E2A52"
    page.padding = padding.only(top=0, bottom=10)
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.window_full_screen = True
    page.window_resizable = False


    Titulo = Container(
        bgcolor="#1D1840",
        padding=10,
        border_radius=border_radius.only(
            topLeft=0, topRight=0, bottomRight=20, bottomLeft=20),
        content= Row([Text(nombreApp ,expand=True,text_align="center"),IconButton(flet.icons.CLOSE, on_click=lambda _: page.window_close())])
    )

    texto1 = flet.TextField(
        label="Valor del Nodo",
        keyboard_type="number",
        filled=True,
        border="underline",
        border_color="#05F29B",
        icon=icons.ACCOUNT_TREE
    )
    RecorridoInorden = flet.Text(
        "Recorrido Inorden:", text_align="center",
        color="#FFFFFF", style="titleMedium"
    )
    RecorridoPreorden = flet.Text(
        "Recorrido Preorden:", text_align="center",
        color="#FFFFFF", style="titleMedium"
    )
    RecorridoPostorden = flet.Text(
        "Recorrido Postorden:", text_align="center",
        color="#FFFFFF", style="titleMedium"
    )
    recorridos = flet.Column(
        controls=[
            RecorridoInorden, RecorridoPreorden,RecorridoPostorden
        ]
    )

    arbol = Avl.Avl()
    Xnodos = [flet.Row(alignment="spaceAround"), flet.Row(alignment="spaceAround")]
    Ynodos = flet.Column(spacing=5, controls=Xnodos, expand=True, width=700)

    labelNodos = flet.Container(
        content=Ynodos,
        bgcolor="#FFFFFF",
        expand=False,
        width= 1600,
        height= 650,
        border_radius=5,
        padding=10,
        margin=12
    )

    def eliminarNodo_Buton_Controler(e):
        arbol.eliminar(arbol.buscar(int(texto1.value), arbol.getRaiz()))
        Xnodos.clear()
        for i in range(10):
            Xnodos.append(flet.Row(alignment="spaceAround"))
        agregarnodorecursivo(arbol.getRaiz(), 0)
        RecorridoInorden.value = "Recorrido Inorden : " + str(arbol.inorden(arbol.getRaiz()))
        RecorridoPreorden.value = "Recorrido Preorden : " + str(arbol.preorden(arbol.getRaiz()))
        RecorridoPostorden.value = "Recorrido Postorden : " + str(arbol.postorden(arbol.getRaiz()))
        page.update()

    EliminarNodo = flet.ElevatedButton(
        text="Eliminar Nodo",
        icon="remove",
        disabled=False,
        on_click=eliminarNodo_Buton_Controler)

    def crearBotonNodo(valor):
        miValor = valor
        return flet.ElevatedButton(miValor,color="#FFFFFF", bgcolor="#2E2A52",
                                   style=ButtonStyle(shape=flet.CircleBorder(), padding=10))

    def agregarnodorecursivo(nodo, indice):
        if nodo is not None:
            Xnodos[indice].controls.append(crearBotonNodo(nodo.getValue()))
        if nodo is not None:
            indice = indice + 1
            if nodo.getLeft() is not None:
                agregarnodorecursivo(nodo.getLeft(), indice)
            if nodo.getLeft() is None:
                #Xnodos[indice].controls.append(flet.Container(expand=False, bgcolor="#000000"))
                Xnodos[indice].controls.append(flet.FilledButton(style=ButtonStyle(bgcolor="FFFFFF"),height=0))
            if nodo.getRight() is not None:
                agregarnodorecursivo(nodo.getRight(), indice)
            if nodo.getRight() is None:
               # Xnodos[indice].controls.append(flet.Container(expand=False, bgcolor="#000000"))
                Xnodos[indice].controls.append(flet.FilledButton(style=ButtonStyle(bgcolor="FFFFFF"),height=0))

    def agregarNodoVisible(e):
        arbol.insertar(int(texto1.value), arbol.getRaiz())
        Xnodos.clear()
        for i in range(10):
            Xnodos.append(flet.Row(alignment="spaceAround"))
        RecorridoInorden.value = "Recorrido Inorden : " + str(arbol.inorden(arbol.getRaiz()))
        RecorridoPreorden.value = "Recorrido Preorden : " + str(arbol.preorden(arbol.getRaiz()))
        RecorridoPostorden.value = "Recorrido Postorden : " + str(arbol.postorden(arbol.getRaiz()))

        agregarnodorecursivo(arbol.getRaiz(), 0)

        page.update()

    AgregarNodo = flet.ElevatedButton(
        text="Agregar Nodo",
        icon="add",
        style=ButtonStyle(bgcolor="#02FBAC", color="#1B1537"),
        on_click=agregarNodoVisible
    )

    botones = flet.Container(
        Row(spacing=20, controls=[
            AgregarNodo,
            EliminarNodo,
            texto1,
            recorridos,
        ]
            ),
        margin=10
    )
    page.add(Titulo,
             labelNodos,
             botones,
             )


flet.app(target=main)
