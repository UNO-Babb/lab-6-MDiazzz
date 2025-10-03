#DiceRoll.py
#Name: Michelle Diaz
#Date: 9/30/2025
#Assignment: Dice Roll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls[(dice1+dice2)-1] = rolls[(dice1+dice2) -1] + 1

  #find the sum total of the two dice
   
  
  #print statictics for dice rolls
  dice = 1
  for count in rolls:
    print(dice, ":", count,":", (count/10000)*100)
    dice = dice + 1

if __name__ == '__main__':
  main()
