[app]
title = SER TEC
package.name = sertecapp
package.domain = org.esteban
source.dir = .
source.include_exts = py,png,jpg,kv,wav
version = 1.0

# Requisitos mínimos (sacamos pygame y todo lo extra)
requirements = python3,kivy==2.3.0,kivymd==1.2.0

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

icon.filename = logo.png
presplash.filename = logo.png

# CONFIGURACIÓN ANTIFALLO
android.accept_sdk_license = True
android.api = 31
android.minapi = 21
android.archs = arm64-v8a
# Esto es clave para que GitHub vea que algo está pasando
log_level = 2
