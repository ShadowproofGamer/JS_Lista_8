import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    
    lv = ft.ListView(expand=True, spacing=10)
    for i in range(2000):
        lv.controls.append(ft.Text(f"Line {i}"))

    #subpg = ft.Page()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ft.IconButton(ft.icons.NAVIGATE_NEXT_ROUNDED, on_click=plus_click),
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                lv,
                ft.Column(
                    [
                        #TODO
                    ]
                )
            ]
        )
        
    )

ft.app(target=main)