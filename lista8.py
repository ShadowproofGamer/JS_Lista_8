import flet as ft
import l8_backend as core
import variables as var



def main(page: ft.Page):
    x_w = page.width
    x_h = page.height
    if(page.width<1200 or page.height<700):
        x_w = 1280
        x_h = 720
    
    shorter_w = 300
    standard_w = 450
    

    page.title = "Przeglądarka logów SSH"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    txt_number = ft.TextField(hint_text="Podaj adres logów SSH do przejrzenia", text_align=ft.TextAlign.RIGHT, width=standard_w, label="adres logów ssh")

    txt_date = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=standard_w, read_only=True, label="date")
    txt_pid = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=standard_w, read_only=True, label="pid")
    txt_user = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=standard_w, read_only=True, label="user")
    txt_description = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=standard_w, read_only=True, multiline=True, label="description")

    txt_start = ft.TextField(hint_text="Jan  7 16:55:14", text_align=ft.TextAlign.RIGHT, width=shorter_w, label="data początkowa", keyboard_type=ft.KeyboardType.DATETIME)
    txt_end = ft.TextField(hint_text="Jan  7 16:55:14", text_align=ft.TextAlign.RIGHT, width=shorter_w, label="data końcowa", keyboard_type=ft.KeyboardType.DATETIME)

    def minus_click(e):
        #txt_number.value = str(int(txt_number.value) - 1)
        #txt_number.value = f"width = {page.width}, height = {page.height}"
        page.update()

    def plus_click(e):
        #txt_number.value = str(int(txt_number.value) + 1)
        #txt_number.value = f"width = {page.width}, height = {page.height}"
        var.current_id+=1
        lv.controls[var.current_id].focus()
        if(len(lv.controls)==var.current_id+1):
            button_next.disabled=True
        elif(button_next.disabled==True and len(lv.controls)>var.current_id+1):
            button_next.disabled=False
        page.update()

       
    def update_current(e):
        txt_date.value = str(e)
        if(var.current_id>0):
            button_before.disabled=False
        if(var.current_id<len(lv.controls)-1):
            button_next.disabled=False
        print(e.controls.value)
        page.update()

    def search(e):
        try:
            core.initializer(str(txt_number.value))
            for i in var.ssh_list:
                lv.controls.append(ft.Radio(label=f"", value=i))
            button_next.disabled=False
        except:
            txt_number.value = f"failed to find {txt_number.value}!"
        if(len(lv.controls)>1):
            button_next.disabled=False
        page.update()

    def output_filter(e):
        pass

    button_search = ft.IconButton(ft.icons.SEARCH, on_click=search)
    button_before = ft.IconButton(ft.icons.NAVIGATE_BEFORE_ROUNDED, on_click=minus_click, disabled=True)
    button_next = ft.IconButton(ft.icons.NAVIGATE_NEXT_ROUNDED, on_click=plus_click, disabled=True)
    
    button_apply_filter = ft.IconButton(ft.icons.FILTER_ALT, on_click=output_filter)
    
    lv = ft.ListView(width=x_w/2, height=x_h/2, spacing=10)
    for i in range(500):lv.controls.append(ft.Radio(label=f"Line {i}", value=i))

    radiogroup_list = ft.RadioGroup(content=lv, on_change=update_current)
    #txt_number.value = f"width = {page.width}, height = {page.height}"

    page.add(
        ft.Row(
        [
            ft.TextField(value="Przeglądarka logów SSH", text_align=ft.TextAlign.CENTER, width=x_w, read_only=True, border=ft.InputBorder.NONE,)
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                txt_number,
                button_search
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                #ft.TextField(value="start: ", text_align=ft.TextAlign.CENTER, width=100, read_only=True),
                txt_start,
                #ft.TextField(value="koniec: ", text_align=ft.TextAlign.CENTER, width=100, read_only=True),
                txt_end,
                button_apply_filter

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                button_before,
                button_next
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        
        ft.Row(
            [
                radiogroup_list,
                ft.Column(
                    [
                        txt_date,
                        txt_pid,
                        txt_user,
                        txt_description,
                        
                    ], height=x_h/2, width=x_w/2
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER
        )
        
        
        
        
    )
    page.update()
    

ft.app(target=main)