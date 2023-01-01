cats = {}
for cat in range(1,101):
    # add a 100 different cats to dictionary
    cats['#' + str(cat)] = ''
counter_round = 0
def every_cat():
    """loop over every cat to add or remove values in dict keys"""
    for cat, hat in cats.items():
        hat = check_for_hat(hat)
        cats[cat] = hat

def second_cat():
    """loop on second cat to add or remove values in dict keys"""
    counter_loop = 0
    for cat, hat in cats.items():
        counter_loop = counter_loop + 1
        if counter_loop % 2 == 0:
            hat = check_for_hat(hat)
            cats[cat] = hat
def third_cat():
    """loop on third cat to add or remove values in dict keys"""
    counter_loop = 0
    for cat, hat in cats.items():
        counter_loop = counter_loop + 1
        if counter_loop % 3 == 0:
            hat = check_for_hat(hat)
            cats[cat] = hat
    print(cats)
##def last_round():

def check_for_hat(hat):
    """"changes a hat variable"""
    if hat == 'hat':
        hat = 'not hat'
    else:
        hat = 'hat'
    return hat


while True:
    every_cat()
    counter_round  = counter_round +1
    second_cat()
    counter_round  = counter_round +1
    third_cat()
    counter_round  = counter_round +1
    break
    

    
