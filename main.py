import os
import webbrowser
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, NoTransition # Agregados estos dos
from kivy.core.window import Window
from kivy.core.audio import SoundLoader 
from kivy.utils import platform


# --- CONFIGURACIÓN DE DIRECTORIO ---
directorio_script = os.path.dirname(os.path.abspath(__file__))
os.chdir(directorio_script)

# --- CONFIGURACIÓN DE PANTALLA ---
if platform == 'android':
    Window.maximize()
else:
    Window.size = (360, 640)

KV = '''
ScreenManager:
    ScreenInicio:
    ScreenDatos:
    ScreenResumen:

<ScreenInicio>:
    name: 'inicio'
    MDFloatLayout:
        md_bg_color: 0, 0, 0, 1
        Image:
            source: 'logo.png'
            size_hint: (0.8, 0.5) 
            pos_hint: {"center_x": .5, "center_y": .6}
            allow_stretch: True
            keep_ratio: True
        MDFillRoundFlatButton:
            text: "EMPEZAR"
            pos_hint: {"center_x": .5, "center_y": .2}
            md_bg_color: 1, 0.4, 0, 1
            on_release: 
                app.reproducir_click()
                root.manager.current = 'datos'

<ScreenDatos>:
    name: 'datos'
    MDFloatLayout:
        md_bg_color: 0, 0, 0, 1
        
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"top": 0.98, "x": 0.02}
            theme_text_color: "Custom"
            text_color: 1, 0.5, 0, 1
            on_release: 
                app.reproducir_click()
                root.manager.current = 'inicio'
            
        MDLabel:
            text: "DATOS DEL EQUIPO"
            halign: "center"
            pos_hint: {"center_y": .88}
            theme_text_color: "Custom"
            text_color: 1, 0.5, 0, 1
            font_style: "H5"
            bold: True
            font_name: "RobotoMono-Regular"

        MDTextField:
            id: marca
            hint_text: "Marca del Celular"
            icon_right: "cellphone"
            pos_hint: {"center_x": .5, "center_y": .72}
            size_hint_x: .8
            mode: "rectangle"
            line_color_focus: 1, 0.5, 0, 1
            hint_text_color_focus: 1, 0.5, 0, 1
            text_color_normal: 1, 1, 1, 1
            text_color_focus: 1, 1, 1, 1
            icon_right_color_focus: 1, 0.5, 0, 1
            font_name: "RobotoMono-Regular"

        MDTextField:
            id: modelo
            hint_text: "Modelo exacto"
            icon_right: "tag-outline"
            pos_hint: {"center_x": .5, "center_y": .58}
            size_hint_x: .8
            mode: "rectangle"
            line_color_focus: 1, 0.5, 0, 1
            hint_text_color_focus: 1, 0.5, 0, 1
            text_color_normal: 1, 1, 1, 1
            text_color_focus: 1, 1, 1, 1
            icon_right_color_focus: 1, 0.5, 0, 1
            font_name: "RobotoMono-Regular"

        MDTextField:
            id: problema
            hint_text: "Falla o problema"
            icon_right: "tools"
            multiline: True
            pos_hint: {"center_x": .5, "center_y": .38}
            size_hint_x: .8
            mode: "rectangle"
            line_color_focus: 1, 0.5, 0, 1
            hint_text_color_focus: 1, 0.5, 0, 1
            text_color_normal: 1, 1, 1, 1
            text_color_focus: 1, 1, 1, 1
            icon_right_color_focus: 1, 0.5, 0, 1
            font_name: "RobotoMono-Regular"

        MDFillRoundFlatButton:
            text: "GENERAR RESUMEN"
            font_size: "18sp"
            pos_hint: {"center_x": .5, "center_y": .15}
            size_hint_x: .7
            md_bg_color: 1, 0.4, 0, 1
            font_name: "RobotoMono-Regular"
            on_release: 
                app.reproducir_click()
                app.preparar_resumen(marca.text, modelo.text, problema.text)
                root.manager.current = 'resumen'

<ScreenResumen>:
    name: 'resumen'
    MDFloatLayout:
        md_bg_color: 0, 0, 0, 1
        
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"top": 0.98, "x": 0.02}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            on_release: 
                app.reproducir_click()
                root.manager.current = 'datos'

        MDLabel:
            text: "CONFIRMAR PEDIDO"
            halign: "center"
            pos_hint: {"center_y": .9}
            theme_text_color: "Custom"
            text_color: 1, 0.5, 0, 1
            font_style: "H6"
            bold: True
            font_name: "RobotoMono-Regular"

        MDLabel:
            id: info_resumen
            text: ""
            halign: "left"
            pos_hint: {"center_x": .5, "center_y": .65}
            size_hint_x: .8
            theme_text_color: "Custom"
            text_color: .9, .9, .9, 1
            markup: True
            font_name: "RobotoMono-Regular"
            line_height: 1.2

        MDTextField:
            id: nombre_cliente
            hint_text: "Nombre del Cliente"
            icon_right: "account"
            pos_hint: {"center_x": .5, "center_y": .4}
            size_hint_x: .85
            mode: "rectangle"
            font_name: "RobotoMono-Regular"

        MDFillRoundFlatButton:
            text: "ENVIAR A SER-TEC"
            pos_hint: {"center_x": .5, "center_y": .18}
            size_hint_x: .75
            padding: "12dp"
            md_bg_color: 0.15, 0.65, 0.35, 1
            font_name: "RobotoMono-Regular"
            on_release: 
                app.reproducir_click()
                app.enviar_whatsapp(nombre_cliente.text)
'''

class ScreenInicio(Screen): pass
class ScreenDatos(Screen): pass
class ScreenResumen(Screen): pass

class SerTecApp(MDApp):
    datos_equipo = {}

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def reproducir_click(self):
        """Carga y reproduce el sonido click.wav"""
        try:
            # SoundLoader busca el archivo en el directorio actual
            sonido = SoundLoader.load('click.wav')
            if sonido:
                sonido.play()
        except Exception as e:
            print(f"No se pudo reproducir el sonido: {e}")

    def preparar_resumen(self, marca, modelo, problema):
        self.datos_equipo = {"marca": marca, "modelo": modelo, "problema": problema}
        resumen_screen = self.root.get_screen('resumen')
        
        # Corregí los saltos de línea para que se vean bien en la pantalla
        resumen_screen.ids.info_resumen.text = (
            f"[color=#FF8000][b]EQUIPO:[/b][/color]\\n"
            f"{marca} {modelo}\\n\\n"
            f"[color=#FF8000][b]FALLA REPORTADA:[/b][/color]\\n"
            f"{problema}"
        ).replace("\\n", "\n")

    def enviar_whatsapp(self, nombre):
        if not nombre:
            nombre = "Cliente"
            
        numero = "5491136520765"
        mensaje = (f"¡Hola SER-TEC! Soy {nombre}.\\n\\n"
                   f"*ORDEN DE REPARACIÓN*\\n"
                   f"----------------------------\\n"
                   f"📱 *Marca:* {self.datos_equipo.get('marca', '')}\\n"
                   f"📝 *Modelo:* {self.datos_equipo.get('modelo', '')}\\n"
                   f"⚠️ *Falla:* {self.datos_equipo.get('problema', '')}")
        
        mensaje_url = mensaje.replace(" ", "%20").replace("\\n", "%0A")
        url = f"https://wa.me/{numero}?text={mensaje_url}"
        webbrowser.open(url)

if __name__ == '__main__':
    SerTecApp().run()