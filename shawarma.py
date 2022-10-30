print("Nolan's Shawarma Palace")


print(
    "\n"
    + "\t" * 3
    + "MENU"
    + "\n" * 2
    + "-" * 50
    + "\n"
    + "\t" * 5
    + " |(Sml)"
    + "\t" * 2
    + "|(Med)"
    + "\t"
    + "    |(Lrg)"
    + "\n"
    + "-" * 50
    + "\n"
    "Shawarma plate"
    + "\t" * 4
    + " |$5.00"
    + "\t" * 2
    + "|$7.50"
    + "\t" * 2
    + "|$10.00"
    + "\n"
    + "-" * 50
    + "\n"
    "Meat-free Shawarma Wrap"
    + "\t" * 3
    + " |$5.75"
    + "\t" * 2
    + "|$8.63"
    + "\t" * 2
    + "|$11.50"
    + "\n"
    + "-" * 50
    + "\n"
    "Chicken Shawarma Wrap"
    + "\t" * 3
    + " |$6.50"
    + "\t" * 2
    + "|$9.75"
    + "\t" * 2
    + "|$13.00"
    + "\n"
    + "-" * 50
    + "\n"
    "Drink           "
    + "\t" * 3
    + " |$1.50"
    + "\t" * 2
    + "|$3.00"
    + "\t" * 2
    + "|$4.50"
    + "\n" * 2
)


str_name1 = input("What did you order? ")
str_cost1 = input("How much did it cost? ")
str_quantity1 = input(
    "How many did you buy? "
)
print("\n")

str_name2 = input("What else did you order? ")
str_cost2 = input("How much did it cost? ")
str_quantity2 = input(
    "How many did you buy? "
)  
print("\n")


flt_subtotal1 = float(str_cost1) * float(
    str_quantity1
)
flt_subtotal2 = float(str_cost2) * float(
    str_quantity2
)
flt_subtotal = (
    flt_subtotal1 + flt_subtotal2 
)
flt_tax = flt_subtotal * 0.13
flt_total = flt_subtotal + flt_tax


flt_cash = input("\n" + "How much cash do you have? ")
flt_cash = float(flt_cash)
flt_change = flt_cash - flt_total


print("\n" * 2 + "The total cost is " + "${:.2f}".format(flt_total))
input("Here is your reciept! (Press Enter to see your reciept) ")

print(
    "\n" * 3
    + "\t" * 4
    + "-" * 26
    + "\n"
    + "\n"
    + "\t" * 5
    + "   Nolan's Shawarma Palace"
    + "\n"
    + "\t" * 4
    + "    140 main St"
    + "\n"
    + "\t" * 5
    + "   Ottawa, ON"
    + "\n" * 2
    + "\t" * 4
    + "29/10/22"
    + "\t" * 3
    + " 6:01"
    + "\n" * 2
    + "\t" * 4
    + "QTY"
    + "\t" * 2
    + "ITEM"
    + "\t" * 2
    + " TOTAL"
    + "\n"
    + "\n"
    + "\t" * 4
    + str(str_quantity1)
    + "\t" * 2
    + str(str_name1)
    + "\t" * 2
    + " "
    + "${:.2f}".format(flt_subtotal1)
    + "\n"
    + "\t" * 4
    + str(str_quantity2)
    + "\t" * 2
    + str(str_name2)
    + "\t"
    + " "
    + "${:.2f}".format(flt_subtotal2)
    + "\n"
    + "\n"
    + "\t" * 4
    + "Subtotal"
    + "\t" * 3
    + "${:.2f}".format(flt_subtotal)
    + "\n"
    + "\t" * 4
    + "HST"
    + "\t" * 5
    + "$ "
    + "{:.2f}".format(flt_tax)
    + "\n"
)
print(
    "\t" * 4
    + "Total"
    + "\t" * 4
    + "${:.2f}".format(flt_total)
    + "\n"
    + "\t" * 4
    + "Cash"
    + "\t" * 4
    + "${:.2f}".format(flt_cash)
    + "\n"
    + "\t" * 4
    + "Change"
    + "\t" * 4
    + "${:.2f}".format(flt_change)
    + "\n"
    + "\n"
    + "\t" * 3
    + "Thank you for shopping at Nolan's Shawarma Palace!"
    + "\n" * 2
    + "\t"
    + " Take our survey at www.Nolan'sShawarmaPalace.ca for a free shawarma of your choice!"
    + "\n"
    + "\n"
    + "\t" * 4
    + "-" * 26
)