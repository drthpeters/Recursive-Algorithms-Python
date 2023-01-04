# (c) drthpeters

def shift(x,y,z,k,count):
    if k == 1: 
        count += 1
        print('disk ',k,' ',x,' -> ',y)       
    else: 
        count = shift(x,z,y,k-1,count)
        count += 1
        print('disk ',k,' ',x,' -> ',y)
        count = shift(z,y,x,k-1,count)
    return count

#------------------------------------------------------------------------------
# main program  
print(); print('Tower of Hanoi')
n = int(input('number of disks (<= 6): '))

count = shift('source','target','auxiliary',n,0)
print(); print('number of shift calls: ',count)        