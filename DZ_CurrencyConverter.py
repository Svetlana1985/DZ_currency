# from DZ_decorate import requires_permission
class CheckCode:
    def __get__(self, instance, owner):
        return instance.__dict__['code']

    def __set__(self, instance, code_currency):
        if not (isinstance(code_currency, str) and len(code_currency) == 3 and code_currency.isupper()):
            raise ValueError(f'Код {code_currency} должен состоять из 3-х заглавных букв')
        instance.__dict__['code'] = code_currency


class Currency():
    code = CheckCode()
    def __init__(self, code_currency: str, rate: float):

        self.code = code_currency
        self.__rate = rate
        self.set_rate = rate

    @property
    def get_rate(self):
        return self.__rate

    @get_rate.setter
    def set_rate(self, new_rate: float):
        Currency.correct_currency(new_rate)
        self.__rate = new_rate

    @staticmethod
    def correct_currency(rate):
        if rate <= 0:
            raise ValueError(f'Значение {rate} должно быть положительным')

class CurrencyConvert:
    def convert(self, currency_from: Currency, currency_to: Currency, amount: float):
        if amount <= 0:
            raise ValueError(f'Значение {amount} должно быть положительным')
        usd_amount = amount / currency_from.get_rate
        converted_amount = usd_amount * currency_to.get_rate

        return converted_amount

eur = Currency('EUR', 0.947)
rub = Currency('RUB', 99.42)
usd = Currency('USD', 1)
converter = CurrencyConvert()
amount_eur = converter.convert(rub, eur,  100)
print(f"100 RUB to EUR: {amount_eur:.3f}")


