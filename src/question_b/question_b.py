class Stock:
    def __init__(self, symbol, company_name):
        self._symbol = symbol
        self._company_name = company_name

    def get_symbol(self):
        return self._symbol

    def get_company_name(self):
        return self._company_name


def stock_purchase_history():
    aapl = Stock("AAPL", "Apple Inc")
    cat = Stock("CAT", "Caterpillar")
    ek = Stock("EK", "Eastman Kodak")
    goog = Stock("GOOG", "Google")
    msft = Stock("MSFT", "Microsoft")

    stock_dict = {
        aapl.get_symbol(): aapl,
        cat.get_symbol(): cat,
        ek.get_symbol(): ek,
        goog.get_symbol(): goog,
        msft.get_symbol(): msft
    }

    print("Stock Purchase History:")
    print(f"{'Symbol':<10} {'Company Name':<20}")
    for symbol, stock in stock_dict.items():
        print(f"{symbol:<10} {stock.get_company_name():<20}")