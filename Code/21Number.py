 #!env/bin/python

def AddPairOdd(arr):
    ap = ao = 0
    solution = []
    for i in arr:
        if i%2 == 0:
            ap += i
        else:
            ao += i
    solution.append(ap)
    solution.append(ao)
    return solution

def main():
     arr = []
     result = []
     pair = odd = 0
     for i in range(10):
        n = int(input('Insert the number %d:' %(i+1)))
        arr.append(n)

     result = AddPairOdd(arr)
     pair = result[0]
     odd = result[1]
     print('\nPair %d' %pair)
     print('\nOdd %d' %odd)

if __name__ == "__main__":
     main()
