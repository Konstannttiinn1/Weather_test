from datetime import date
from constants import DATE_FORMAT
from weather_forecast_utils.custom_typings import ForecastType


def get_pretty_html_forecast_message(location: str, forecast_date: date, forecast: ForecastType) -> str:
    main_info = forecast["main"]
    temperature = main_info["temp"]
    feels_like = main_info["feels_like"]

    return \
        f"""
<u><b>Прогноз погоды</b></u>
<i>{location}</i> | <i>{forecast_date.strftime(DATE_FORMAT)}</i>\n
–––––––––––––––––––––
<b>Температура воздуха</b> {temperature} °C
<b>Ощущается как:</b> {feels_like} °C

–––––––––––––––––––––\n

        """