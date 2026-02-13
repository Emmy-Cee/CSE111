def main():
#call the function to read the list and print it
    list = read_provinces('provinces.txt')
    print(list)

    #remove the first element of the list
    list.pop(0)
    #print statement
    # print(list)

    #remove the last element of the list
    list.pop()
    #print statement
    # print(list)

    for i in range(len(list)):
        if list[i] == 'AB':
            list[i] = 'Alberta'

    count = list.count('Alberta')

    print(f'Alberta occurs {count} times in the modified list.')

def read_provinces(filename):

    #The initialized empty list to store the text in the text file
    province_list = []

    with open(filename, "rt") as province:
        # to read each line of the province file
        for line in province:
            # to strip ehite lines in the text file
            clean_line  = line.strip()

            #to appeend the clean line to the empty list
            province_list.append(clean_line)

    #to return the updated list to the function
    return province_list

if __name__ == "__main__":
    main()