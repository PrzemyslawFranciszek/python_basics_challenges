cats = {}
for cat in range(1,101):
    # add a 100 different cats to dictionary
    cats['#' + str(cat)] = ''
counter = 0
def every_cat():
    """loop over every cat to add or remove values in dict keys"""
    for cat, hat in cats.items():
        hat = check_for_hat(hat)
        cats[cat] = hat

def second_cat():
    """loop on second cat to add or remove values in dict keys"""
    
##def third_cat():
##    

def check_for_hat(hat):
    """"changes a hat variable"""
    if hat == 'hat':
        hat = 'not hat'
    else:
        hat = 'hat'
    return hat


while True:
    every_cat()
    counter  = counter +1
    second_cat()
    counter  = counter +1
    third_cat()
    counter  = counter +1
    

    
