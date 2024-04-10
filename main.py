# Display Menu
# Made by Katelyn Fry
from encoder import *
while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    val = int(input("Please enter an option: "))
    if val == 1:
        num = input("Please enter your password to encode: ")
        enc = encoder(num)
        print("Your password has been encoded and stored!")
    if val == 2:
        print(f"The encoded password is {enc}, and the original password is {num}.")
    if val == 3:
        break
