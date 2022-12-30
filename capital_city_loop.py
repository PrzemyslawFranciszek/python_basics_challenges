import random
capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phonix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}
def rand_capital():
    """Return random key with its value from dictionary"""
    empty_list = []
    for state in capitals_dict:
        #Create a list of keys from dictionary
        empty_list.append(state)
    #Randomly choices a key from list 
    rand_state = random.choice(empty_list)
    #Assign value from choiced key
    rand_capital = capitals_dict[rand_state]
    return rand_state, rand_capital
#assignment for state and capital to tuple
drawned_pair = rand_capital()
while True:
    #inifinite loop
    guess = ""
    guess = input(f"Please enter the capital of the {drawned_pair[0]}:\n")
    if guess.lower() == drawned_pair[1].lower():
        print("Correct")
        break
    elif guess.lower() == "exit":
        print(f"The answer was {drawned_pair[1]}. Goodbye.")
        break
    
