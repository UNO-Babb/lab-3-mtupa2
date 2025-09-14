#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  TEMPF=input("Enter Value:")
  number_float = float(TEMPF)
  rounded_number = round(number_float, 1)
  print(f"The number rounded to one decimal place is: {rounded_number}")
  print("Invalid input. Please enter a valid number.")
  #Convert that temperature to celsius, rounding to 1 decimal percision
  celsius = (fahrenheit - 32) * 5/9

  #Output converted temperature.
  

  

  print(rounded_number, "is ", celsius, "degrees celsius.")
if __name__ == '__main__':
  main()
