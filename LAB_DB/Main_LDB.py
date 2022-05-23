#!/usr/bin/python3

import sqlite3
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import sys
import os


class DB:
	def __init__(self):
		self.conn = sqlite3.connect("GeoTekLab.db")
		self.cur = self.conn.cursor()
		self.cur.execute(
			"CREATE TABLE IF NOT EXISTS samples (id INTEGER PRIMARY KEY, sample_id TEXT, sample_depth REAL, core_id TEXT, core_depth REAL, lat FLOAT, lon FLOAT, cruise TEXT, test_type TEXT, grain_size TEXT, pl REAL, ll REAL, pi REAL, is_wc REAL, is_void REAL, is_effstrs REAL, dep_poro REAL, depo_hydcon REAL, depo_store REAL, cc REAL, cs REAL, cr REAL, strain_rate REAL, pre_strs REAL)")
		
		self.conn.commit()

	def __del__(self):
		self.conn.close()

	def view(self):
		self.cur.execute("SELECT * FROM samples")
		rows = self.cur.fetchall()
		return rows

	def insert(self, sample_id, sample_depth, core_id, core_depth, lat, lon, cruise, test_type, grain_size,
			 pl, ll, pi, is_wc, is_void, is_effstrs, dep_void, depo_hydcon, depo_store, cc, cs, cr, strain_rate, pre_strs):
		self.cur.execute("INSERT INTO samples VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (sample_id , sample_depth, core_id , core_depth, lat,
				    lon, cruise , test_type , grain_size , pl, ll, pi, is_wc, is_void, is_effstrs, dep_poro, depo_hydcon, depo_store, cc, cs, cr, strain_rate, pre_strs))
		self.conn.commit()
		self.view()

	def update(self, id, sample_id , sample_depth, core_id , core_depth, lat, lon, cruise , test_type , grain_size , pl, ll, pi, is_wc, is_void, is_effstrs, dep_poro, depo_hydcon, depo_store, cc, cs, cr, strain_rate, pre_strs):
		self.conn.commit()
		self.cur.execute("UPDATE samples SET sample_id =?, sample_depth=?, core_id =?, core_depth=?, lat=?, lon=?, cruise =?, test_type =?, grain_size =?, pl=?, ll=?, pi=?, is_wc=?, is_void=?, is_effstrs=?, dep_poro=?, depo_hydcon=?, depo_store=?, cc=?, cs=?, cr=?, strain_rate=?, pre_strs=?", 
				   (sample_id , sample_depth, core_id , core_depth, lat, lon, cruise , test_type , grain_size , pl, ll, pi, is_wc, is_void, is_effstrs, dep_poro, depo_hydcon, depo_store, cc, cs, cr, strain_rate, pre_strs, id))
		self.view()

	def delete(self, id):
		self.cur.execute("DELETE FROM samples WHERE id=?", (id,))
		self.conn.commit()
		self.view()

	def search(self, sample_id ="", sample_depth="", core_id ="", core_depth="", lat="", lon="", cruise ="", test_type ="", grain_size ="", pl="", ll="", pi="", is_wc="", is_void="", is_effstrs="", dep_poro="", depo_hydcon="", depo_store="", cc="", cs="", crr="", strain_rate="", pre_strs=""):
		self.cur.execute("SELECT * FROM samples WHERE sample_id =? OR sample_depth=? OR core_id =? OR core_depth=? OR lat=? OR lon=? OR cruise =? OR test_type =? OR grain_size =? OR pl=? OR ll=? OR pi=? OR is_wc=? OR is_void=? OR is_effstrs=? OR dep_poro=? OR depo_hydcon=? OR depo_store=? OR cc=? OR cs=? OR crr=? OR strain_rate=? OR pre_strs=?", 
				   (sample_id , sample_depth, core_id , core_depth, lat, lon, cruise, test_type , grain_size , pl, ll, pi, is_wc, is_void, is_effstrs, dep_poro, depo_hydcon, depo_store, cc, cs, crr, strain_rate, pre_strs))
		rows = self.cur.fetchall()
		if not rows:
			no_exist()
			clear_fields()
		return rows


