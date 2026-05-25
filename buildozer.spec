[app]
# Название твоей игры на экране телефона
title = Brawl-Stars-v36

# Уникальный ID твоего приложения
package.name = brawlv36
package.domain = com.vspysh

# Какие файлы включать в APK (все файлы python и твои папки)
source.include_exts = py
source.include_dirs = Logic, Protocol, Database

# Главный файл запуска
source.dir = .
entrypoint = main.py

# Настройки экрана
version = 1.0
orientation = landscape

# Права доступа (чтобы сервер мог принимать подключения)
android.permissions = INTERNET

# Версии для сборки
android.api = 31
android.minapi = 21
