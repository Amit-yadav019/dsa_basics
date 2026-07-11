# Recursion = when a function calls itself untill a specific condition is mmet .


# let we have to print hello strivers 10 times using recursion 



def striver10(count):
    
    if count == 10 :
        return 
    print(" Hello , striver ")
    striver10(count+1)

if __name__ == "__main__":
    print(striver10(0))

