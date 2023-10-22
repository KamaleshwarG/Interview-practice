def calculate_total_profit(n, income_table):
    middle_row_product = 1
    middle_column_product = 1

    middle_row = n//2
    middle_column = n//2

    for i in range(n):
        middle_row_product *= income_table[middle_row][i]
        
        middle_column_product *= income_table[i][middle_column]

    total_profit = middle_row_product + middle_column_product

    total_profit = str(total_profit)[::-1]

    for i in total_profit:
        if(i == "0"):
            total_profit = total_profit[1:]
    

    return total_profit


def main():

    n= int(input("Enter the number of  cells:"))
    income_table = []
    for i in range(n):
        row = list(map(int , input(f"Enter row {i} values:").split()))
        income_table.append(row)
    print(calculate_total_profit(n , income_table))

if __name__ == "__main__":
    main()