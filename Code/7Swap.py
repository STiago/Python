def swap_case(s):
    solution = ''
    for element in s:
        if element.isupper():
            solution += element.lower() 
        else:
            solution += element.upper()
    return solution


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
