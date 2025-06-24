[app]

title = MyBotApp
package.name = mybotapp
package.domain = org.telegram.bot
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
requirements = python3,kivy,telebot,colorama,requests
orientation = portrait

osx.python_version = 3
fullscreen = 0

android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 30
android.minapi = 21
android.ndk = 23b
android.arch = armeabi-v7a
android.sdk = 24
android.gradle_dependencies = 

# (إظهار سجل الأخطاء)
log_level = 2

[buildozer]

log_level = 2
warn_on_root = 1
