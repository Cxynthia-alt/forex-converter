from forex_python.converter import CurrencyCodes, CurrencyRates, RatesNotAvailableError


class CurrencyConverter:
    @staticmethod
    def get_symbol(target_currency):
        return CurrencyCodes().get_symbol(target_currency)

    @staticmethod
    def convert(source_currency, target_currency, amount):
        return CurrencyRates().convert(source_currency, target_currency, amount)

    @staticmethod
    def validate(currency):
        result = CurrencyCodes().get_currency_name(currency)
        if result is None:
            return f"{currency} is not a valid currency"
        return result
