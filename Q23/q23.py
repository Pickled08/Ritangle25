import random

word=["D","O","D","E","C","A","H","E","D","R","O","N"]

for i in range(100):
    randwordorder = random.shuffle(word)
    if randwordorder[0] == "D" and (randwordorder[0] == randwordorder[2] or randwordorder[0] == randwordorder[3] or randwordorder[0] == randwordorder[4] or randwordorder[0] == randwordorder[5] or randwordorder[0] == randwordorder[6] or randwordorder[0] == randwordorder[7]):
        
