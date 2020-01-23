from tax_cal import total
cash=float(input("Enter or insert Bill : "))
Change = str(float((cash)-float((total)).__round__(2)).__round__(2))
change = str(float(Change).__round__(2)).split(".")[1]
bill=str(float(Change).__round__(2)).split(".")[0]
print("Total change :" + Change)
print("Change in Bills : " + bill)
print("Change in coins : " + change)
