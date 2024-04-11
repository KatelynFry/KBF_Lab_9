def decoder(enc):
    dec = ""
    for digit in enc:
        decoded_digit = str((int(digit) - 3) % 10)
        dec += decoded_digit
    return dec