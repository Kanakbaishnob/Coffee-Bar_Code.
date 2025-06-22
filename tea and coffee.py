print("Welcome to our Restaurant")
print("please Give Us Your Information.")

Name =input("Enter your Name: ")
table_no = (input("Enter Your Table No: "))
print(f"Thanks For Your Info {Name}.")
print("list of Item.")
print("Tea.")
print("Coffee.")
order= input("What is Order (Tea or Coffee): ")
order_confirmed = False

if order.lower().strip()=="tea":
    print("List of Tea.")
    print("1. Black Tea. (25$)")
    print("2. Green Tea.(40$)")
    print("3. Rainbow Tea. (45$)")
    Tea_order=input("What Tea You Want To Order: ").lower().strip()
    valid_tea=["black tea","green tea","rainbow tea"]
    if Tea_order in valid_tea:
        Tea_no=input("How many cap you want to order: ")
        print("Do You need extra suger?")
        suger=input("Yes or no: ").lower().strip()
        print("Your Order Is Confirmed.")
        print("\n Order Summary")  ###
        print(f"Tea Name: {Tea_order}")
        print(f"{Tea_no} cup of Tea")
        print(f"Extra suger: {suger}")
        order_confirmed = True
    else:
        print("Please Enter The valid Tea.")
elif order =="coffee":
    print("List of Coffee.")
    print("1. Black Coffee. (30$)")
    print("2. cuppuccino. (60$)")
    print("3. Turkish Coffee. (69$)")
    print("4. Espresso. (80$)")
    coffee_order = input("What Coffee You Want To Order: ").lower().strip()
    valid_coffee=["black coffee","cuppuccino","turkish coffee","espresso"]
    if coffee_order in valid_coffee:
        coffee_no=input("How many cap you want to order: ")
        print("Do You need extra suger?")
        suger=input("Yes or no: ")
        print("Your Order Is Confirmed.")
        print("\n Order Summary")
        print(f"Coffee Name: {coffee_order}")
        print(f"{coffee_no} cup of Tea")
        print(f"Extra suger: {suger}")
        order_confirmed = True
    else:
        print("Please Enter The Proper Coffee.")
else:
     print("please Choose Tea, Coffee of Cookies.")
if order_confirmed :
    print("Only for today, we are giving our customers a free cookie!")
    Cookies=input("Enter Yes Or No: ").lower().strip()
    print(f"Thank You Sir. Enjoy Your {order}")
else:
    print("Confirm Your Order.")