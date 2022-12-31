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

state, capital = random.choice(list(capitals_dict.items()))
#Randomly choiced state and capital
while True:
    guess = input(f"Please enter the capital of {state} :\n").lower()
    if guess == capital.lower():
        print("Correct")
        break
    elif guess == "exit":
        print(f"The answer was {capital}. Goodbye.")
        break
    
