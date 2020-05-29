#!/usr/bin/env python3
##################################
#                                #
#       Created by tralph3       #
#   https://github.com/tralph3   #
#                                #
##################################

import random
import math
import sys

try:
    repeats = int(sys.argv[1])
except IndexError:
    repeats = 1

def cdKeyGen():
    invalidOutput = [333, 444, 555, 666, 777, 888, 999]
    isInvalid = True
    firstSegment = str(math.trunc(random.random() * 999)).zfill(3)
    while isInvalid:
        for i in invalidOutput:
            if firstSegment == i:
                firstSegment = str(math.trunc(random.random() * 999)).zfill(3)
            else:
                isInvalid = False
    isInvalid = True
    secondSegment = str(math.trunc(random.random() * 9999999)).zfill(7)
    while isInvalid:
        if secondSegment[6] == "0" or int(secondSegment[6]) >= 8:
            charList = list(secondSegment)
            charList[6] = str(math.trunc(random.random() * 6 + 1))
            secondSegment = "".join(charList)
        sumOfDigits = 0
        for i in secondSegment:
            sumOfDigits += int(i)
        if sumOfDigits % 7 == 0:
            isInvalid = False
        else:
            secondSegment = str(math.trunc(random.random() * 9999999)).zfill(7)

    completeKey = firstSegment + "-" + secondSegment

    return "Windows 95 CD Key: " + completeKey

def oemKeyGen():
    firstSegment = str(math.trunc(random.random() * 366)).zfill(3) + str(math.trunc(random.random() * 5 + 95)).zfill(2)
    secondSegment = "OEM"

    isInvalid = True
    thirdSegment = str(math.trunc(random.random() * 9999999)).zfill(7)
    while isInvalid:
        if thirdSegment[0] != "0":
            charList = list(thirdSegment)
            charList[0] = "0"
            thirdSegment = "".join(charList)
        sumOfDigits = 0
        for i in thirdSegment:
            sumOfDigits += int(i)
        if sumOfDigits % 7 == 0:
            isInvalid = False
        else:
            thirdSegment = str(math.trunc(random.random() * 9999999)).zfill(7)
    
    fourthSegment = str(math.trunc(random.random() * 99999)).zfill(5)
    completeKey = firstSegment + "-" + secondSegment + "-" + thirdSegment + "-" + fourthSegment
    return "Windows 95 OEM Key: " + completeKey

for i in range(repeats):
    print(str(cdKeyGen()) + "\n" + str(oemKeyGen()) + "\n-----------------")
