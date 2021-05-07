from datetime import datetime
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("700x170")
root.resizable(False,False)
root.configure(bg='#00ffff')
vlist = ["January","February","March","April","May","June","July","August","September","October","November","December"]

vlist2 = list(range(1,32))

vlist3 = list(range(1900,2100))

vlist4 = list(range(1,30))

Combo = ttk.Combobox(root, values = vlist, state='writeonly')
Combo.set("Pick a month")
Combo.place(x = 150 , y= 60)

Combo2 = ttk.Combobox(root, values = vlist2, state='writeonly')
Combo2.set("Pick a day")
Combo2.place( x = 310 , y= 60)

Combo3 = ttk.Combobox(root, values = vlist3, state='writeonly')
Combo3.set("Pick a year")
Combo3.place(x = 470 , y = 60)

def retrieve():
    medicine_info = medicine.get()

    time_info = time.get()

    if Combo.get() == "April":
        Combo2["values"] = (vlist4)
    else:
        Combo2["values"] = (vlist2)

    combo_info = Combo.get()

    combo2_info = Combo2.get()

    combo3_info = Combo3.get()

    print(medicine_info,time_info,combo_info, combo2_info, combo3_info)

    file = open("sample.txt1","a")

    file.write("MEDICINE NAME :" + medicine_info)

    file.write("\n")

    file.write("TIME OF THE DAY :" + time_info)

    file.write("\n")

    file.write("MONTH :" + str(combo_info))

    file.write("\n")

    file.write("DAY :" + str(combo2_info))

    file.write("\n")

    file.write("YEAR :" + str(combo3_info))

    file.close()

date = Label(root ,text="DATE",font = ('times',12))
date.place(x = 10 , y = 60)

medicine_txt = Label(text="MEDICINE NAME",font = ('times',12))
medicine_txt.place(x = 10 , y = 30)
medicine = StringVar()
medicine_entry = Entry(textvariable=medicine,width="30")
medicine_entry.place(x = 150 , y = 30)

time_txt = Label(text = "TIME",font = ('times',12))
time_txt.place(x = 10 , y = 90)
time = StringVar()
time_entry = ttk.Combobox(textvariable = time, width = "30", values=("9'o clock","10'o clock","11'o clock","12'o clock","1'0 clock","2'o clock","3'o clock","4'o clock","5'o clock","6'o clock","7'o clock","8'o clock"))
time_entry.place(x = 150 , y = 90)

Button = Button(root, text = "SUMBIT", command = retrieve,font=('times',12))
Button.place(x = 30 , y = 120)

root.title('MEDICINE DATABASE')
root.mainloop()
