import tkinter as tk
from base_GUI_ttinker import BaseGui
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


class Currency_GUI(BaseGui):
    def __init__(self, master=None):
        # BaseGui.__init__(self, master)
        super().__init__(master)

        self.title("Currency Converter GUI")
        self.current_converter_get = currency_Converter_get()

        #! Validate entry
        validate_entry_cmd = self.register(self.validate_entry)


        self.currency_frame = tk.Frame(self)
        self.currency_frame.pack(padx=50, pady=50)

        self.gui_name = tk.Label(self.currency_frame, text="Currency Converter")
        self.gui_name.pack()

        self.currency_one_label = tk.Label(self.currency_frame, text="Currency 1")
        self.currency_one_label.pack()

        self.currency_one_entry = tk.Entry(self.currency_frame)
        self.currency_one_entry.pack()
        #! add validate command to the entry
        self.currency_one_entry.config(validate="key", validatecommand=(validate_entry_cmd, '%P'))

        self.currency_two_label = tk.Label(self.currency_frame, text="Currency 2")
        self.currency_two_label.pack()

        self.currency_two_entry = tk.Entry(self.currency_frame)
        self.currency_two_entry.pack()
        self.currency_two_entry.config(validate="key", validatecommand=(validate_entry_cmd, '%P'))

        self.amount_label = tk.Label(self.currency_frame, text="Amount")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(self.currency_frame)
        self.amount_entry.pack()

        self.result_label = tk.Label(self.currency_frame, text="")
        self.result_label.pack()

        self.convert_button = tk.Button(
            self, text="Convert", command=self.convert_currency
        )
        self.convert_button.pack()

    def validate_entry(self,P):
        return len(P) <= 3
        
    def convert_currency(self):
        data = (
            self.current_converter_get.get_exchange_rate_data()[0]["rates"]
            + self.current_converter_get.get_exchange_rate_data()[1]["rates"]
        )
        time = self.current_converter_get.get_exchange_rate_data()[0]["effectiveDate"]

        currency1 = self.currency_one_entry.get().upper()
        currency2 = self.currency_two_entry.get().upper()
        
        if self.amount_entry.get() == "":
            self.result_label.config(text="Amount cannot be empty")
            return
        
        amount = float(self.amount_entry.get())

        code_list=[]
        for code in data:
            code_list.append(code["code"])

        if currency1 not in code_list:
            self.result_label.config(text=f"{currency1} is not a valid currency code")
            return
        
        if currency2 not in code_list:
            self.result_label.config(text=f"{currency2} is not a valid currency code")
            return
        
        #print(code_list)
        
        if amount < 0:
            self.result_label.config(text="Amount must be greater than 0")
            return
        
        converted_amount = self.current_converter_get.convert_currency(amount, currency1, currency2)

        self.result_label.config(text=f"{amount} {currency1} = {converted_amount:.2f} {currency2} at {time}")


if __name__ == "__main__":
    root = tk.Tk()
    currency_window = Currency_GUI(root)
    root.withdraw()  # Hide the main Tkinter window
    currency_window.show()
