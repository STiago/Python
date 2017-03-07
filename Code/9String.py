def print_full_name(a, b):
    print 'Hello ' + str(a) + ' ' + str(b) + '! You just delved into python.'
    #print("Hello {} {}! You just delved into python.".format(a,b))

if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)
