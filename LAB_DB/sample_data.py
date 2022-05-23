#!/usr/bin/python3
import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import sys
import os


def center_window(width, height):
	# get screen width and height
	screen_width = window.winfo_screenwidth()
	screen_height = window.winfo_screenheight()
	
	# calculate position x and y coordinates
	x = (screen_width/7)
	y = (screen_height/7)
	window.geometry('%dx%d+%d+%d' % (width, height, x, y))

window = Tk()
window.title("LS3GP Laboratory DataBase")
window.configure(background="ghost white")
#window.geometry("570x350")
window.resizable(False, False)
window.iconbitmap(os.getcwd() + '\logo3_sqt.ico')
center_window(600, 350) #window size


window.protocol("WM_DELETE_WINDOW")  # handle window closing





l1 = Label(window, text="Grain size", bg="ghost white")
l1.grid(row=12, column=0, sticky=W, padx=5, pady=5)
l1_1 = Label(window, text="CL", width=2, bg="ghost white")
l1_1.grid(row=12, column=1, sticky=E, padx=2, pady=5)
clay_text = StringVar()
e1_1 = Entry(window, textvariable=clay_text, width=6)
e1_1.grid(row=12, column=2, padx=1, pady=5, sticky=W)
l1_2 = Label(window, text="SL", width=2, bg="ghost white")
l1_2.grid(row=12, column=3, sticky=E, padx=2, pady=5)
silt_text = StringVar()
e1_2 = Entry(window, textvariable=silt_text, width=6)
e1_2.grid(row=12, column=4, padx=1, pady=5, sticky=W)
l1_3 = Label(window, text="SD", width=2, bg="ghost white")
l1_3.grid(row=12, column=5, sticky=E, padx=2, pady=5)
sand_text = StringVar()
e1_3 = Entry(window, textvariable=sand_text, width=6)
e1_3.grid(row=12, column=6, padx=1, pady=5, sticky=W)

l2 = Label(window, text="Atterberg limits", bg="ghost white")
l2.grid(row=13, column=0, sticky=W, padx=5, pady=5)
l2_1 = Label(window, text="PL", width=2, bg="ghost white")
l2_1.grid(row=13, column=1, sticky=E, padx=2, pady=5)
pl_text = StringVar()
e1_1 = Entry(window, textvariable=pl_text, width=6)
e1_1.grid(row=13, column=2, padx=1, pady=5, sticky=W)
l2_2 = Label(window, text="LL", width=2, anchor=W, bg="ghost white")
l2_2.grid(row=13, column=3, sticky=E, padx=2, pady=5)
ll_text = StringVar()
e1_1 = Entry(window, textvariable=ll_text, width=6)
e1_1.grid(row=13, column=4, padx=1, pady=5, sticky=W)
l2_3 = Label(window, text="PI", width=2, anchor=W, bg="ghost white")
l2_3.grid(row=13, column=5, sticky=E, padx=2, pady=5)
pi_text = StringVar()
e1_1 = Entry(window, textvariable=pi_text, width=6)
e1_1.grid(row=13, column=6, padx=1, pady=5, sticky=W)

l3 = Label(window, text="In situ", bg="ghost white")
l3.grid(row=14, column=0, sticky=W, padx=5, pady=5)
l3_1 = Label(window, text="wc", width=2, bg="ghost white")
l3_1.grid(row=14, column=1, sticky=E, padx=2, pady=5)
is_wc_text = StringVar()
e1_1 = Entry(window, textvariable=is_wc_text, width=6)
e1_1.grid(row=14, column=2, padx=1, pady=5, sticky=W)
l3_2 = Label(window, text="f", font="Symbol", width=2, bg="ghost white")
l3_2.grid(row=14, column=3, sticky=E, padx=2, pady=5)
is_poro_text = StringVar()
e1_1 = Entry(window, textvariable=is_poro_text, width=6)
e1_1.grid(row=14, column=4, padx=1, pady=5, sticky=W)
l3_3 = Label(window, text="s\u02C8", font="Symbol", width=2, bg="ghost white")
l3_3.grid(row=14, column=5, sticky=E, padx=2, pady=5)
is_effstrs_text = StringVar()
e1_1 = Entry(window, textvariable=is_effstrs_text, width=6)
e1_1.grid(row=14, column=6, padx=1, pady=5, sticky=W)

