from question_c import create_multiplication_table, display_multiplication_table

while True:
    multiplication_table = create_multiplication_table()
    display_multiplication_table(multiplication_table)
    
    user_choice = input("Would you like to continue? (yes/no): ").lower()
    if user_choice != 'yes':
        break