
def sum_of_digits(number):
    # Initialize sum to 0
    sum = 0

    # Convert number to absolute value to handle negative numbers
    number = abs(number)

    # Iterate through each digit in the number
    while number > 0:
        # Add the last digit (remainder when divided by 10) to sum
        sum += number % 10

        # Remove the last digit from number
        number = number // 10

    return sum

print(f"sum of digits of {num} is:{sum_of_didgits(num)}")









