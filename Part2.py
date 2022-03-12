def isStringPermutation(s1: str, s2: str) -> bool:
    s1list = sorted(s1)
    s2list = sorted(s2)
    if s2list != s1list:
        print(False)
    else:
        print(True)
isStringPermutation("asd", "asd")

def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    diffList = []
    for i, v in enumerate(inputArray):
        diff = targetSum - v
        if diff > 0 and diff in inputArray:
            diffList.append((diff, v))
            inputArray.remove(v)
        for tupl in diffList:
            if tupl == (0, targetSum):
                diffList.remove(tupl)
    print(diffList)

pairsThatEqualSum([1,2,3,4,5], 7)