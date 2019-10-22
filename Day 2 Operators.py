import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    total=(1+0.01*(tip_percent+tax_percent))*meal_cost+0.5
    t=int(total)
    print("Total cost = "+str(t))

if __name__ == '__main__':
    meal_cost = float(input("Meal Cost : "))

    tip_percent = int(input("Tip percent : "))

    tax_percent = int(input("Tax percent : "))

    solve(meal_cost, tip_percent, tax_percent)
