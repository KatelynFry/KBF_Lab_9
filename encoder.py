# encoder function
# Made by Katelyn Fry
def encoder(num):
    enc = ""
    for i in num:
        # I have added the % 10 to use the remainder so that there isn't an increase in digits added to the string
        enc += str((int(i)+3) % 10)
    return enc
