





firtValue = (float(input("input first value -> ")))
operator = input("enter operation ->")
secondValue  =(float(input("input second value -> ")))




match operator:
    case "*":
        print(firtValue * secondValue)
    case  "/":
        print(firtValue/secondValue)
    case "+":
        print(firtValue + secondValue)
    case "-":
        print(firtValue-secondValue)
    case "^":
        print(firtValue**secondValue)