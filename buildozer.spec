[app]

# App title
title = SC Solutions

# Android package name
package.name = scsolutionsinvoice

# Android package domain
package.domain = com.scsolutions

# Main project folder
source.dir = .

# Main Python file
source.main = main.py

# File types included inside APK
source.include_exts = py,pdf,png,jpg,jpeg,ttf,otf,kv,txt,json,csv,db,sqlite,webp

# App version
version = 0.1

# Python requirements
# Kivy is pinned for safer Android builds
requirements = python3,kivy==2.3.0,reportlab,num2words,pillow

# Screen orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Android SDK path for GitHub Actions runner
android.sdk_path = /usr/local/lib/android/sdk

# Android NDK path for GitHub Actions runner
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

# Android API level
# Must match workflow: platforms;android-33
android.api = 33

# Minimum Android version
android.minapi = 21

# Accept Android SDK license automatically
android.accept_sdk_license = True

# Android entry point
android.entrypoint = sdl2

# Android permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET

# Build only arm64 first for fewer errors.
# Modern Android phones support arm64-v8a.
android.archs = arm64-v8a

# Allow Android backup
android.allow_backup = True

# Icon file if you have one
# icon.filename = %(source.dir)s/icon.png

# Splash image if you have one
# splash.filename = %(source.dir)s/splash.png
