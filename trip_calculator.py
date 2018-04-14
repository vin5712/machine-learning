# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 04:38:04 2018

@author: vinut
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 00:36:38 2018

@author: Vinay Murthy
"""
#This code has been derived from codecademy which is an online platform for learning Python


print ("Welcome to trip calculator")
print ("How long?,Nights")
nights = int(input())# This allows the user to input how many nights to stay
def hotel_cost(nights): # This function takes the user input--nights and calculates the cost
  return 140 * nights

city= ["Charlotte",  "Chicago", "Pittsburgh", "Los Angeles"]# List of cities 
print ("Choose from cities",city)    
print ("Which city?")
city = input() # for the user to input the city name after the cities are displayed
def plane_ride_cost(city): # defines the plane costs for the city chosen from the list
  if city == "Charlotte":          
    return (183)
  elif city == "Chicago":
    return (220)
  elif city == "Pittsburgh":
    return (222)
  elif city == "Los Angeles":
    return (475)

print ("How many days do you need the rental car for?")
days = int(input()) # User inputs the number of days they need the rental car
def rental_car_cost(days):
  cost = days * 40
  if days >= 7:# If user inputs 7 or more days they get a discount of 50
    cost -= 50
  elif days >= 3:# If user inputs >=3 days they get a discount of 20
    cost -= 20
    
  return (cost)

print ("Other costs?")
spendingmoney= int(input())# For the user to input other costs 

print ('trip_cost of %s, with  %d days of car rental and %d dollars of other costs is' %(city,days,spendingmoney))

def trip_cost():# defines the total trip cost which is an addition of all the functions above
  return (rental_car_cost(days)) + (hotel_cost(nights)) + (plane_ride_cost(city)) 
+(spendingmoney)

print (trip_cost()) # Fucntion called 



