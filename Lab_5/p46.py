import sys
try:
    x=5/0
except:
    print("An error occurred: ", sys.exc_info()[0])