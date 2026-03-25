[app]
title = SER TEC
package.name = sertecapp
package.domain = org.esteban
source.dir = .
source.include_exts = py,png,jpg,kv,wav
version = 1.0

# Solo lo básico para que arranque
requirements = python3,kivy==2.3.0,kivymd==1.2.0

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Versiones fijas que sabemos que funcionan rápido
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

# Bajamos el nivel de log para que no gaste tiempo escribiendo de más
log_level = 1
