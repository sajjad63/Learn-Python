import math

z = {
    "sajjad":
        {
            "height": 1.840,
            "weight": 90
        },

    "parvaneh":
        {
            "height": 1.60,
            "weight": 50
        }
}

y = {
    "safura":
        {
            "height": 1.840,
            "weight": 90
        },

    "maza":
        {
            "height": 1.60,
            "weight": 50
        }
}


# def calcbmi(weight, height):
#     POWER_TWO = 2
#     return weight / math.pow(height, POWER_TWO)


# def calcbmiargs(**args):
#     for i in args:
#         h = args[i]['height']
#         w = args[i]['weight']
#         print(i, "'s bmi is", calcbmi(weight=w, height=h))

# def calcbmiargs(**kwargs):
#     print(kwargs)
#     print(kwargs.items())
#     print(type(kwargs.items()))
#     for i, v in kwargs.items():
#         h = v['height']
#         w = v['weight']
#         print(i, "'s bmi is", calcbmi(weight=w, height=h))

def calcbmiargs(**kwargs):
    f = lambda w, h: w / math.pow(h, 2)
    for i, v in kwargs.items():
        h = v['height']
        w = v['weight']
        print(i, "'s bmi is", f(w, h))



calcbmiargs(**y)
