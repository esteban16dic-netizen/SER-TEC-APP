[app]
title = SER TEC
package.name = sertecapp
package.domain = org.esteban
source.dir = .
source.include_exts = py,png,jpg,kv,wav
version = 1.0

# Requisitos limpios (sacamos pygame por ahora para que no pese)
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Ajustes de estabilidad
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

# Para ver el error exacto si falla
log_level = 2
