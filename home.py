import flet as ft


def main(page: ft.Page):
    page.title = "NutriTech"
    page.bgcolor = ft.colors.WHITE
    page.padding = 0
    page.scroll = "auto"

    # Estilo geral
    def card(content, width=300, height=None):
        return ft.Container(
            content=content,
            width=width,
            height=height,
            padding=15,
            bgcolor=ft.colors.WHITE,
            border_radius=20,
            shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.BLACK12)
        )

    # Sidebar (menu)
    sidebar = ft.Container(
        width=230,
        bgcolor="#B4E2CE",
        padding=20,
        content=ft.Column(
            controls=[
                ft.Row([
                    ft.Icon(ft.icons.CLOSE),
                    ft.Text("NutriTech", size=20, weight="bold")
                ], alignment="spaceBetween"),
                ft.Container(height=20),
                ft.Column([
                    ft.ElevatedButton("Dashboard", icon=ft.icons.DASHBOARD, bgcolor="#FFA88A", color="white"),
                    ft.ElevatedButton("Pacientes", icon=ft.icons.PEOPLE, bgcolor="transparent", color="black"),
                    ft.ElevatedButton("Planos Alimentares", icon=ft.icons.RESTAURANT, bgcolor="transparent", color="black"),
                    ft.ElevatedButton("Perfil de Atividade Física", icon=ft.icons.FITNESS_CENTER, bgcolor="transparent", color="black"),
                    ft.ElevatedButton("Relatórios", icon=ft.icons.INSERT_CHART, bgcolor="transparent", color="black"),
                    ft.ElevatedButton("Preferências Alimentares", icon=ft.icons.FAVORITE, bgcolor="transparent", color="black"),
                    ft.ElevatedButton("Calculadoras", icon=ft.icons.CALCULATE, bgcolor="transparent", color="black"),
                    ft.ElevatedButton("Fotos de Refeições", icon=ft.icons.IMAGE, bgcolor="transparent", color="black"),
                ], spacing=5),
                ft.Container(height=20),
                ft.Row([
                    ft.Text("Light Mode"),
                    ft.Switch(value=True)
                ]),
                ft.ElevatedButton("Logout", icon=ft.icons.LOGOUT, bgcolor=ft.colors.GREEN_900, color="white")
            ],
            spacing=15
        )
    )

    # Busca e pacientes
    search_and_list = card(
        ft.Column([
            ft.TextField(hint_text="Digite o nome do paciente", prefix_icon=ft.icons.SEARCH),
            ft.ListView(
                expand=True,
                spacing=10,
                controls=[
                    ft.Text("Sam Pucket\nModificado em 24/05/2025 - 10:35", size=14),
                    ft.Text("Freddy Benson\nModificado em 24/05/2025 - 10:35", size=14),
                    ft.Text("Cat Valentine\nModificado em 24/05/2025 - 10:35", size=14),
                    ft.Text("Tori Vesga\nModificado em 24/05/2025 - 10:35", size=14),
                ]
            )
        ]),
        width=400,
        height=280
    )

    # Gráfico (imagem gerada)
    chart = card(
        ft.Column([
            ft.Text("Progresso Geral", size=16, weight="bold"),
            ft.Image(src="grafico.png", width=400, height=250, fit=ft.ImageFit.CONTAIN)
        ])
    )

    # Próximas Consultas e Agenda Semanal
    consultas_card = card(
        ft.Column([
            ft.Text("Próximas Consultas", size=16, weight="bold"),
            ft.Divider(),
            ft.Text("🍎 Spencer Shay\n20/06/2025 - 10:35"),
            ft.Text("🍎 Spencer Shay\n20/06/2025 - 10:35"),
            ft.Text("🍎 Spencer Shay\n20/06/2025 - 10:35")
        ]),
        width=350
    )

    agenda_card = card(
        ft.Column([
            ft.Text("Agenda Semanal", size=16, weight="bold"),
            ft.Divider(),
            ft.Checkbox(label="Consulta de Spencer Shay", value=False),
            ft.Checkbox(label="Enviar plano de Cat Valentine", value=True),
            ft.Checkbox(label="Consulta de Spencer Shay", value=False),
            ft.Checkbox(label="Consulta de Spencer Shay", value=False)
        ]),
        width=350
    )

    # Registro de fotografias
    conversas_card = card(ft.Text("Registros", size=16, weight="bold"), width=350)

    # Coluna esquerda e direita
    main_left = ft.Column([
        search_and_list,
        chart
    ], spacing=20)

    main_right = ft.Column([
        consultas_card,
        agenda_card,
        conversas_card
    ], spacing=20)

    # Layout principal
    page.add(
        ft.Row([
            sidebar,
            ft.Column([
                ft.Row([
                    main_left,
                    main_right
                ], alignment="start")
            ], scroll="auto")
        ])
    )


ft.app(target=main)
