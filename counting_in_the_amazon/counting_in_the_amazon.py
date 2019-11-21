import math
'''
    For example one to eight is as follows:

1 = anane
2 = adak
3 = adak anane
4 = adak adak
5 = adak adak anane
6 = adak adak adak
7 = adak adak adak anane
8 = adak adak adak adak

Take a given number and return the Arara's equivalent. 
'''

def count_arara(n):
    adak_str = 'adak ' * int(n/2)
    if n%2!=0:
        adak_str += 'anane'
    return adak_str.strip(  )

print(count_arara(3))