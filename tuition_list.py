universities = [
    ['California Institute of Technology', 2175 , 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology' , 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(item_in_outer_list):
    """Return 2 lists: first all student enrollment values and second all the tuition fees"""
    enrollment_values = []
    tuition_fees = []

    for item_in_inner_list in item_in_outer_list:
        
        # add to list value of single enrollment
        enrollment_values.append(item_in_inner_list[1])
        # add to list value of single tuition fee
        tuition_fees.append(item_in_inner_list[2])
    return enrollment_values, tuition_fees

def mean(mean_arg):
    """Returns the mean of numbers in list"""
    return round(sum(mean_arg)/len(mean_arg), 2)

def median(median_arg):
    """Returns the median of numbers in list"""
    median_arg.sort()
    list_length = len(median_arg)
    
    if list_length % 2 == 0:
        # if the number of values in list are even we have 2 median numbers
        indices = (list_length // 2)   
        return (median_arg[indices - 1] + median_arg[indices]) / 2
    else:
        # if the number of values in list are odd we have only one median number
        return median_arg[(list_length // 2)]

print(f"**************************\n"
      f"Total students:   {sum((enrollment_stats(universities)[0])):,}\n"
      f"Total tuition:  $ {sum((enrollment_stats(universities)[1])):,}\n\n"
      f"Student mean:     {mean((enrollment_stats(universities)[0])):,}\n"
      f"Student median:   {median(enrollment_stats(universities)[0]):,}\n\n"
      f"Tuition mean:   $ {mean(enrollment_stats(universities)[1]):,}\n"
      f"Tuition median: $ {median(enrollment_stats(universities)[1]):,}")

