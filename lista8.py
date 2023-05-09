import flet as ft
import l8_backend as core
import variables as var



def main(page: ft.Page):

    #ustalanie wymiarów aplikacji
    x_w = page.width
    x_h = page.height
    if(page.width<1200 or page.height<700):
        x_w = 1280
        x_h = 720
    
    #ustalanie wymiarów elementów o stałym rozmiarze
    shorter_w = 300
    standard_w = 450
    
    #dane okna aplikacji
    page.title = "Przeglądarka logów SSH"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #pola pobierające dane
    txt_address = ft.TextField(hint_text="Podaj adres logów SSH do przejrzenia", text_align=ft.TextAlign.RIGHT, width=standard_w, label="adres logów ssh")
    txt_start = ft.TextField(hint_text="Jan  7 16:55:14", text_align=ft.TextAlign.RIGHT, width=shorter_w, label="data początkowa (opcjonalna)", keyboard_type=ft.KeyboardType.DATETIME)
    txt_end = ft.TextField(hint_text="Jan  7 16:55:14", text_align=ft.TextAlign.RIGHT, width=shorter_w, label="data końcowa (opcjonalna)", keyboard_type=ft.KeyboardType.DATETIME)

    #pola tekstowe które wyświetlać będą dane
    txt_current_line = ft.TextField(value="", text_align=ft.TextAlign.CENTER, width=x_w, read_only=True, label="obecnie przeglądany log")
    txt_date = ft.TextField(value="", text_align=ft.TextAlign.LEFT, width=standard_w, read_only=True, label="data")
    txt_pid = ft.TextField(value="", text_align=ft.TextAlign.LEFT, width=standard_w, read_only=True, label="pid")
    txt_user = ft.TextField(value="", text_align=ft.TextAlign.LEFT, width=standard_w, read_only=True, label="użytkownik")
    txt_description = ft.TextField(value="", text_align=ft.TextAlign.LEFT, width=standard_w, read_only=True, multiline=True, label="opis")
    txt_ip = ft.TextField(value="", text_align=ft.TextAlign.LEFT, width=standard_w, read_only=True, label="IPv4")


    #event handlery związane z klikaniem przycisków i zachowaniem GUI
    def minus_click(e):
        var.current_id-=1
        refresh_button()
        refresh_detail()
        page.update()

    def plus_click(e):
        var.current_id+=1
        refresh_button()
        refresh_detail()
        page.update()

       
    def update_current(e):
        var.current_id=int(e.control.value)
        refresh_button()
        refresh_detail()
        page.update()

    def search(e):
        #try:
        core.initializer(str(txt_address.value))
        n=0
        for i in var.info_list:
            lv.controls.append(ft.Radio(label=str(i[0][0:70:]), value=n))
            n+=1
        refresh_detail()
        #except:txt_address.value = f"failed to find {txt_address.value}!"
        refresh_button()
        page.update()

    #TODO
    def output_filter(e):
        pass

    def refresh_button():
        #print(f"len: {len(lv.controls)}, id: {var.current_id}, next_dis: {button_next.disabled}, before_dis: {button_before.disabled}")
        if(len(lv.controls)==var.current_id+1):
            button_next.disabled=True
        elif(button_next.disabled==True and len(lv.controls)>var.current_id+1):
            button_next.disabled=False
        if(var.current_id==0):
            button_before.disabled=True
        elif(button_before.disabled==True and var.current_id>0):
            button_before.disabled=False

    def refresh_detail():
        txt_current_line.value=var.info_list[var.current_id][0]
        txt_date.value=var.info_list[var.current_id][1]
        txt_pid.value=var.info_list[var.current_id][2]
        txt_user.value=var.info_list[var.current_id][3]
        txt_description.value=var.info_list[var.current_id][4]
        txt_ip.value=var.info_list[var.current_id][5]


    #przyciski uruchamiające procesy zmieniające stronę
    button_search = ft.IconButton(ft.icons.SEARCH, on_click=search)
    button_before = ft.IconButton(ft.icons.NAVIGATE_BEFORE_ROUNDED, on_click=minus_click, disabled=True)
    button_next = ft.IconButton(ft.icons.NAVIGATE_NEXT_ROUNDED, on_click=plus_click, disabled=True)
    button_apply_filter = ft.IconButton(ft.icons.FILTER_ALT, on_click=output_filter)
    

    #element master
    lv = ft.ListView(width=x_w/2, height=x_h/2, spacing=10)
    radiogroup_list = ft.RadioGroup(content=lv, on_change=update_current)


    #dodawanie elementów do GUI
    page.add(
        ft.Row(
        [
            ft.TextField(value="Przeglądarka logów SSH", text_align=ft.TextAlign.CENTER, width=x_w, read_only=True, border=ft.InputBorder.NONE,)
        ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                txt_address,
                button_search
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                txt_start,
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
        [txt_current_line],
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
                        txt_ip,
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