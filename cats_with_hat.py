cats = {}

for cat in range(1,101):
    # add a 100 different cats to dictionary
    cats['#' + str(cat)] = ''

def every_cat():
    """loop over every cat to add or remove values in dict keys"""
    for cat, hat in cats.items():
        hat = check_for_hat(hat)
        cats[cat] = hat

def second_cat():
    """loop on second cat to add or remove values in dict keys"""
    cats_loop = 0
    for cat, hat in cats.items():
        cats_loop = cats_loop + 1
        if cats_loop % 2 == 0:
            hat = check_for_hat(hat)
            cats[cat] = hat

def third_cat():
    """loop on third cat to add or remove values in dict keys"""
    cats_loop = 0
    for cat, hat in cats.items():
        cats_loop = cats_loop + 1
        if cats_loop % 3 == 0:
            hat = check_for_hat(hat)
            cats[cat] = hat

def last_round():
    """changes value of the last key"""
    if cats['#100'] ==  'hat':
        cats['#100'] = ''
    else:
        cats['#100'] = 'hat'

def check_for_hat(hat):
    """"changes a hat variable"""
    if hat == 'hat':
        hat = ''
    else:
        hat = 'hat'
    return hat
def print_cat():
    """print cats which have hats"""
    for cat, hat in cats.items():
        if hat == 'hat':
            print(cat)

counter_round = 0
while True:
    if counter_round < 100:
        every_cat()
        counter_round  = counter_round + 1
        second_cat()
        counter_round  = counter_round + 1
        third_cat()
        counter_round  = counter_round + 1
    else:
        last_round()
        print_cat()
        break

