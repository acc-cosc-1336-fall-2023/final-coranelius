from question_a import get_stock_list

def display_stock_purchase_history(stocks):
    for symbol, stock in stocks.items():
        print(f"Symbol: {stock.get_symbol()}, Company: {stock.get_company_name()}")


def main():
    stocks = get_stock_list()
    while True:
        print("\nMenu:")
        print("1- Display your stock purchase history")
        print("2- Exit")
        option = input("Which option would you like to choose?: ")

        if option == '1':
            display_stock_purchase_history(stocks)
        elif option == '2':
            print("Exiting program.")
            break
        else:
            print("Option can not be chosen.")


if __name__ == "__main__":
    main()