
def naiveSimplify(numerator, denominator):
    numStr = str(numerator)
    denStr = str(denominator)
    lenNum = len(numStr)
    numStrConst = numStr
    for i in range(0, lenNum):
        testDigit = numStrConst[i]
        if testDigit != "0" and denStr.find(testDigit) != -1:
            denStr = denStr.replace(testDigit, "", 1)
            numStr = numStr.replace(testDigit, "", 1)
    if denStr == "" or denStr == "0":
        return ["", ""]
    output = [int(numStr), int(denStr)]
    return output


def calcFraction(input):
    if input == ["", ""]:
        return ["", ""]
    output = input[0] / input[1]
    return output


def generateFractions():
    prodNumerators = 1
    prodDenominators = 1
    for numerator in range(10, 100):
        for denominator in range(numerator, 100):
            if naiveSimplify(numerator, denominator) != ["", ""] and [numerator, denominator] != naiveSimplify(numerator, denominator):
                if (numerator / denominator) == calcFraction(naiveSimplify(numerator, denominator)):
                    # print(numerator, denominator)
                    # print(naiveSimplify(numerator, denominator))
                    prodNumerators = prodNumerators * \
                        naiveSimplify(numerator, denominator)[0]
                    prodDenominators = prodDenominators * \
                        naiveSimplify(numerator, denominator)[1]
    return [prodNumerators, prodDenominators]


print(generateFractions())
# answer is 8 / 800 = 1 / 100


# print(naiveSimplify(11, 12))
# print(naiveSimplify(10, 20))
# print(naiveSimplify(49, 98))
# print(naiveSimplify(30, 50))


# print(calcFraction(naiveSimplify(11, 12)))
# print(calcFraction(naiveSimplify(10, 20)))
# print(calcFraction(naiveSimplify(49, 98)))
# print(calcFraction(naiveSimplify(30, 50)))
