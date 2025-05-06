from nagini_contracts.contracts import *

@Pure
def purefunction(i: int) -> int:
    y = 18
    if(i > 0):
        y = y + 1
    elif(i < 0):
        return 0
    else:
        y = y * 2
        return 3

@ContractOnly
def compare3(b: int) -> int:
    Requires(purefunction(1) == 3)
    Ensures(Result() > 13)