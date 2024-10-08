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
        
        selected_id = selected_id - 1
        txt_number.value = str(selected_id - 1)
        update_nav_buttons(selected_id)
        page.update()

    def plus_click(e):
        
        selected_id = selected_id + 1
        txt_number.value = str(selected_id)
        update_nav_buttons(selected_id)
        page.update()

    def update_nav_buttons(id=selected_id):
        if(id + 1>=len(lv.controls)):
            button_next.disabled=True
        if(id - 1<=0):
            button_before.disabled=True
    
    def update_current(i=0):
        txt_date.value = str(i)
        page.update()

    button_before = ft.IconButton(ft.icons.NAVIGATE_BEFORE_ROUNDED, on_click=minus_click)
    button_next = ft.IconButton(ft.icons.NAVIGATE_NEXT_ROUNDED, on_click=plus_click)
    
    lv = ft.ListView(width=x_w/2, height=x_h/2, spacing=10)
    for i in range(2000):
        lv.controls.append(ft.TextButton(text=f"Line {i}", on_click=update_current(i)))



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
            lv,
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