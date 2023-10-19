def first_meat_pizza_order(orderPlaced_size , orders , size):

    result = []
    first_negative = 0

    for i in range(orderPlaced_size):
        display = orders[i : i+size]

        if(len(display) != size):
            break
        else:
            for meat in display:
                if meat < 0:
                    first_negative = meat
                    break
                else:
                    first_negative = 0

            result.append(first_negative)

    return result


orderPlaced_size = int(input("Enter no of orders:"))
orders = list(map(int,input("Enter the pizza values:").split()))
size = int(input("Enter the display window size:"))

result = first_meat_pizza_order(orderPlaced_size,orders,size)

print("The first negative order of each display of size {0} is: {1}" .format(size , result) )