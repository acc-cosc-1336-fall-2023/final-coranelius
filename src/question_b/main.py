from question_b import stock_purchase_history


def main():
    while True:
        print("\nMenu:")
        print("1- Display your stock purchase history")
        print("2- Exit")

        option = input("Which option would you like to choose?: ")

        if option == '1':
            stock_purchase_history()
        elif option == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()