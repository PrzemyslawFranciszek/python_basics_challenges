universities = [
    ['California Institute of Technology', 2175 , 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology' , 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 19535, 40569],
    ['Yale', 11701, 40500]
]

enrollment_values = []
tuition_fees = []
def enrollment_stats(item):
    """Return 2 lists: first all student enrollment values and second all the tuition fees"""
    
    for item_in_list in item:
        
        enrollment_values.append(item_in_list[1])
    
        # append values to empty list 
#    print(item[1])
#    print([item_in_list for item_in_list in item])

enrollment_stats(universities)
print(enrollment_values)

# enrollment_stats(universities)
