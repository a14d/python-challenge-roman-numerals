def number_to_roman(number):
    """
    Convert a number to a Roman number.
    """
    output = []

    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    digits = ['M', 'CM', 'D', 'CD','C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    for i in range(len(numbers)):
        count = int(number / numbers[i])
        output.append(digits[i] * count)
        number -= numbers[i] * count
    
    return ''.join(output)