def get_input():
    input_number = input("Enter 3 digit or larger integer: ")
    return input_number

def get_divisor(num):
    num_to_str = str(num)
    first_digit = int(num_to_str[0])
    second_digit = (num % 10)
    div = (first_digit * 10) + second_digit
    return div

def check_for_gapful(num, div):
    if(num % div == 0):
        return True
    else:
        return False

number = get_input()
#check to see if user input is a gapful number
try:
   number = int(number)
   if(number > 100):
       divisor = get_divisor(number)
       if(check_for_gapful(number, divisor)):
           print("true: %s is gapful because it is divisible by %s" % (number, divisor))
       else:
           print("false: %s is not gapful because it is not divisible by %s" % (number, divisor))  
   else:
       print("Number is not at least 3 digits")
except ValueError:
   print("Input is not an integer")

