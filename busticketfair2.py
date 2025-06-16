print("Welcome to Sajha Yatayat")
print("We provide the best deals of bus travels in Nepal. So, where do you want to go this vacation")
print("The followinf routes from Kathmandu are as folows:")
print("1. Butwal = Rs 800")
print("2. Pokhara = Rs 700")
print("3. Chitwan = Rs 600")
print("4. Bhairahawa = Rs 900")
choice = int(input("Enter your choice(1,2,3,4):"))
num_tickets = int(input("Enter the number of tickets:"))
# Determine fare based on choice
if choice == 1:
    cost_per_ticket= 800
elif choice == 2:
    cost_per_ticket= 700
elif choice == 3:
    cost_per_ticket= 600
elif choice == 4:
    cost_per_ticket= 900
else:
    print("Invalid format choose number from 1 to 4")
# To calculate total fare
total_fare= cost_per_ticket * num_tickets
# Display the result
print(f"\nYour total bus fare is: Rs. {total_fare}")