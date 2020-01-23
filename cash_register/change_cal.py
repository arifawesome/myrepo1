from change import change


while reminder != 0  and int(change) < 100:
       print("No of Quaters : " +  Quaters)
       Dimes = str(int(reminder/10).__floordiv__(1))
       reminder =reminder%10
       print("No of Dime : " + Dimes )
       if reminder != 0:
              Nickels = str(int(reminder / 5).__floordiv__(1))
              reminder = reminder % 5
              print("No of Nickels: " + Nickels)
              if reminder != 0:
                     Pennies = str(int(reminder / 1).__floordiv__(1))
                     reminder = reminder % 1
                     print("No of Pennies : " + Pennies)
              break
       break
else:
   print ("No Coins in change")
