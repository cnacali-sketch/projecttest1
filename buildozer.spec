[app]

title = SC Solutions
package.name = scsolutionsinvoice
package.domain = com.scsolutions

source.dir = .
source.main = main.py

source.include_exts = py,pdf,png,jpg,jpeg,ttf,otf,kv,txt,json,csv,db,sqlite,webp

version = 0.1

requirements = python3,kivy==2.3.0,reportlab,num2words,pillow

orientation = portrait
fullscreen = 0

# GitHub Actions Android SDK path
android.sdk_path = /usr/local/lib/android/sdk

# GitHub Actions Android NDK path
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

android.api = 33
android.minapi = 21

android.accept_sdk_license = True

android.entrypoint = sdl2

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET

android.archs = arm64-v8a

android.allow_backup = True

# icon.filename = %(source.dir)s/icon.png
# splash.filename = %(source.dir)s/splash.png

log_level = 2
warn_on_root = 1


[buildozer]

profile = default
log_level = 2