db = DB()


def get_selected_row(event):
	global selected_tuple
	if list1.curselection():
#	if any(map(lambda x: any(x), list1.curselection())):
		index = list1.curselection()[0]
		selected_tuple = list1.get(index)
		e1.delete(0, END)
		e1.insert(END, selected_tuple[1])
		e2.delete(0, END)
		e2.insert(END, selected_tuple[2])
	#	sex.set(None)
	#	if sex_text == 'Home':
	#		sex.set(0)
	#	elif sex_text == 'Dona':
	#		sex.set(1)
		e3.delete(0, END)
		e3.insert(END, selected_tuple[3])
		e4.delete(0, END)
		e4.insert(END, selected_tuple[4])
		e5.delete(0, END)
		e5.insert(END, selected_tuple[5])
		e6.delete(0, END)
		e6.insert(END, selected_tuple[6])

#	index = list1.curselection()[0]
	


def clear_fields():
	e1.delete(0, END)
	e2.delete(0, END)
#	sex.set(None)
	e3.delete(0, END)
	e4.delete(0, END)
	e5.delete(0, END)
	e6.delete(0, END)


def view_command():
	list1.delete(0, END)
	for row in db.view():
		list1.insert(END, row)


def search_command():
	list1.delete(0, END)
	for row in db.search(first_text.get(), last_text.get(), sex_text.get(), date_text.get(), telf_text.get(), mail_text.get()):
		list1.insert(END, row)


def add_command():
	db.insert(first_text.get(), last_text.get(), sex_text.get(), date_text.get(), telf_text.get(), mail_text.get())
	list1.delete(0, END)
	list1.insert(END, (first_text.get(), last_text.get(), sex_text.get(), date_text.get(), telf_text.get(), mail_text.get()))
	paci_data = (first_text.get(), last_text.get(), sex_text.get(), date_text.get(), telf_text.get(), mail_text.get())
	fi = create_pc_file(paci_data)
	clear = clear_fields()
	d = view_command()


def delete_command():
	db.delete(selected_tuple[0])
	d = view_command()
	clear = clear_fields()


def update_command():
	db.update(selected_tuple[0], first_text.get(), last_text.get(), sex_text.get(), date_text.get(), telf_text.get(), mail_text.get())
	u = view_command()

def create_pc_file(pac_data):
	name = pac_data[0]
	last_name = pac_data[1]
	gender = pac_data[2]
	birth = pac_data[3]
	
	#Create samples file
	file_name = last_name + '_' + name + '.txt'
	with open(file_name, 'w+') as f:
		f.write('Nom: {0}\nCognom: {1}\nGènere: {2}\nData de naixement: {3}\n'.format(name, last_name, gender, birth))
		f.write('***Antropomètrics***\nDia:\nPes:\nAlçada:\n***Perímetres***\nBraç:\nCintura:\nCanell:\nMalucs:\n'.format())
		f.write('***Indexs masa corporal***\nIMC:\nPes ideal:\nGreix:\nRCC:\n'.format())
	f.close()
	
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
center_window(590, 690)

## Pop-up warnings
# Close window
def on_closing():
	dd = db
	if messagebox.askokcancel("Exiting", "Do you want to exit?"):
		window.destroy()
		del dd
# No exist error
def no_exist():
	messagebox.showwarning("Warning", "Samples do not exist")
# No hi ha res seleccionat
def no_select():
	messagebox.showwarning("Warning", "No samples selected")
#############

# Open samples window
def on_samples():
#	import pac_wi
	import interview
	try:
		index = list1.curselection()[0]
		selected_tuple = list1.get(index)
		if selected_tuple[1] and selected_tuple[2]:
			pac_name = selected_tuple[2] + '_' + selected_tuple[1]
