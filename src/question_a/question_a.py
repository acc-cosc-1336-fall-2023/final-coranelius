class Stock:
    def __init__(self, symbol, company_name):
        self.symbol = symbol
        self.company_name = company_name

    def get_symbol(self):
        return self.symbol

    def get_company_name(self):
        return self.company_name


def get_stock_list():
    stock_dict = {}
    with open('stock_file.dat', 'r') as file:
        next(file)  
       
        for line in file:
            symbol, company_name = line.strip().split(' ', 1)
            stock_dict[symbol] = Stock(symbol, company_name)
    return stock_dict