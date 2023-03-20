firstValue = "Python 2023"
secondValue = firstValue
thirdValue = secondValue

print(firstValue == secondValue)
print(secondValue == thirdValue)
print(type(firstValue), hex(id(firstValue)))
print(type(secondValue), hex(id(secondValue)))
print(type(thirdValue), hex(id(thirdValue)))

thirdValue = "Java 11"

print(firstValue == secondValue)
print(secondValue == thirdValue)
print(type(firstValue), hex(id(firstValue)))
print(type(secondValue), hex(id(secondValue)))
print(type(thirdValue), hex(id(thirdValue)))