import flet as ft



def main(page: ft.Page):
    x_w = page.width
    x_h = page.height
    standard_w = 400
    

    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=standard_w, read_only=True)

    txt_date = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=standard_w, read_only=True)
    txt_pid = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=standard_w, read_only=True)
    txt_user = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=standard_w, read_only=True)
    txt_description = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=standard_w, read_only=True)

    selected_id = 0

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

       
    def update_current(e):
        txt_date.value = str(e)
        page.update()

    button_before = ft.IconButton(ft.icons.NAVIGATE_BEFORE_ROUNDED, on_click=minus_click)
    button_next = ft.IconButton(ft.icons.NAVIGATE_NEXT_ROUNDED, on_click=plus_click)
    
    
    lv = ft.ListView(width=x_w/2, height=x_h/2, spacing=10)
    for i in range(2000):
        lv.controls.append(ft.Radio(label=f"Line {i}", value=i))

    radiogroup_list = ft.RadioGroup(content=lv, on_change=update_current)

    page.add(
        ft.TextField(value="Przeglądarka logów SSH", text_align=ft.TextAlign.CENTER, width=x_w, read_only=True, height=50),
        ft.Row(
            [
                txt_number,
                button_before,
                button_next
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
        [
            radiogroup_list,
            ft.Column(
                [
                    txt_date, 
                    txt_pid, 
                    txt_user, 
                    txt_description
                ], height=x_h/2, width=x_w/2
            )
        ],
        expand=True
        )
        
        
        
        
    )

ft.app(target=main)