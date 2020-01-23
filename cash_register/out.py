isdollar_out = ""
isdime_out = False
isquater_out = False
isnickel_out = False
ispenny_out= False

while isdollar_out(True) and int(change) < 10:
       reminder = int(change)%25
       Quaters = str((int(int(change)/25).__floordiv__(1)))
       print("No of Quaters : " + Quaters)

while isquater_out(True) and int(change) < 5:
       Dimes = str(int(reminder / 10).__floordiv__(1))
       reminder = reminder % 10
       print("No of Dime : " + Dimes)