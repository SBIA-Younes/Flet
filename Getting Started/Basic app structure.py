import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    pass

# ft.app(target=main)  # rum the application as an application
ft.app(target=main, view=ft.AppView.WEB_BROWSER) # rum the application as a web browser
# ft.app(target=main, port=8550, view=ft.AppView.WEB_BROWSER) # rum the application as a web browser port 8050