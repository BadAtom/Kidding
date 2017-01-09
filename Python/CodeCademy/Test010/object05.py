from requests import get

out = {'ru': ("Выберите язык (ru)", "Введите целое число: ", "Это неверное число.", "Выберите год производства: ",
              "Выберите марку: ", "Выберите модель: ", "Проблема при запросе. Ошибка №"),
       'en': ("Choose the language (en)", "Input integer number: ", "It's incorrect number.",
              "Choose production year: ", "Choose a maker: ", "Choose a model: ", "Bad request. Error №")}
url = "http://webapi.nhtsa.gov/api/SafetyRatings"
get_format = "?format=json"
lang = ""


def get_int():
    try:
        return int(input(out[lang][1]))
    except ValueError:
        print(out[lang][2])
        return get_int()

while lang != "ru" and lang != "en":
    lang = str(input(out['ru'][0] + " / " + out['en'][0] + ": "))


