import sys
import re


for line in sys.stdin:
    print(line.title().replace(" ",""),sep="", end="")
