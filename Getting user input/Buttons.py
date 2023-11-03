import flet as ft 

def main(page : ft.Page):
  
  btn = ft.ElevatedButton("Click me")
  page.add(btn)
  
ft.app(target=main)