from forex_python.converter import CurrencyCodes, CurrencyRates, RatesNotAvailableError


class CurrencyConverter:
    @staticmethod
    def get_symbol(target_currency):
        return CurrencyCodes().get_symbol(target_currency)

    @staticmethod
    def convert(source_currency, target_currency, amount):
        return CurrencyRates().convert(source_currency, target_currency, amount)
