import flet as ft
import pyperclip
from src.translate import translate_text



@ft.component
def App()-> ft.Control:
    
    text , set_text = ft.use_state("hello") #type: ignore

    text_trn , set_txtTrans =  ft.use_state("hola") #type: ignore

    def handle_copy(e: ft.Event[ft.Button]) -> None:
        text_new:str =  pyperclip.paste()

        set_text(text_new)

        result = translate_text(text_new)

        set_txtTrans(result)



    text_past = ft.TextField(
        label="text to translate",
        hint_text="Write your text here...",
        value=text,
        multiline=True,
        min_lines=5,
        max_lines=10,
        max_width=500,
        expand=True,
        bgcolor= "#383F56",
        border=ft.OutlineInputBorder(
            border_radius=12,
            side=ft.BorderSide(
                width=1,
                color="#48536D"
            )
        ),
        read_only=True
    )

    text_translate = ft.TextField(
        label="Translate ES",
        hint_text="Write your text here...",
        multiline=True,
        min_lines=5,
        max_lines=10,
        max_width=500,
        expand=True,
        read_only=True,
        value=text_trn,
        bgcolor= "#383F56",
        border=ft.OutlineInputBorder(
            border_radius=12,
            side=ft.BorderSide(
                width=1,
                color="#48536D"
            )
        )
    )

    btn_trans = ft.Button(
        "translate", 
        min_width=150, 
        width=400, 
        bgcolor="#8494FF",
        color=ft.Colors.WHITE ,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            elevation={
                ft.ControlState.DEFAULT: 2,
                ft.ControlState.HOVERED: 8,
            },
            shadow_color="#6366F1",
            padding=ft.Padding.symmetric(
                horizontal=10,
                vertical=17
            ),
         
        ),
        
        on_click=handle_copy)

    col_main = ft.Column(
        [
            ft.Text("Translate", size=30),
            text_past,
            btn_trans,
            text_translate
        ], 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,spacing=20)

    return ft.Container(
        content=col_main,
        padding=20,
        border_radius=10,
    )



def main(page: ft.Page) -> None:
    page.title = "APP"
    page.fonts = {
        "Inter": "src/assets/Inter/Inter-Italic.ttf",
        "Inter_variable": "src/assets/Inter/Inter-Variable.ttf"
    }

    page.theme = ft.Theme(
        font_family="Inter_variable"
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding=0
    page.window.frameless = False
    # Native window: transparent
    page.window.bgcolor = ft.Colors.TRANSPARENT

    # Page: 50% transparent
    page.bgcolor = ft.Colors.with_opacity(
        0.9, "#25293B"
    )

    page.window.width = 500
    page.window.height =  500
    page.render(App)


if __name__ == "__main__":
    ft.run(main)
