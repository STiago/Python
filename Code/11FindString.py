def count_substring(string, sub_string):
    count = 0
    i = 0
    while i < len(string):
        a = string.find(sub_string,i,len(string))
        if a == -1:
            a = 0
        else:
            count += 1
        i += a + 1              
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
