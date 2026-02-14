import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry, FloatEntry
import math
from datetime import date

def main():
    root = tk.Tk()
    frm_main = Frame(root)
    frm_main.option_add("*Font", "Arial 16")
    frm_main.master.title('Tire Volume')
    frm_main.pack(padx = 3, pady = 3, fill = tk.BOTH, expand = 1)
    setup_main(frm_main)
    frm_main.mainloop()
    
def setup_main(frm):
    lbl_width = Label(frm, text="Width (80 - 300)")
    lbl_width.grid(row=0, column=0, padx = 3, pady = 3, sticky='w')
    ent_width = FloatEntry(frm, width=5, lower_bound=80, upper_bound=300)
    ent_width.grid(row=0, column=1, padx = 3, pady = 3, sticky='e')
    txt_width = Label(frm, text="Millimeters")
    txt_width.grid(row=0, column=2, padx=2, pady=2, sticky='w')
    
    lbl_ratio = Label(frm, text="Aspect Ratio (30 - 90)")
    lbl_ratio.grid(row=1, column=0, padx = 3, pady = 3, sticky='w')
    ent_ratio = FloatEntry(frm, width=5, lower_bound=30, upper_bound=90)
    ent_ratio.grid(row=1, column=1, padx = 3, pady = 3, sticky='e'),
    
    lbl_diameter = Label(frm, text="Diameter (7 - 30)")
    lbl_diameter.grid(row=2, column=0, padx = 3, pady = 3, sticky='w')
    ent_diameter = FloatEntry(frm, width=5, lower_bound=7, upper_bound=30)
    ent_diameter.grid(row=2, column=1, padx = 3, pady = 3, sticky='e')
    txt_diameter = Label(frm, text="Inches")
    txt_diameter.grid(row=2, column=2, padx=2, pady=2, sticky='w')
    
    btn_calculate = Button(frm, text="Calculate")
    btn_calculate.grid(row=3, column=0, padx = 3, pady = 3)
    
    btn_clear = Button(frm, text="Clear")
    btn_clear.grid(row=3, column=2, padx=2, pady=2)
    
    lbl_calculate = Label(frm, text="", anchor='w')
    lbl_calculate.grid(row=4, column=0, padx = 3, pady = 3)
    calc_txt = Label(frm, text="Litres")
    calc_txt.grid(row=4, column=1, padx = 2, pady=2, sticky='e')

    # lbl_final = Label(frm, text="")
    # lbl_final.grid(row=5, column=0, padx = 2, pady = 2)
    
    def calculate_vol(width, ratio, diameter):
        Volume = (math.pi * (width ** 2) * ratio * (width * ratio + 2540 * diameter)) / 10000000000
        return Volume
    
    def calc_btn():
        try:
            width = ent_width.get()
            ratio = ent_ratio.get()
            diameter = ent_diameter.get()
        except ValueError:
            lbl_calculate.config(text=f"Please enter a valid number for all fields")
    
        calcvol = calculate_vol(width, ratio, diameter)
        lbl_calculate.config(text=f"{calcvol:.2f}")
    
    def clear():
        btn_clear.focus()
        ent_width.clear()
        ent_ratio.clear()
        ent_diameter.clear()
        lbl_calculate.config(text="")
        # lbl_final.config(text="")
        ent_width.focus()
    
    btn_calculate.config(command=calc_btn)
    btn_clear.config(command=clear)
    
if __name__ == "__main__":
    main()