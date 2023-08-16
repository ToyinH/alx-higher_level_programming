#!/usr/bin/python3
def weight_average(my_list=[]):
    sum1 = 0
    sum2 = 0
    if my_list == []:
        return 0
    else:
        for item in my_list:
            pdt = item[0] * item[1]
            sum1 += pdt
            sum2 += item[1]
        return sum1 / sum2
