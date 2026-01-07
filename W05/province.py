def main():
    province_list = read_list("provinces.txt")
    
    print(province_list)
    
    if province_list:
        province_list.pop(0)
    if province_list:
        province_list.pop()
    
    for i in range(len(province_list)):
        if province_list[i] == "AB":
            province_list[i] = "Alberta"
    print(province_list)

def read_list(filename):
    text_list = []
    
    with open(filename, "rt") as f:
        for line in f:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list

if __name__ == "__main__":
    main()
    
    