import sys

print("Recustion limit is:", sys.getrecursionlimit()) # 1000 - max no of stackframes

sys.setrecursionlimit(2001) # not recommended - also after certain limit python changes limit but actually stops appln before only

print("Recustion limit now is:", sys.getrecursionlimit()) # 1000 - max no of stackframes