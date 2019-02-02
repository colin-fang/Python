##
'''
Colin Fang
Program for Comp Sci 1026 Assignment 1
Computes and displays information for a company which rents vehicles to its customers
5/12/2018
'''
import math #using the math.ceil function

print("Please fill in the following:") #prompt user to fill in inputs

#variable declaration and initiation as the user inputted values
name = input("Customer's name: ")
age = int(input("Customer's age: "))
code = input("Customer's classification code: ")
numDays = int(input("Number of days the vehicle was rented: "))
odoStart = int(input("The vehicle's odometer reading at the start of the rental period: "))
odoEnd = int(input("The vehicle's odometer reading at the end of the rental period: "))

#variables for kilometers driven during rental period
#and the amount of money billed to the customer for the rental period
kilo = odoEnd - odoStart
kiloCalc = 0                                    #value of kliometers used for calculation of bill total
kiloAvg = kilo/numDays
kiloMulti = 0                                   #multiplier for kilometers driven
dayMulti = 0                                    #multiplier for days rented
numWeeks = math.ceil(float(numDays)/7)          #number of weeks rounded up
weekMulti = 0                                   #multiplier for weeks rented
dolla = 0                                       #final billed value

#if statements for calculating the multiplier variables
if (code == "B" or code == "b"):
    dayMulti = 20                               #$20.00 per day
    kiloMulti = .30                             #$0.30 per kilometer
    kiloCalc = kilo
elif (code == "D" or code == "d"):
    dayMulti = 50                               #$50.00 per day
    if(kiloAvg <= 100):
        kiloMulti = 0                           #$0 per kilometer
    elif(kiloAvg > 100):
        kiloAvg = kiloAvg - 100                 #calculation for exceeded kilometer average
        kiloCalc = kiloAvg*numDays              #kilometer value used for final calculation is derived from this and is distinct from kilo
        kiloMulti = .30                         #$0.30 per daily average kilometer exceeded
elif (code == "W" or code == "w"):
    weekMulti = 200                             #$200.00 per week
    if (kiloAvg <= 1000/7):                     #Daily average kilometer multiplied by 7 to get weekly average kilometer
        kiloMulti = 0                           #$0.00 per week
    elif (1000/7 < kiloAvg <= 2000/7):
        weekMulti = weekMulti + 50              #Additional $50.00 per week, Total $250.00 per week
    elif (kiloAvg > 2000/7):
        weekMulti = weekMulti + 100             #Additional $100.00 per week, Total $300.00 per week
        kiloAvg = (kiloAvg-2000/7)              #Calculation for exceeded weekly kilometer average
        kiloCalc = kiloAvg*7*numWeeks           #kilometer value used for final calculation is derived from this and is distinct from kilo
        kiloMulti = .30                         #$0.30 for each average kilo exceeding 2000 kilo
else:
    #invalid class code case:
    print("Sorry that is not a valid classification code \n"
          "The valid classification codes are: \n"
          "'B' or 'b' for budget plan \n"
          "'D' or 'd' for daily plan \n"
          "'W' or 'w' for weekly plan \n")
    exit()
#end of if

#if statement for age fee
if (age<25):
    dayMulti = dayMulti + 10
#end of if

#calculation of dolla aka total value billed
#convert int to float, round to 2 decimal places, formatted to have commas between zeroes
# and round to 2 decimal places or fill in zeroes to 2 decimal places (found online)
dolla = str('${:,.2f}'.format(round(float(dayMulti*numDays + weekMulti*numWeeks + kiloCalc*kiloMulti),2)))

#print functions for displaying summary
#looks a bit messy but was unable to successfully print altogether in one 'print()' function
print( "customer's name: ")
print(name)
print("customer's age: ")
print(age)
print("customer's classification code: ")
print(code)
print("number of days the vehicle was rented: ")
print(numDays)
print("vehicle's odometer reading at the start of the rental period: ")
print(odoStart)
print("vehicle's odometer reading at the end of the rental period: ")
print(odoEnd)
print("number of kilometers driven during the rental period: ")
print(kilo)
print("amount of money billed to the customer for the rental period: ")
print(dolla)
#end of program Press run to repeat
