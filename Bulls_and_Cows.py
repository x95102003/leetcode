#! /usr/bin/python

def calc(secret, guess):
    A = 0
    B = 0
    secret = list(secret)
    guess = list(guess)
    for a,b in zip(secret, guess):
        if a == b:
            A += 1
            secret.remove(a)
            guess.remove(b)

    for a,b in zip(secret, guess):
        if a in guess:
            B += 1
            secret.remove(a)
            guess.remove(a)
        else:
            pass
    return "%dA%dB" %(A, B)

secret = "011"
guess = "110"
print calc(secret, guess)
            
