
# 2------------------------------------------------------------
from requests import get, utils

res = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp."))


def currency_rates(code):
    content = res.split("Valute ID=")
    for i in content:
        if code.upper() in i:
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


print(currency_rates("uSd"))
print(currency_rates("EUR"))

# 3------------------------------------------------------------
from datetime import date
from requests import get, utils

res = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp."))


def currency_rates(code):
    content = res.split("Valute ID=")
    d, m, y = content[0].split()[3].split("Date=")[1][1:-1].split(".")

    for i in content:
        if code.upper() in i:
            print(date(year=int(y), month=int(m), day=int(d)), end=", ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


print(currency_rates("uSd"))
print(currency_rates("EUR"))

# 4------------------------------------------------------------
from datetime import date
from requests import get, utils

res = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp."))


def currency_rates(code):
    content = res.split("Valute ID=")
    d, m, y = content[0].split()[3].split("Date=")[1][1:-1].split(".")

    for i in content:
        if code.upper() in i:
            print(date(year=int(y), month=int(m), day=int(d)), end=", ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


print(currency_rates("uSd"))
print(currency_rates("EUR"))

import utils

print(utils.currency_rates("CNY"))

# 5--------------------------------------------

from datetime import date
from requests import get, utils
from sys import argv

res = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp."))


def currency_rates(code):
    content = res.split("Valute ID=")
    d, m, y = content[0].split()[3].split("Date=")[1][1:-1].split(".")

    for i in content:
        if code.upper() in i:
            print(date(year=int(y), month=int(m), day=int(d)), end=", ")
            return float(i.replace("/", "").split("<Value>")[-2].replace(",", "."))


if __name__ == "__maim__":
    word = argv[1]
print(currency_rates(word))
