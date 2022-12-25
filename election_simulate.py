from random import random
win_a_counter = 0
win_b_counter = 0
flips = 10_000

for trial in range(flips):

    win_a_region = 0
    win_b_region = 0

    # counts which candidate win in 1 region
    if random() > 0.87:
        win_b_region = win_b_region + 1
    else:
        win_a_region = win_a_region + 1
    # counts which candidate win in 2 region
    if random() > 0.65:
        win_b_region = win_b_region + 1
    else:
        win_a_region = win_a_region + 1
    # counts which candidate win in 3 region
    if random() > 0.17:
        win_b_region = win_b_region + 1
    else:
        win_a_region = win_a_region + 1
    # counts which candidate win election in a flip
    if (win_a_region > win_b_region):
        win_a_counter = win_a_counter + 1
    else:
        win_b_counter = win_b_counter + 1


result_of_voting_a = win_a_counter / flips
result_of_voting_b = win_b_counter / flips

print(f"% of winning election A {result_of_voting_a:.1%}")
print(f"% of winning election B {result_of_voting_b:.1%}")