# 			pw = pac_wi.start_window(pac_name)
			pint = interview.start_inwind(pac_name)
		else:
			ee = no_exist()
	except:
		ns = no_select()

def open_menu():
	import os
	from os.path import exists
	pac_file = selected_tuple[2] + '_' + selected_tuple[1] + '.xlsx'

	from os.path import exists
	if exists(pac_file):
		os.startfile(pac_file)
	else:
		os.system('copy menu_basic.xlsx ' + pac_file)
		os.startfile(pac_file)

window.protocol("WM_DELETE_WINDOW", on_closing)  # handle window closing

top_frame = Frame(window, width = 590, height=155, pady=3, borderwidth = 2, relief="ridge", bg="LightSteelBlue1", highlightcolor="red").grid(row=1, rowspan=5, column=0, columnspan=9, sticky=N)
center_frame = Frame(window, width = 590, height=240, pady=3, borderwidth = 2, relief="ridge", bg="LightSteelBlue1").grid(row=7, rowspan=5, column=0, columnspan=9)
bot_frame = Frame(window, width = 590, height=300, pady=3, borderwidth = 2, relief="ridge", bg="snow").grid(row=12, rowspan=6, column=0, columnspan=9)

l1 = Label(top_frame, text="Sample ID", bg="LightSteelBlue1")
l1.grid(row=1, column=0, sticky=NW, padx=5, pady=5)

l2 = Label(top_frame, text="Sample depth (mbsf)", bg="LightSteelBlue1")
l2.grid(row=1, column=3, columnspan=2, sticky=NW, padx=5, pady=5)

l3 = Label(top_frame, text="Core", bg="LightSteelBlue1")
l3.grid(row=2, column=0, sticky=NW, padx=5, pady=5)

l4 = Label(top_frame, text="Core depth (mbsl)", anchor=W, bg="LightSteelBlue1")
l4.grid(row=2, column=3, columnspan=2, sticky=W, padx=5, pady=5)

l5 = Label(top_frame, text="Corer type", anchor=W, bg="LightSteelBlue1")
l5.grid(row=3, column=0, sticky=W, padx=5, pady=5)

l6 = Label(top_frame, text="Cruise", anchor=W, bg="LightSteelBlue1")
l6.grid(row=3, column=3, columnspan=2, sticky=W, padx=5, pady=5)

l7 = Label(top_frame, text="Test type", bg="LightSteelBlue1")
l7.grid(row=4, column=0, sticky=W, padx=5, pady=5)

l8 = Label(top_frame, text="Lat", bg="LightSteelBlue1")
l8.grid(row=4, column=3, sticky=W, padx=5, pady=5)

l9 = Label(top_frame, text="Lon", bg="LightSteelBlue1")
l9.grid(row=4, column=5, sticky=W, pady=5)


sampleid_text = StringVar()
e1 = Entry(top_frame, textvariable=sampleid_text)
e1.grid(row=1, column=1, columnspan=2, padx=1, pady=5)

sample_depth_text = StringVar()
e2 = Entry(top_frame, textvariable=sample_depth_text)
e2.grid(row=1, column=5, columnspan=2, padx=1, pady=5)

core_id_text = StringVar()
e3 = Entry(top_frame, textvariable=core_id_text)
e3.grid(row=2, column=1, columnspan=2, padx=1, pady=5)

core_depth_float = StringVar()
e4 = Entry(top_frame, textvariable=core_depth_float)
e4.grid(row=2, column=5, columnspan=2, padx=1, pady=5)

core_type_text = StringVar()
e5 = ttk.Combobox(values=["Gravity", "Piston", "Vibro", "Other"], width=17)
e5.grid(row=3, column=1, columnspan=2, padx=1, pady=5)
test_type_text = e3

