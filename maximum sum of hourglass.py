"""
An hour glass is made of 7 cells
in following form.
    A B C
      D
    E F G
"""

#columns=input("enter columns:")

rows=input("enter rows:")

counter=0
lister=[]
def falo():
    for counter in range(rows):
        mystring=input()
        lister=mystring.split()
        return lister
        lister.clear()
print(falo(    






#ri[n]+ri[n+1]+ri[n+2]
#+r(i+1)[n+1]
#+r(i+2)[n]+r(i+2)[n+1]+r(i+2)[n+2]

