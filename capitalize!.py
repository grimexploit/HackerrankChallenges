#!/bin/python3

import math
import os
import random
import re
import sys
import string 
# Complete the solve function below.
def solve(s):			#ugsun stringiig hoorond ni salgaad ehnii usgiig capitalize() ashiglan tomruulaad i iin lower usgiig replace 
    str= [i.strip().capitalize() for i in s.split() ]
    for i in str:
         s =s.replace(i.lower(),i)
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
