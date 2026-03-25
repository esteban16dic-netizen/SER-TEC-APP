[app]
title = SER TEC
package.name = sertecapp
package.domain = org.esteban
source.dir = .
source.include_exts = py,png,jpg,kv,wav
version = 1.0

# Requisitos básicos (sacamos pygame por ahora para asegurar el APK)
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

icon.filename = logo.png
presplash.filename = logo.png

# CONFIGURACIÓN DE SEGURIDAD (Esto es lo que evita el Broken Pipe)
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.skip_update = False

# Solo una arquitectura (la más común y rápida de compilar)
android.archs = arm64-v8a

# Para que GitHub no corte la conexión por silencio
log_level = 2
