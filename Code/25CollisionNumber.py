#!/usr/bin/env python27

def assigned_numbers():
    assigned_numb = []
    sorted_list = []
    filepath =  '/Python/Code/numbers.txt'
    with open(filepath,"r+") as newfile: 
        data = newfile.read()
        assigned_numb = data.split('\n')
        assigned_numb = assigned_numb[0:-1]
        for num in assigned_numb:
            sorted_list.append(int(num))
        sorted_list = sorted(sorted_list)
    return sorted_list 


def get_assigned():
    assigned = assigned_numbers()
    assigned = list(set(assigned)) 
    return sorted(assigned)          


def free_numbers():
    free = []
    assigned = get_assigned()
    for item in range(251):
        if item not in assigned:
            free.append(item)
    return free


def get_occurences(number):
    occurences = 0
    assigned_n = assigned_numbers()
    for element in assigned_n:
        if number == element:
            occurences += 1
    return occurences


def retrieve_occurences_list():
    occurences_number = []
    assigned = assigned_numbers()
    free = free_numbers()
    for item in assigned:
        occurence = get_occurences(item)
        occurences_number.append([item, occurence])
    for item in free:
        occurences_number.append([item, 0])
    return occurences_number


def next_to_assign():
    occ_num = retrieve_occurences_list()
    occ = []
    for number in occ_num:
        occ.append(number[1])
    minimun = min(occ)
    for number in occ_num:
        if number[1] == minimun:
            num_selected = number[0]
            break
    return num_selected
        

def main():
    number = next_to_assign()
    print number

if __name__ == "__main__":
    main()
