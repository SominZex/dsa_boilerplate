prev2 = 0
prev1 = 1
count = 2

def fibonacci(prev1,prev2):
    global count
    if count<=19:
        newFibo = prev1+prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)