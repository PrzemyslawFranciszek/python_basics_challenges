from random import randint

def coin_flip():
    """returns a result of flip a coin heads or tails string"""
    if randint(0,1) == 0:
        return "heads"
    else:
        return "tails"

flips = 0
num_trials = 10000

for trial in range(num_trials):
    first_flip = coin_flip()
    flips = flips + 1
    while coin_flip() == first_flip:
        flips = flips + 1
    flips = flips + 1
avg = flips / num_trials
print(avg)
