def convert_cel_to_far(temp_cel):
    """Function converts Celsius degrees to Farenheit degrees"""
    temp_far = temp_cel * 9/5 + 32
    return temp_far

temp_cel = input("Please input temperature in Celsius degrees: ")
temp_cel = float(temp_cel)
print(f"You entered {temp_cel} in Celsius degrees,"
      f" in Farenheit degrees it will be {convert_cel_to_far(temp_cel):.2f}")

def convert_far_to_cel(temp_far):
    """Function converts Farenheit degrees to Celsius degrees"""
    temp_cel = (temp_far - 32) * 5/9
    return temp_cel

temp_far = input("Please input temperature in Farenheit degrees: ")
temp_far = float(temp_far)
print(f"You entered {temp_far} in Farenheit degrees,"
      f" in Celsius degrees it will be {convert_far_to_cel(temp_far):.2f}")
