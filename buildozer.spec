[app]
title = SER-TEC
package.name = sertecapp
package.domain = org.esteban
source.dir = .
source.include_exts = py,png,jpg,kv,wav
version = 1.0

# Requisitos en ingles (muy importante)
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,requests,urllib3,pygame

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Icono y Pantalla de Carga
icon.filename = logo.png
presplash.filename = logo.png

# Ajustes para GitHub Actions
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
