units_consumed = int(input("Enter the units consumed:"))

total_charge = 0

if(units_consumed <= 50):
    total_charge = units_consumed * 0.5
elif(units_consumed <= 150):
    total_charge = ((units_consumed - 50) * 0.75) + 50 * 0.50
elif(units_consumed <= 250):
    total_charge = ((units_consumed - 150) * 1.20) + (100 * 0.75) + (50 * 0.5) 
else:
    total_charge = ((units_consumed - 250) * 1.50) + (100 * 1.20) + (100 * 0.75) + (50 * 0.5)

total_charge = total_charge + (total_charge*0.20)

print(f"The total price for {units_consumed} units is : {total_charge:.2f}")