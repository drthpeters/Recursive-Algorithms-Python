# (c) drthpeters

print(); print('Ackermann function with WHILE') 
x = int(input('m = '))
y = int(input('n = '))

m = x; n = y

stack = []
stack.append(m) # push(m; stack);
stack.append(n) # push(n; stack);

count = 0
while len(stack) != 1:
    count += 1
    if count % 1000 == 0: print('count = ',count)
    #print('count = ',count,' stack = ',stack)
    n = stack[-1]; stack.pop(-1) # n := pop(stack);
    m = stack[-1]; stack.pop(-1) # m := pop(stack);
    if m == 0:
        stack.append(n+1) # push(n + 1; stack);
    else:
        if n == 0:
            stack.append(m-1) # push(m-1; stack); 
            stack.append(1) # push(1; stack)
        else: 
            stack.append(m-1) # push(m-1; stack); 
            stack.append(m) # push(m; stack); 
            stack.append(n-1) #push(n-1; stack);

result = stack[-1] # pop(stack)

print(); print('number of runs = ',count)
print(); print('A(',x,',',y,') = ',result)