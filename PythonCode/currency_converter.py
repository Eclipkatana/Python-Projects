
from requests import get
from pprint import PrettyPrinter


class currency_Converter_get:
    def __init__(self):
        self.base_url = "http://api.nbp.pl/api/"
        self.format = "?format=json"
        self.currency_rate_url = "exchangerates/tables/"
        self.printer = PrettyPrinter()

    def get_exchange_rate_data(self):
        data = []
        url1 = self.base_url + self.currency_rate_url + "A" + self.format
        url2 = self.base_url + self.currency_rate_url + "B" + self.format
        # url3 = base_url + exchange_rate+"C"+format
        data1 = get(url1).json()
        data2 = get(url2).json()
        # data3=get(url3).json()[0]['rates']
        data = data1 + data2
        # print(url1)
        # printer.pprint(data)
        return data

    def print_currency(datas):
        for data in datas:
            print(f'{data["code"]} - {data["currency"]} - {data["mid"]}')

    #! this function must include self as the first argument
    def exchange_rate(self, currency1, currency2):
        data_list = (
            self.get_exchange_rate_data()[0]["rates"] + self.get_exchange_rate_data()[1]["rates"]
        )
        for data in data_list:
            if data["code"] == currency1:
                rate1 = data["mid"]
            if data["code"] == currency2:
                rate2 = data["mid"]

        return rate1 / rate2

    def convert_currency(self, amount, currency1, currency2):
        rate = self.exchange_rate(currency1, currency2)
        return amount * rate