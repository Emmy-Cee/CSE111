def main():
    # Subnet Calculator for Class C IPv4 Networks
    # This program works with CIDR notation like 192.168.1.0/24

    print("===== Subnet Calculator =====")

    # Step 1: Get the network from the user
    network = input("Enter Class C network (example: 192.168.1.0/24): ")

    # Split the IP and the prefix
    ip_part, prefix_part = network.split("/")
    base_prefix = int(prefix_part)

    # Step 2: Ask what the user wants to do
    print("\nChoose an option:")
    print("1 - I know how many IPs I need")
    print("2 - I know the prefix index")

    # Step 3: If the user knows the number of IPs
    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            needed_ips = int(input("Enter how many IPs you need: "))
            prefix = get_prefix_from_ips(needed_ips)
            break
        elif choice == "2":
            prefix = int(input("Enter prefix (example: 27): "))
            break
        else:
            print("Invalid option. Please enter 1 or 2.")


    total_ips = get_total_ips(prefix)
    usable_ips = total_ips - 2
    subnet_mask = get_subnet_mask(prefix)

# Step 7: Show results
    print("\n------ Subnet Result ------")
    print("Network:", ip_part)
    print("Prefix Index: /" + str(prefix))
    print("Subnet Mask:", subnet_mask)
    print("Total IPs:", total_ips)
    print("Usable IPs:", usable_ips)


# Find how many bits are needed
def get_prefix_from_ips(needed_ips):
        host_bits = 0
        power = 1

        while power < needed_ips:
            power = power * 2
            host_bits = host_bits + 1

        return 32 - host_bits

# Step 5: Calculate total IPs
def get_total_ips(prefix):
    host_bits = 32 - prefix
    total = 1

    for i in range(host_bits):
        total = total * 2

    return total

# Step 6: Build subnet mask
def get_subnet_mask(prefix):
    mask_binary = ""

    for i in range(prefix):
        mask_binary = mask_binary + "1"

    for i in range(32 - prefix):
        mask_binary = mask_binary + "0"

# Split into 4 parts
    part1 = mask_binary[0:8]
    part2 = mask_binary[8:16]
    part3 = mask_binary[16:24]
    part4 = mask_binary[24:32]

# Convert to decimal
    mask1 = int(part1, 2)
    mask2 = int(part2, 2)
    mask3 = int(part3, 2)
    mask4 = int(part4, 2)

    return str(mask1) + "." + str(mask2) + "." + str(mask3) + "." + str(mask4)

if __name__ == "__main__":
    main()
