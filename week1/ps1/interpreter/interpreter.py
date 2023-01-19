expression = str(input("What's the expression? ").lower())

x, y, z = expression.split(" ")

first = float(x)
third = float(z)

match y:
    case "+":
        answer = first + third
    case "-":
        answer = first - third
    case "*":
        answer = first * third
    case "/":
        answer = first / third

print(round(answer, 1))