cruise_text = StringVar()
e6 = Entry(top_frame, textvariable=cruise_text)
e6.grid(row=3, column=5, columnspan=2, padx=1, pady=5)

test_type_text = StringVar()
e7 = ttk.Combobox(values=["R&B", "CRS", "TAS"], width=17)
e7.grid(row=4, column=1, columnspan=2, padx=1, pady=5)
test_type_text = e3

lat_text = StringVar()
e8 = Entry(top_frame, textvariable=lat_text, width=12)
e8.grid(row=4, column=4, sticky=W, padx=1, pady=5)

lon_text = StringVar()
e9 = Entry(top_frame, textvariable=lon_text, width=14)
e9.grid(row=4, column=6, sticky=W, padx=1, pady=5)


l11 = Label(top_frame, text="", bg="LightSteelBlue1")
l11.grid(row=5, column=0, sticky=W, padx=5, pady=1)

b9 = Button(top_frame, text="Clear all", width=8, height=3, bg="white", command=clear_fields)
b9.grid(row=1, column=7, columnspan=3, rowspan=2, padx=5, pady=5)


# b1 = Button(window, text="View all", width=12, bg="LightCyan2", command=view_command)
# b1.grid(row=5, column=5)

# b2 = Button(window, text="Find samples", width=12, bg="LightCyan2",command=search_command)
# b2.grid(row=6, column=5)

# b3 = Button(window, text="Add samples", width=12, bg="LightCyan2",command=add_command)
# b3.grid(row=7, column=5)

# b4 = Button(window, text="Update", width=12, bg="LightCyan2",command=update_command)
# b4.grid(row=8, column=5)

# b5 = Button(window, text="Delete sample", width=12, bg="LightCyan2",command=delete_command)
# b5.grid(row=9, column=5)

# b6 = Button(window, text="View samples", width=12, bg="light blue", command=on_samples)
# b6.grid(row=10, column=5, pady=5)

# b7 = Button(window, text="Exit", width=12, bg="rosy brown",command=on_closing)
# b7.grid(row=11, column=5, pady=5)

# b8 = Button(window, text="Open menu", width=12, bg="light blue",command=open_menu)
# b8.grid(row=11, column=0, pady=5, padx=5)



###############################################################
###############################################################
#### Central Frame ####

l1 = Label(center_frame, text="Grain size", bg="LightSteelBlue1")
l1.grid(row=7, column=0, sticky=W, padx=5, pady=5)
l1_1 = Label(center_frame, text="CL", width=4, bg="LightSteelBlue1")
l1_1.grid(row=7, column=1, sticky=W, padx=2, pady=5)
clay_text = StringVar()
e1_1 = Entry(center_frame, textvariable=clay_text, width=6)
e1_1.grid(row=7, column=2, padx=1, pady=5, sticky=W)
l1_2 = Label(center_frame, text="SL", width=4, bg="LightSteelBlue1")
l1_2.grid(row=7, column=3, sticky=W, padx=2, pady=5)
silt_text = StringVar()
e1_2 = Entry(center_frame, textvariable=silt_text, width=6)
e1_2.grid(row=7, column=4, padx=1, pady=5, sticky=W)
l1_3 = Label(center_frame, text="SD", width=4, bg="LightSteelBlue1")
l1_3.grid(row=7, column=5, sticky=W, padx=2, pady=5)
sand_text = StringVar()
e1_3 = Entry(center_frame, textvariable=sand_text, width=6)
e1_3.grid(row=7, column=6, padx=1, pady=5, sticky=W)
l1_4 = Label(center_frame, text="SD", width=4, bg="LightSteelBlue1")
l1_4.grid(row=7, column=7, sticky=W, padx=2, pady=5)
gravel_text = StringVar()
e1_4 = Entry(center_frame, textvariable=gravel_text, width=6)
e1_4.grid(row=7, column=8, padx=1, pady=5, sticky=W)

