
# (c) drthpeters

def prob(step,white):
    if (white > step) or (white < 0): return 0
    else:
        if step == 1: 
            if white == 1: return p
            else: return 1 - p
        else:
            return prob(1,0)*prob(step-1,white)+prob(1,1)*prob(step-1,white-1)

# main program
print(); print('Binomial Distribution')
w = int(input('Number of white balls: '))
b = int(input('Number of black balls: '))    
p = w/(w + b)
n = int(input('Number of draws: '))  
for k in range(n+1):
    print('Probability for ',k,' white balls: ',prob(n,k))      