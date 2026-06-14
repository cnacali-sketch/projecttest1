[app]

# App name
title = SC Solutions

# Android package name
package.name = scsolutionsinvoice

# Android package domain
package.domain = com.scsolutions

# Project source folder
source.dir = .

# Main Python file
source.main = main.py

# File types included in APK
source.include_exts = py,pdf,png,jpg,jpeg,ttf,otf,kv,txt

# App version
version = 0.1

# Python packages inside APK
# Keep Kivy pinned for safer Android build
requirements = python3,kivy==2.3.0,reportlab,num2words,pillow

# Screen orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Android SDK path for GitHub Actions runner
# Your log shows this path exists on the GitHub runner
android.sdk_path = /usr/local/lib/android/sdk

# Android NDK path for GitHub Actions runner
# Your log shows this path exists on the GitHub runner
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

# Android API level
# Must match installed platform in workflow: platforms;android-33
android.api = 33

# Minimum Android version
android.minapi = 21

# NDK version setting
# Not used if android.ndk_path is set, but keep for reference
android.ndk = 27.3.13750724

# Accept Android SDK license
android.accept_sdk_license = True

# Android entry point
android.entrypoint = sdl2

# Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET

# Start with one architecture first.
# arm64-v8a works on modern Android phones.
# After build succeeds, you can try adding armeabi-v7a later.
android.archs = arm64-v8a

# App backup
android.allow_backup = True

# Icon if you have one
# icon.filename = %(source.dir)s/icon.png

# Splash if you have one
# splash.filename = %(source.dir)s/splash.png

# Log level
log_level = 2

# Root warning
warn_on_root = 1


[buildozer]

profile = default
log_level = 2
