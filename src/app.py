import flet as ft
from lenguajes import (
    prefijos,
    sufijos,
    subcadenas,
    cerradura_Kleene,
    cerradura_positiva
)


def main(page: ft.Page):
    page.title = "Calculadora de Teoría de Lenguajes"
    page.window.width = 550
    page.window.height = 700
    page.padding = 20
    page.scroll = ft.ScrollMode.ADAPTIVE

    titulo = ft.Text(
        "Operaciones con Cadenas y Alfabetos",
        size=22,
        weight=ft.FontWeight.BOLD
    )

    input_texto = ft.TextField(
        label="Cadena de texto (ej: abc)",
        width=400
    )

    input_longitud = ft.TextField(
        label="Longitud Máxima",
        width=400,
        disabled=True,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    texto_resultado = ft.Text(
        value="Aquí aparecerá el resultado...",
        selectable=True
    )

    
    def cambiar_op(e):
        seleccion = e.control.value

        if seleccion in ("Cerradura de Kleene", "Cerradura Positiva"):
            input_longitud.disabled = False
            input_texto.label = "Alfabeto (separado por comas, ej: 0, 1)"
        else:
            input_longitud.disabled = True
            input_longitud.value = ""
            input_texto.label = "Cadena de texto (ej: abc)"

            input_longitud.update()
            input_texto.update()

    opciones_dropdown = ft.Dropdown(
        label="Selecciona una operación",
        width=400,
        options=[
            ft.dropdown.Option("Prefijos"),
            ft.dropdown.Option("Sufijos"),
            ft.dropdown.Option("Subcadenas"),
            ft.dropdown.Option("Cerradura de Kleene"),
            ft.dropdown.Option("Cerradura Positiva"),
        ],
        on_select=cambiar_op
    )
    def mostrar_error(mensaje):
        texto_resultado.value = f"ERROR: {mensaje}"
        texto_resultado.color = ft.Colors.RED_400
        page.update()

    def calcular_res(e):
        op = opciones_dropdown.value
        texto = input_texto.value or ""

        texto_resultado.color = None

        if not op or not texto.strip():
            mostrar_error(
                "Por favor selecciona una operación y escribe "
                "la cadena o el alfabeto."
            )
            return

        texto = texto.strip()

        try:
            if op == "Prefijos":
                res = prefijos(texto)
                resultado = f"Prefijos: {res}"

            elif op == "Sufijos":
                res = sufijos(texto)
                resultado = f"Sufijos: {res}"

            elif op == "Subcadenas":
                res = subcadenas(texto)
                resultado = f"Subcadenas: {res}"

            elif op in [
                "Cerradura de Kleene",
                "Cerradura Positiva"
            ]:
                alfabeto = [
                    x.strip()
                    for x in texto.split(",")
                    if x.strip()
                ]

                if not alfabeto:
                    mostrar_error(
                        "El alfabeto no es válido o está vacío."
                    )
                    return

                try:
                    n = int(input_longitud.value)
                except (ValueError, TypeError):
                    mostrar_error(
                        "La longitud máxima debe ser un entero."
                    )
                    return

                if n < 0:
                    mostrar_error(
                        "La longitud máxima no puede ser negativa."
                    )
                    return

                k = len(alfabeto)
                inicio = 0 if op == "Cerradura de Kleene" else 1

                total = sum(k ** i for i in range(inicio, n + 1))

                if total > 200000:
                    mostrar_error(
                        f"Se intentaron generar {total} combinaciones.\n"
                        "El límite de seguridad es 200,000."
                    )
                    return

                if op == "Cerradura de Kleene":
                    res = cerradura_Kleene(alfabeto, n)
                else:
                    res = cerradura_positiva(alfabeto, n)

                resultado = (
                    f"Cálculo exitoso ({len(res)} elementos):\n{res}"
                )

            else:
                mostrar_error("La operación seleccionada no es válida.")
                return

            texto_resultado.value = resultado
            texto_resultado.color = None

        except Exception as ex:
            mostrar_error(f"Ocurrió un error al calcular: {ex}")
            return

        page.update()

    boton_calcular = ft.ElevatedButton(
        "Calcular",
        on_click=calcular_res
    )

    contenedor_resultado = ft.Container(
        content=ft.SelectionArea(
            content=texto_resultado
        ),
        padding=15,
        border_radius=5,
        width=500,
        border=ft.Border.all(1, ft.Colors.GREY_400)
    )

    page.add(
        titulo,
        opciones_dropdown,
        input_texto,
        input_longitud,
        boton_calcular,
        contenedor_resultado
    )

    page.update()


ft.run(main)