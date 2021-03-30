import math

z = [
    {
        "name": "sajjad",
        "height": 1.840,
        "weight": 90
    },
    {
        "name" : "parvaneh",
        "height": 1.60,
        "weight": 50
    }

]


def calcbmi(weight, height):
    POWER_TWO = 2
    return weight / math.pow(height, POWER_TWO)


def calcbmiargs(*args):
    for i in args:
        h = i["height"]
        w = i["weight"]
        print(i["name"], "'s bmi is", calcbmi(weight=w, height=h))

# a = {"height" : 1.84, "weight" : 90, "name" : "sajjad"}

calcbmiargs(*z)
# calcbmiargs(a,b)

# for item in z:
#     height = z[item]["height"]
#     weight = z[item]["weight"]
#     bmi = calcbmi(weight, height)
#     print(item, "'s bmi is ", bmi)

#
