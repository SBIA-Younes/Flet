import flet as ft

def main(page : ft.Page):
  # ! --------- Controler dont use a ref -----------
  first_name = ft.TextField(
    label="First name",
    autofocus=True,
  )
  last_name = ft.TextField(
    label="Last name",
  )
  greetings = ft.Column()
  
  def btn_click(e):
    greetings.controls.append(
      ft.Text(
        f'Hello, {first_name.value} {last_name.value}!'
      )
    )
    first_name.value = ""
    last_name.value = ""
    page.update()
    first_name.focus()
    
  
  page.add(
    first_name,
    last_name,
    ft.ElevatedButton(
      "Say hello!",
      on_click=btn_click,
    ),
    greetings,
  )
  
  # ! ---- Controler add a Ref ------
  first_name_ref = ft.Ref[ft.TextField()]
  last_name_ref = ft.Ref[ft.TextField()]
  greetings_ref = ft.Ref[ft.Column()]
  
  page.add(
    ft.TextField(
      ref=first_name_ref,
      label="First name ref",
      autofocus=True,
    ),
    ft.TextField(
      ref=last_name_ref,
      label='Last name ref',
    ),
    ft.ElevatedButton("Say hello!",on_click=btn_click),
    ft.Column(ref=greetings_ref)
    
  )
  
  

  
ft.app(target=main)