def calculator(number1, number2, operationType):
    if operationType == "+":
        answer = int(number1)+int(number2)
        return answer
    elif operationType == "-":
        answer = int(number1)-int(number2)
        return answer
    elif operationType == "*":
        answer = int(number1)*int(number2)
        return answer
    elif operationType == "/":
        answer = int(number1)/int(number2)
        return answer
    else:
        return None


def main():
    # write your code here
    valid = False
    while not valid:
        try:
            num1 = int(input("Enter the first number:"))
            num2 = int(input("Enter the second number:"))
            valid = True
        except ValueError:
            print("Number is not valid")

    operation1 = input("Choose the operation (+, -, /, *):")

    answer = calculator(num1, num2, operation1)
    if answer == None:
        print("Operation not valid")
    else:
        print("The answer is", str(answer))


if __name__ == '__main__':
    main()
