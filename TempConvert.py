#TempConvert.py
#Name:
#Date:
#Assignment:


def main():

# 1. Prompt user to enter a word value of a temperature in Fahrenheit
fahrenheit = input("Enter the temperature in Fahrenheit (in words): ")

from word2number import w2n

# 2. Convert the temperature to a number with only one decimal
fahrenheit_number = round(float(w2n.word_to_num(fahrenheit)), 1)

# 3. Convert Fahrenheit to Celsius
celsius = (fahrenheit_number - 32) * 5 / 9

# 4. Round Celsius to one decimal place
celsius_rounded = round(celsius, 1)

# 5. Print both values
print(f"The Fahrenheit value is {fahrenheit_number}°F and the Celsius value is {celsius_rounded}°C.")

except ValueError:
print("Sorry, I couldn't understand that temperature. Please enter a number in words, like 'seventy two'.")

  



