
def find_max_product(days , products , sales_record):

        max_product_each_day = []

        for i in range(days):
             max_product = max(sales_record[i])
             max_product_each_day.append(max_product)

        return max_product_each_day

days , products = map(int, input("Enter no of days  and products").split())
sales_record = []

for i in range(days):
    sales_per_day = list(map(int , input("Enter the products sales").split()))
    if(len(sales_per_day) == products):
        sales_record.append(sales_per_day)

result = find_max_product(days , products , sales_record)

print("The maximum saled product each day is :" , result)