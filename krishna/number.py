def decimal_to_octal(decimal_number):

    octal_number =""
    while decimal_number > 0:
        remainder = decimal_number % 8
        decimal_number //= 8
        octal_number = str(remainder) + octal_number
    return octal_number


decimal_number = 1234
octal_number = decimal_to_octal(decimal_number)

print("The octal respresentation of {} is {}".format(decimal_number, octal_number))

