import os

BOT_TOKEN = '7349073816:AAHOob6JQwLR_WUgyBiXYZbuTAFlzJEzVSI'
YANDEX_GEOCODER_API_TOKEN = 'b479fb94-1d37-48c7-af20-48587817b75b'
OPEN_WEATHER_API_TOKEN = '13c96c4e69a2eabc395b3549fa743bc5'


def check_all_tokens_set():
    """Проверка на то, что установлены все переменные глобального окружения, необходимые для работы бота"""
    return BOT_TOKEN is not None and YANDEX_GEOCODER_API_TOKEN is not None and OPEN_WEATHER_API_TOKEN is not None
