def is_prime(*values):
    tmp = []
    print("Primes { ", end="")
    for num in values:
        if num < 2:
            tmp.append(False)
        elif num == 2:
            tmp.append(True)
            print(f" {num}  ",end="")
        elif num % 2 == 0:
            tmp.append(False)
        else:
            i = 3
            while i*i <= num:
                if num % i == 0:
                    tmp.append(False)
                    break
                i += 2
            else:
                tmp.append(True)
                print(f" {num}  ",end="")
    print(" }")
    return tmp

is_prime(1,2,3,4,5,6,7,8,9)



