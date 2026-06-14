[app]

# Title shown on Android app
title = SC Solutions

# Package name must be lowercase, no spaces
package.name = scsolutionsinvoice

# Package domain should be valid Android style
package.domain = com.scsolutions

# Main Python file
source.dir = .

# Include these file types in APK
source.include_exts = py,pdf,png,jpg,jpeg,ttf,otf,kv

# Main Python entry file
source.main = main.py

# App version
version = 0.1

# Requirements for Python inside APK
requirements = python3,kivy,reportlab,num2words,pillow

# Orientation
orientation = portrait

# Fullscreen mode
# 0 = normal window/title behavior
# 1 = fullscreen
fullscreen = 0

# Android permissions
# WRITE_EXTERNAL_STORAGE is needed for saving PDF to Download on older Android versions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET

# Android architecture
android.archs = arm64-v8a,armeabi-v7a

# Android API level
# Keep this as 33 if your GitHub Actions workflow installs platforms;android-33
android.api = 33

# Minimum Android version supported
android.minapi = 21

# Android NDK version
android.ndk = 25b

# Accept Android SDK license automatically in CI
android.accept_sdk_license = True

# Android entry point
android.entrypoint = sdl2

# Android SDK path
# Leave blank unless you are using a custom SDK path
android.sdk_path =

# Android NDK path
# Leave blank unless you are using a custom NDK path
android.ndk_path =

# Buildozer bin directory
bin_dir = ./bin

# Buildozer build directory
build_dir = ./.buildozer

# Icon file
# If you do not have icon.png, remove this line or add a real icon.png file
# icon.filename = %(source.dir)s/icon.png

# Splash image
# If you do not have splash.png, remove this line or add a real splash.png file
# splash.filename = %(source.dir)s/splash.png

# Android package display name
# android.apptheme =

# Android manifest extra permissions if needed later
# android.add_permissions = CAMERA,ACCESS_FINE_LOCATION

# Add extra Android Java source files if needed later
# android.add_src =

# Add extra AAR libraries if needed later
# android.add_aars =

# Add extra JAR libraries if needed later
# android.add_jars =

# Add Gradle dependencies if needed later
# android.gradle_dependencies =

# Android backup allow
android.allow_backup = True

# Android backup rules file if needed later
# android.backup_rules =

# Android manifest placeholders if needed later
# android.manifest_placeholders =

# Log level
log_level = 2

# Warn when running as root
warn_on_root = 1


[buildozer]

# Default profile
profile = default

# Log level
log_level = 2

# Ignore some common build warnings
ignore =
