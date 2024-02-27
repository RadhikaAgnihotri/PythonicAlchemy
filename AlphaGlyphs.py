#The AlphaGlyphs

#To print the alphabet A using '*' symbol

#  ***
# *   *
# *   *
# *****
# *   *
# *   *
# *   *

n=7
for i in range(n):
    if i == 0:
        print(' '+'*'*3)
    if i == 1 or i == 2:
        print('*'+' '*3+'*')
    if i == 3:
        print('*'*5)
    if i == 4 or i == 5 or i == 6:
        print('*'+' '*3+'*')