import flet as ft

def main(page : ft.Page):
  def Checkbox_changed(e):
    output_text.value = (
      f"you have learned how to ski : {todo_chek.value}"
    )
    page.update()
    
  output_text = ft.Text()
  todo_chek = ft.Checkbox(
    label="Todo Learn how to use ski",
    value=False,
    on_change=Checkbox_changed
  )
  page.add(todo_chek, output_text)
  
ft.app(target=main)