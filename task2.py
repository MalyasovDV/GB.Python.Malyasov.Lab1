def sumOfDigits(number):
    sum = 0
    while(number > 0):
        sum += number % 10
        number //= 10
    return sum

number = int(input()) 
print(sumOfDigits(number))