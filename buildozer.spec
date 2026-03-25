[app]
title = SER TEC
package.name = sertecapp
package.domain = org.esteban
source.dir = .
source.include_exts = py,png,jpg,kv,wav
version = 1.0

# Reducimos los requisitos al mínimo necesario para que no pese tanto
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,pygame

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

icon.filename = logo.png
presplash.filename = logo.png

# CONFIGURACIÓN ANTIFALLO
android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.skip_update = False

# Solo una arquitectura (la más liviana)
android.archs = arm64-v8a

# Esto evita que se quede "mudo" y corten la conexión
log_level = 2
