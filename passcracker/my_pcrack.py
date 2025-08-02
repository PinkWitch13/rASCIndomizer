import string
import random

def example_pass_breaker():

    with open("rASCIndomizer/passcracker/example_pass.txt", "r") as file:
        mpass = file.read()
    i = 1
    chars = ["a", "b", "c"]
    max_pass_len = 3
    max_combi = 3**3
    atempt = 0
    combinations = []

    while i < max_combi:
        to_try = "".join(random.sample(chars, max_pass_len))
        combinations.append(to_try)
        print(f"{to_try=}")
        print(f"{combinations=}")
        atempt+=1
        if to_try == mpass:
            print(f"Pasword broken! Your password is {mpass}, guest at {atempt=}")
            break
        else:
            i+=1
    
# example_pass_breaker()


def rASCIndomizer2():

    with open("rASCIndomizer/passcracker/example_pass.txt", "r") as file:
        mpass = file.read()
    
    chars = list(string.ascii_letters)+ list(string.digits)
    max_pass_len = 4
    i = 1
    max_combi = len(chars)**max_pass_len
    atempt = 0
    combinations = []
    stop = False

    while i <= max_combi and not stop:
        for n in range(1, max_pass_len+1):
            n =4
            #print(f"{n=} {chars=}")
            to_try = "".join(random.sample(chars, n))
            combinations.append(to_try)
            #print(f"{to_try=}")
            #print(f"{combinations=}")
            atempt+=1
            if to_try == mpass:
                print(f"Pasword broken! Your password is {mpass}, guest at {atempt=}")
                stop = True
                break
            else:
                i+=1
                continue
   

rASCIndomizer2()