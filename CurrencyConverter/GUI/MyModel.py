import requests
import json

class MyModel():

    def get_cur(self, from_c, to_c, input):
        """
            Sie werden aufgefordert, eine Ziel und Ausgangwährung einzugeben, und wenn sie diese Bedingungen nicht erfüllen,
            werden Fehlermeldungen ausgegeben

            :param from_c: Ausgangswährung
            :param to_c: Zielwährung
            :param input:
            :return:
        """
        if (to_c == " "):
            return "Bitte geben Sie eine Zielwährung ein"
        if (from_c == " "):
            return "Bitte geben Sie eine Ausgangswährung ein"
        url = "https://api.exchangeratesapi.io/latest"
        params = {"base": from_c,
                  "symbols": to_c
                  }
        resp = requests.get(url, params=params)

        try:

            if resp.status_code != 200:
                raise ValueError(output.format(resp.status_code))

            output = resp.json()
        except:
            return ("Ausgangswährung oder Zielwährung ungültig")
        ausgabe = "<b> " + str(input) + " " + from_c + " </b> entsprechen: <br>"

        cur = output['rates']
        for key in cur.keys():
            neuerWert = input * output['rates'][key]

            ausgabe += " <ul> <li><b>" + str(round(neuerWert, 2)) + " " + str(key) + "</b> (Kurs: " + str(
                output['rates'][key]) + ") </li></ul>"
        ausgabe += "<br> Stand: " + str(output['date'])
        return ausgabe

    def get_cur_offline(self, from_c, to_c, input):

        if (to_c == ""):
            return "Bitte geben Sie eine Zielwährung ein"

        if (from_c == " "):
            return "Bitte geben Sie eine Ausgangswährung ein"

        if (from_c != "EUR"):
            return "Sie können nur EUR als Ausgangswährung angeben!"

        au = {'rates': {'CAD': 1.4426, 'HKD': 8.5368, 'ISK': 135.1, 'PHP': 56.553, 'DKK': 7.4662, 'HUF': 334.83,
                        'CZK': 25.816, 'AUD': 1.6126, 'RON': 4.7496, 'SEK': 10.6958, 'IDR': 15456.94, 'INR': 77.1615,
                        'BRL': 4.5288, 'RUB': 70.7557, 'HRK': 7.411, 'JPY': 117.59, 'THB': 33.315, 'CHF': 1.0847,
                        'SGD': 1.506, 'PLN': 4.3782, 'BGN': 1.9558, 'TRY': 6.1491, 'CNY': 7.7784, 'NOK': 9.8953,
                        'NZD': 1.7375, 'ZAR': 16.5576, 'USD': 1.0889, 'MXN': 21.4522, 'ILS': 3.7877, 'GBP': 0.88573,
                        'KRW': 1304.83, 'MYR': 4.5592}, 'base': 'EUR', 'date': '2019-09-30'}
        ausgabe = ""

        aus = "<b> " + str(input) + " " + from_c + " </b> entsprechen: <br>"

        cur = au['rates']

        split = to_c.split(",")

        i = 0

        for key in cur.keys():
            for s in split:
                if (s == key):
                    neuerWert = input * au['rates'][key]
                    ausgabe += " <ul> <li><b>" + str(round(neuerWert, 2)) + " " + str(key) + "</b> (Kurs: " + str(
                        au['rates'][key]) + ") </li></ul>"
                    i = i + 1

        ausgabe += "<br> Offline-Stand: " + str(au['date'])

        aus += ausgabe

        if (i == 0):
            return "Zielwährung ist fehlerhaft"

        return aus


