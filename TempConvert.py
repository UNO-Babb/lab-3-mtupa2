#TempConvert.py
#Name:
#Date:
#Assignment:

def word_to_number(words):
    number_words = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
        'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
        'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
        'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80,
        'ninety': 90, 'hundred': 100
    }

    words = words.lower().replace(" and ", " ").strip()
    if "point" in words:
        whole, decimal = words.split("point")
        decimal_words = decimal.strip().split()
    else:
        whole = words
        decimal_words = []

    whole_words = whole.strip().split()
    total = 0
    current = 0

    for word in whole_words:
        if word == "hundred":
            current *= 100
        elif word in number_words:
            current += number_words[word]
        else:
            raise ValueError(f"Unrecognized word: {word}")

    total += current

    # Handle decimal part
    if decimal_words:
        decimal_str = ""
        for d in decimal_words:
            if d in number_words and number_words[d] < 10:
                decimal_str += str(number_words[d])
            else:
                raise ValueError(f"Invalid decimal word: {d}")
        return float(f"{total}.{decimal_str}")
    else:
        return float(total)


def main():
    try:
        # 1. Prompt user to enter a word value of a temperature in Fahrenheit
        fahrenheit = input("Enter the temperature in Fahrenheit (in words): ")

        # 2. Convert the temperature to a number with only one decimal
        fahrenheit_number = round(word_to_number(fahrenheit), 1)

        # 3. Convert Fahrenheit to Celsius
        celsius = (fahrenheit_number - 32) * 5 / 9

        # 4. Round Celsius to one decimal place
        celsius_rounded = round(celsius, 1)

        # 5. Print both values
        print(f"The Fahrenheit value is {fahrenheit_number}°F and the Celsius value is {celsius_rounded}°C.")

    except ValueError as e:
        print("Error:", e)
        print("Please enter a number in words, like 'seventy two', 'one hundred and five', or 'eighty point five'.")

# Run the program
main()
