import tkinter as tk
from tkinter import ttk

# --- Your existing logic functions ---
def get_prefix_from_ips(needed_ips):
    host_bits = 0
    power = 1
    while power < needed_ips:
        power *= 2
        host_bits += 1
    return 32 - host_bits

def get_total_ips(prefix):
    return 2 ** (32 - prefix)

def get_subnet_mask(prefix):
    mask_binary = "1" * prefix + "0" * (32 - prefix)
    parts = [str(int(mask_binary[i:i+8], 2)) for i in range(0, 32, 8)]
    return ".".join(parts)

# --- GUI ---
def calculate():
    network = entry_network.get()
    try:
        ip_part, _ = network.split("/")
    except:
        label_result.config(text="Invalid network format")
        return

    choice = calc_choice.get()
    if choice == "IPs":
        needed_ips = int(entry_value.get())
        prefix = get_prefix_from_ips(needed_ips)
    else:
        prefix = int(entry_value.get())

    total_ips = get_total_ips(prefix)
    usable_ips = total_ips - 2
    subnet_mask = get_subnet_mask(prefix)

    result_text = (
        f"Network: {ip_part}\n"
        f"Prefix Index: /{prefix}\n"
        f"Subnet Mask: {subnet_mask}\n"
        f"Total IPs: {total_ips}\n"
        f"Usable IPs: {usable_ips}"
    )
    label_result.config(text=result_text)

# --- Tkinter Window ---
root = tk.Tk()
root.title("Class C Subnet Calculator")

tk.Label(root, text="Enter network (e.g., 192.168.1.0/24):").pack(pady=5)
entry_network = tk.Entry(root, width=25)
entry_network.pack()

# Radio buttons for choice
calc_choice = tk.StringVar(value="IPs")
tk.Radiobutton(root, text="I know number of IPs", variable=calc_choice, value="IPs").pack()
tk.Radiobutton(root, text="I know prefix", variable=calc_choice, value="Prefix").pack()

tk.Label(root, text="Enter value:").pack(pady=5)
entry_value = tk.Entry(root, width=10)
entry_value.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

label_result = tk.Label(root, text="", justify="left")
label_result.pack(pady=10)

root.mainloop()
import tkinter as tk
from tkinter import ttk

# --- Your existing logic functions ---
def get_prefix_from_ips(needed_ips):
    host_bits = 0
    power = 1
    while power < needed_ips:
        power *= 2
        host_bits += 1
    return 32 - host_bits

def get_total_ips(prefix):
    return 2 ** (32 - prefix)

def get_subnet_mask(prefix):
    mask_binary = "1" * prefix + "0" * (32 - prefix)
    parts = [str(int(mask_binary[i:i+8], 2)) for i in range(0, 32, 8)]
    return ".".join(parts)

# --- GUI ---
def calculate():
    network = entry_network.get()
    try:
        ip_part, _ = network.split("/")
    except:
        label_result.config(text="Invalid network format")
        return

    choice = calc_choice.get()
    if choice == "IPs":
        needed_ips = int(entry_value.get())
        prefix = get_prefix_from_ips(needed_ips)
    else:
        prefix = int(entry_value.get())

    total_ips = get_total_ips(prefix)
    usable_ips = total_ips - 2
    subnet_mask = get_subnet_mask(prefix)

    result_text = (
        f"Network: {ip_part}\n"
        f"Prefix Index: /{prefix}\n"
        f"Subnet Mask: {subnet_mask}\n"
        f"Total IPs: {total_ips}\n"
        f"Usable IPs: {usable_ips}"
    )
    label_result.config(text=result_text)
    
def clear():
    entry_network.delete(0, tk.END)  # Clears network input
    entry_value.delete(0, tk.END)    # Clears value input
    calc_choice.set("IPs")            # Resets radio button to default
    label_result.config(text="")      # Clears result display
    entry_network.focus()

# --- Tkinter Window ---
root = tk.Tk()
root.title("Class C Subnet Calculator")

tk.Label(root, text="Enter network (e.g., 192.168.1.0/24):").pack(pady=5)
entry_network = tk.Entry(root, width=25)
entry_network.pack()

# Radio buttons for choice
calc_choice = tk.StringVar(value="IPs")
tk.Radiobutton(root, text="I know number of IPs", variable=calc_choice, value="IPs").pack()
tk.Radiobutton(root, text="I know prefix", variable=calc_choice, value="Prefix").pack()

tk.Label(root, text="Enter value:").pack(pady=5)
entry_value = tk.Entry(root, width=10)
entry_value.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
tk.Button(root, text='Clear', command=clear).pack(pady=10)

label_result = tk.Label(root, text="", justify="left")
label_result.pack(pady=10)

root.mainloop()
