from CurrencyConverterUI_ui import Ui_Form
import sys

sys.path.append(
    r"C:\Users\bibon\OneDrive\Desktop\Git\Python\Python-Projects\PythonCode"
)
from currency_converter import currency_Converter_get

from PySide6.QtWidgets import QApplication, QWidget


class Currency_Converter_UI(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Currency Converter")

        self.currency_converter = currency_Converter_get()

        self.convert_button.clicked.connect(self.currency_exchange)

    def currency_exchange(self):
        currency1 = self.currency1_input_text.text().upper()
        currency2 = self.currency2_input_text.text().upper()
        amount = float(self.amount_input_text.text())

        data = (
            self.currency_converter.get_exchange_rate_data()[0]["rates"]
            + self.currency_converter.get_exchange_rate_data()[1]["rates"]
        )

        time = self.currency_converter.get_exchange_rate_data()[0]["effectiveDate"]

        if amount == "":
            self.output_label.setText("Amount can not be empty")

        code_list = []

        for code in data:
            code_list.append(code["code"])

        if currency1 not in code_list:
            self.output_label.setText(f"{currency1} is not valid")
            return

        if currency2 not in code_list:
            self.output_label.setText(f"{currency2} is not valid")
            return

        if amount < 0:
            self.output_label.setText("Amount can not be negative")
            return

        converted_amount = self.currency_converter.convert_currency(
            amount, currency1, currency2
        )

        self.output_label.setText(
            f"{amount} {currency1} is {converted_amount:.2f} {currency2} at {time}"
        )


if __name__ == "__main__":
    app = QApplication([])
    widget = Currency_Converter_UI()
    widget.show()
    app.exec()
