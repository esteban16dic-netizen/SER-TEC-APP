[app]
title = SER-TEC
package.name = sertecapp
package.domain = org.esteban
source.dir = .
source.include_exts = py,png,jpg,kv,wav
version = 1.0

# Requisitos bien declarados
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,requests,urllib3,pygame

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Iconos
icon.filename = logo.png
presplash.filename = logo.png

# ESTO ES LO QUE ARREGLA EL ERROR DE LOS 8 MINUTOS:
android.accept_sdk_license = True
# Dejamos solo una arquitectura para que sea más rápido y no falle por espacio
android.archs = arm64-v8a
android.allow_backup = True

# Nivel de detalle para ver el error si vuelve a fallar
log_level = 2