l2 = Label(center_frame, text="Atterberg limits", bg="LightSteelBlue1")
l2.grid(row=8, column=0, sticky=W, padx=5, pady=5)
l2_1 = Label(center_frame, text="PL", width=4, bg="LightSteelBlue1")
l2_1.grid(row=8, column=1, sticky=W, padx=2, pady=5)
pl_text = StringVar()
e2_1 = Entry(center_frame, textvariable=pl_text, width=6)
e2_1.grid(row=8, column=2, padx=1, pady=5, sticky=W)
l2_2 = Label(center_frame, text="LL", width=4, bg="LightSteelBlue1")
l2_2.grid(row=8, column=3, sticky=W, padx=2, pady=5)
ll_text = StringVar()
e2_2 = Entry(center_frame, textvariable=ll_text, width=6)
e2_2.grid(row=8, column=4, padx=1, pady=5, sticky=W)
l2_3 = Label(center_frame, text="PI", width=4, bg="LightSteelBlue1")
l2_3.grid(row=8, column=5, sticky=W, padx=2, pady=5)
pi_text = StringVar()
e2_3 = Entry(center_frame, textvariable=pi_text, width=6)
e2_3.grid(row=8, column=6, padx=1, pady=5, sticky=W)
l2_4 = Label(center_frame, text="LI", width=4, bg="LightSteelBlue1")
l2_4.grid(row=8, column=7, sticky=W, padx=2, pady=5)
pi_text = StringVar()
e2_4 = Entry(center_frame, textvariable=pi_text, width=6)
e2_4.grid(row=8, column=8, padx=1, pady=5, sticky=W)


l3 = Label(center_frame, text="In situ", bg="LightSteelBlue1")
l3.grid(row=9, column=0, sticky=W, padx=5, pady=5)
l3_1 = Label(center_frame, text="wc", width=4, bg="LightSteelBlue1")
l3_1.grid(row=9, column=1, sticky=W, padx=2, pady=5)
is_wc_text = StringVar()
e3_1 = Entry(center_frame, textvariable=is_wc_text, width=6)
e3_1.grid(row=9, column=2, padx=1, pady=5, sticky=W)
l3_2 = Label(center_frame, text="e\u2081", width=4, bg="LightSteelBlue1")
l3_2.grid(row=9, column=3, sticky=W, padx=2, pady=5)
is_void_text = StringVar()
e3_2 = Entry(center_frame, textvariable=is_void_text, width=6)
e3_2.grid(row=9, column=4, padx=1, pady=5, sticky=W)
l3_3 = Label(center_frame, text="G\u209B", width=4, bg="LightSteelBlue1")
l3_3.grid(row=9, column=5, sticky=W, padx=2, pady=5)
is_grain_text = StringVar()
e3_3 = Entry(center_frame, textvariable=is_grain_text, width=6)
e3_3.grid(row=9, column=6, padx=1, pady=5, sticky=W)
font_l3_4 = a = chr(0x03C3) + "'"
l3_4 = Label(center_frame, text=font_l3_4, width=4, bg="LightSteelBlue1")
l3_4.grid(row=9, column=7, sticky=W, padx=2, pady=5)
is_effstrs_text = StringVar()
e3_4 = Entry(center_frame, textvariable=is_effstrs_text, width=6)
e3_4.grid(row=9, column=8, padx=1, pady=5, sticky=W)

