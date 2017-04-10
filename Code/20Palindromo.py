#!env/bin/python
def palindromo(arr):
    new_arr = arr.lower()
    aux = new_arr.replace(' ','')
    result = -1

    if aux == aux[::-1]:
        result = 1

    return result

def main():
    arr = raw_input('Insert the sentence:')
    solution = palindromo(arr)

    if solution == 1:
        print "Is palindromo"
    else:
        print "Is not palindromo"

if __name__ == "__main__":
    main()
