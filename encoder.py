# encoder function
# Made by Katelyn Fry
def encoder(num):
    enc = ""
    for i in num:
        enc += str((int(i)+3) % 10)
    return enc