l4 = Label(center_frame, text="Compressibilities", bg="LightSteelBlue1")
l4.grid(row=10, column=0, sticky=W, padx=5, pady=5)
l4_1 = Label(center_frame, text="Cc", width=4, bg="LightSteelBlue1")
l4_1.grid(row=10, column=1, sticky=W, padx=2, pady=4)
cc_text = StringVar()
e4_1 = Entry(center_frame, textvariable=cc_text, width=6)
e4_1.grid(row=10, column=2, padx=1, pady=5, sticky=W)
l4_2 = Label(center_frame, text="Cs", width=4, bg="LightSteelBlue1")
l4_2.grid(row=10, column=3, sticky=W, padx=2, pady=5)
cs_text = StringVar()
e4_2 = Entry(center_frame, textvariable=cs_text, width=6)
e4_2.grid(row=10, column=4, padx=1, pady=5, sticky=W)
l4_3 = Label(center_frame, text="Cr", width=4, bg="LightSteelBlue1")
l4_3.grid(row=10, column=5, sticky=W, padx=2, pady=5)
cr_text = StringVar()
e4_3 = Entry(center_frame, textvariable=cr_text, width=6)
e4_3.grid(row=10, column=6, padx=1, pady=5, sticky=W)
font_l4_4 = a = chr(0x03B4) + chr(0x03B5) + '/' + chr(0x03B4) + 't'
l4_4 = Label(center_frame, text=font_l4_4, width=4, bg="LightSteelBlue1")
l4_4.grid(row=10, column=7, sticky=W, padx=2, pady=5)
strain_rate_text = StringVar()
e4_4 = Entry(center_frame, textvariable=strain_rate_text, width=6)
e4_4.grid(row=10, column=8, padx=1, pady=5, sticky=W)

l5 = Label(center_frame, text="Depostion", bg="LightSteelBlue1")
l5.grid(row=11, column=0, sticky=W, padx=5, pady=5)
l5_1 = Label(center_frame, text="e\u2080", width=4, bg="LightSteelBlue1")
l5_1.grid(row=11, column=1, sticky=W, padx=2, pady=4)
dep_void_text = StringVar()
e5_2 = Entry(center_frame, textvariable=dep_void_text, width=6)
e5_2.grid(row=11, column=2, padx=1, pady=5, sticky=W)
l5_2 = Label(center_frame, text="K\u2080", width=4, bg="LightSteelBlue1")
l5_2.grid(row=11, column=3, sticky=W, padx=2, pady=5)
depo_hydcon_text = StringVar()
e5_2 = Entry(center_frame, textvariable=depo_hydcon_text, width=6)
e5_2.grid(row=11, column=4, padx=1, pady=5, sticky=W)
l5_3 = Label(center_frame, text="Ss\u2080", width=4, bg="LightSteelBlue1")
l5_3.grid(row=11, column=5, sticky=W, padx=2, pady=5)
depo_store_text = StringVar()
e5_3 = Entry(center_frame, textvariable=depo_store_text, width=6)
e5_3.grid(row=11, column=6, padx=1, pady=5, sticky=W)
font_l5_4 = a = chr(0x03C3) + "'" + chr(0x209a) + chr(0x1d63) + chr(0x2091)
l5_4 = Label(center_frame, text=font_l5_4, width=4, bg="LightSteelBlue1")
l5_4.grid(row=11, column=7, sticky=W, padx=2, pady=5)
is_effstrs_text = StringVar()
e5_4 = Entry(center_frame, textvariable=is_effstrs_text, width=6)
e5_4.grid(row=11, column=8, padx=1, pady=5, sticky=W)

#### Bottom Frame ####
l10 = Label(bot_frame, text="Sample data:")
l10.grid(row=12, column=0, columnspan=9, sticky=NW, padx=5, pady=5) 

list1 = Listbox(bot_frame, height=14, width=80)
list1.grid(row=13, column=0, rowspan=4, columnspan=8, padx=5, sticky=NW)
sb1 = Scrollbar(bot_frame, activebackground="black", relief="raised")
sb1.grid(row=13, column=7, rowspan=4, padx=5, sticky=NW)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
l10x = Label(bot_frame, text="Sample data:", bg="LightSteelBlue1")
l10x.grid(row=17, column=0, sticky=NW, padx=5, pady=6)


list1.bind('<<ListboxSelect>>')

window.mainloop()
