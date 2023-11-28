#asking user for salary and years of service
salary=float(input("enter your salary:"))
years_of_service=int(input("enter your years of service:"))
 
 #calculating bonus based on years of service
 if years_of_service>10:
     bonus_percentage=0.10
elif 6<=years_of_service<=10:
    bonus_percentage=0.08
else:
    bonus_percentage=0.05
    
#calculating bonus amount
bonus_amount=salary*bonus_percentage

#printing the net bonus bonus amount
print("your bonus amount is:+ str(bonus_amount))
