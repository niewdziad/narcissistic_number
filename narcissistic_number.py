def narcissistic(test_number):
    num_str = str(test_number)
    num_digits = len(num_str)
    narcissistic_sum = sum(int(digit) ** num_digits for digit in num_str)
    return narcissistic_sum == test_number

print(narcissistic(7))     # True
print(narcissistic(371))   # True
print(narcissistic(122))   # False
print(narcissistic(4887))  # False