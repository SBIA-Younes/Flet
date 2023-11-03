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
    
    
  def button_clicked(e):
    page.add(ft.Text("Clicked!"))
    
  page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))
  
  first_name = ft.TextField()
  last_name = ft.TextField()
  first_name.disabled = True
  last_name.disabled = True
  page.add(first_name, last_name)
  
  first_name_c = ft.TextField()
  last_name_c = ft.TextField()
  c = ft.Column(
    controls=[
      first_name_c,
      last_name_c
    ]
  )
  
  c.disabled = True
  page.add(c)
  
ft.app(target=main)