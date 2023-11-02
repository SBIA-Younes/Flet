import time
import flet as ft


def main(page: ft.Page):
  t = ft.Text(
    value="Hello, world",
    color='green',
  )
  # page.controls.append(t) 
  # page.update()
  page.add(t) # it's a shortcut for page.controls.append(t) and then page.update()
  
  for i in range(10):
    t.value = f'Step {i}'
    page.update()
    time.sleep(0.5)
  
  page.add(
    ft.Row(
      controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C"),
      ]
    )
  )
  
  page.add(
    ft.Row(
      controls=[
        ft.TextField(label="Your name"),
        ft.ElevatedButton(text="Say my name!")
      ]
    )
  )
  
  for i in range(10):
    page.controls.append(ft.Text(f'Line {i}'))
    if i > 4:
      page.controls.pop(0)
    page.update()
    time.sleep(0.3)
  

ft.app(target=main)