l4 = Label(window, text="Depostion", bg="ghost white")
l4.grid(row=15, column=0, sticky=W, padx=5, pady=5)
l4_1 = Label(window, text="f\u02F3", font="Symbol", width=2, bg="ghost white")
l4_1.grid(row=15, column=1, sticky=E, padx=2, pady=4)
dep_poro_text = StringVar()
e1_1 = Entry(window, textvariable=dep_poro_text, width=6)
e1_1.grid(row=15, column=2, padx=1, pady=5, sticky=W)
l4_2 = Label(window, text="K\u02F3", width=2, bg="ghost white")
l4_2.grid(row=15, column=3, sticky=E, padx=2, pady=5)
depo_hydcon_text = StringVar()
e1_1 = Entry(window, textvariable=depo_hydcon_text, width=6)
e1_1.grid(row=15, column=4, padx=1, pady=5, sticky=W)
l4_3 = Label(window, text="Ss\u02F3", width=2, bg="ghost white")
l4_3.grid(row=15, column=5, sticky=E, padx=2, pady=5)
depo_store_text = StringVar()
e1_1 = Entry(window, textvariable=depo_store_text, width=6)
e1_1.grid(row=15, column=6, padx=1, pady=5, sticky=W)

l5 = Label(window, text="Compressibilities", bg="ghost white")
l5.grid(row=16, column=0, sticky=W, padx=5, pady=5)
l5_1 = Label(window, text="Cc", width=2, bg="ghost white")
l5_1.grid(row=16, column=1, sticky=E, padx=2, pady=4)
cc_text = StringVar()
e1_1 = Entry(window, textvariable=cc_text, width=6)
e1_1.grid(row=16, column=2, padx=1, pady=5, sticky=W)
l5_2 = Label(window, text="Cs", width=2, bg="ghost white")
l5_2.grid(row=16, column=3, sticky=E, padx=2, pady=5)
cs_text = StringVar()
e1_1 = Entry(window, textvariable=cs_text, width=6)
e1_1.grid(row=16, column=4, padx=1, pady=5, sticky=W)
l5_3 = Label(window, text="Cr", width=2, bg="ghost white")
l5_3.grid(row=16, column=5, sticky=E, padx=2, pady=5)
cr_text = StringVar()
e1_1 = Entry(window, textvariable=cr_text, width=6)
e1_1.grid(row=16, column=6, padx=1, pady=5, sticky=W)







# l6 = Label(window, text="Core depth (mbsl)", anchor=W, bg="ghost white")
# l6.grid(row=13, column=3, sticky=W, padx=5, pady=5)

# l7 = Label(window, text="Sample data:", bg="ghost white")
# l7.grid(row=15, column=0, sticky=W, padx=5, pady=5)

# sampleid_text = StringVar()
# e1 = Entry(window, textvariable=sampleid_text)
# e1.grid(row=12, column=1, columnspan=1, padx=5, pady=5)

# sample_depth_text = StringVar()
# e2 = Entry(window, textvariable=sample_depth_text)
# e2.grid(row=12, column=4, columnspan=1, padx=5, pady=5)

# core_id_text = StringVar()
# e5 = Entry(window, textvariable=core_id_text)
# e5.grid(row=13, column=1, columnspan=1, padx=5, pady=5)

# core_depth_float = StringVar()
# e4 = Entry(window, textvariable=core_depth_float)
# e4.grid(row=13, column=4, columnspan=1, padx=5, pady=5)

# test_type_text = StringVar()
# e3 = ttk.Combobox(values=["R&B", "CRS", "TAS"], width=17)
# e3.grid(row=14, column=1, columnspan=1, padx=5, pady=5)
# test_type_text = e3

# cruise_text = StringVar()
# e6 = Entry(window, textvariable=cruise_text)
# e6.grid(row=14, column=4, columnspan=1, padx=5, pady=5)

# list1 = Listbox(window, height=11, width=37)
# list1.grid(row=16, column=0, rowspan=6, columnspan=5, padx=5, sticky=W)

# sb1 = Scrollbar(window)
# sb1.grid(row=16, column=4, rowspan=4, padx=5, sticky=E)

# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)

# list1.bind('<<ListboxSelect>>')

# b1 = Button(window, text="View all", width=12, bg="LightCyan2", command=view_command)
# b1.grid(row=16, column=5)

# b2 = Button(window, text="Find samples", width=12, bg="LightCyan2",command=search_command)
# b2.grid(row=6, column=5)

# b3 = Button(window, text="Add samples", width=12, bg="LightCyan2",command=add_command)
# b3.grid(row=7, column=5)

# b4 = Button(window, text="Update", width=12, bg="LightCyan2",command=update_command)
# b4.grid(row=8, column=5)

# b5 = Button(window, text="Delete sample", width=12, bg="LightCyan2",command=delete_command)
# b5.grid(row=9, column=5)

# b6 = Button(window, text="View samples", width=12, bg="light blue", command=on_samples)
# b6.grid(row=120, column=5, pady=5)

# b7 = Button(window, text="Exit", width=12, bg="rosy brown",command=on_closing)
# b7.grid(row=121, column=5, pady=5)

# b8 = Button(window, text="Open menu", width=12, bg="light blue",command=open_menu)
# b8.grid(row=121, column=0, pady=5, padx=5)

# b9 = Button(window, text="Clear all", width=10, height=4, bg="ghost white", command=clear_fields)
# b9.grid(row=12, column=5, rowspan=3)

window.mainloop()