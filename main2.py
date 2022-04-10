from tkinter import *
import units
import gears

root = Tk()

root.title("Designer's Reference")
#root.geometry('1400x400')

instruction_frame = LabelFrame(master=root, text="Instructions", bg='#c9ad20')
instruction_frame.grid(row=0, column=0, padx=5, pady=5, columnspan=4)

instruction_text = """Hello! This is an application meant as a quick reference to designers working with CAD. 
This is my final project for EECE 2140: Computing Fundamentals. Simply select between the 
different options for each individual calculator/convertor and input data for results! -Oliver Hugh"""

instruction_label = Label(master=instruction_frame, text=instruction_text, bg='#c9ad20', width=90)
instruction_label.grid(row=0, column=0)

#The Gear Calculator Frame
gear_frame = LabelFrame(master=root, text="Gear Calculator", bg='#c98a00')
gear_frame.grid(row=1, column=0, padx=5, pady=5)
gear_label = Label(gear_frame, text="GEARSSSSS", bg='#c98a00', width=20, height=20,)
gear_label.pack()

#entry for num teeth in gear 1
#entry for num teeth in gear 2
#entry or drop-down for dp
#button to calculate
#display result


#The unit Calculator Frame
unit_frame = LabelFrame(master=root, text="Unit Convertor", bg='#7a6d17')
unit_frame.grid(row=1, column=1, padx=5, pady=5)

#Drop Down menu for the calculator frame
conversion_options = ['Time', 'Distance', 'Weight/Mass', 'Angle', 'Metric Prefixes']
#The type of conversion which will be decided by the user clicking
conversion_type = StringVar()
#But we will set it to first in list as default
conversion_type.set(conversion_options[0])
conversion_type_drop = OptionMenu(unit_frame, conversion_type, *conversion_options)
conversion_type_drop.pack()
unit_label = Label(unit_frame, text="UNITSSS", bg='#7a6d17', width=20, height=20)
unit_label.pack()

#Drop-down of unit to convert FROM

#Drop-down of unit to convert TO

#Entry widget

#button to press to make the conversion

#display result


#The Decimal/Fraction Convertor
dec_frac_frame = LabelFrame(root, text="Decimal/Fraction Convertor", bg='#e09758')
dec_frac_frame.grid(row=1, column=2, padx=5, pady=5)
dec_frac_label = Label(dec_frac_frame, text="FRACTIONSSS", bg='#e09758', width=20, height=20)
dec_frac_label.pack()

hardware_ref_frame = LabelFrame(root, text="Hardware Reference", bg='#b8341a')
hardware_ref_frame.grid(row=1, column=3, padx=5, pady=5)
hardware_ref_label = Label(hardware_ref_frame, text="HARDWARE", bg='#b8341a', width=20, height=20)
hardware_ref_label.pack()

root.mainloop()
