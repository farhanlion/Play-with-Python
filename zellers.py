#zellers function
def zellers(month, day, year):
    '''Returns the day of week of a given date.'''
    month_dict={'january': 11, 'february': 12, 'march': 1, 'april': 2, 'may': 3, 'june': 4, 'july': 5, 'august': 6, 'september': 7, 'october': 8, 'november': 9, 'december': 10}
    month = month.lower()
    A = month_dict.get(month)
    B=int(day)
    year_adjusted=(int(year))
    if A == 11 or A == 12 :
        year_adjusted = year_adjusted - 1
    C=year_adjusted % 100
    D=int(year_adjusted // 100)
    
    W = int((13*A - 1) / 5)
    X = int(C / 4)
    Y = int(D / 4)
    Z = int(W + X + Y + B + C - 2*D)
    R = Z%7

    dayofweek_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Tuhrsday', 'Friday', 'Saturday']
    dayofweek = dayofweek_list[R]
    return dayofweek

#GUI
from Tkinter import *
import tkMessageBox
root = Tk()
root.minsize(width =500, height = 150)
root.maxsize(width =500, height = 150)
root.title("Zeller's Algorithm")

def gui_function():
    month = str(month_entry.get())
    day = int(day_entry.get())
    year = int(year_entry.get())

    month_dict={'january': 11, 'february': 12, 'march': 1, 'april': 2, 'may': 3, 'june': 4, 'july': 5, 'august': 6, 'september': 7, 'october': 8, 'november': 9, 'december': 10}
    if str(month.lower()) not in month_dict:
        tkMessageBox.showerror("Error", "The month is invalid, please try again.\ne.g. January")
    elif day < 1 or day > 31 :
        tkMessageBox.showerror("Error", "The day is invalid, please try again, it should between 1 and 31.\ne.g. 31")
    elif year < 1000 or year > 9999:
        tkMessageBox.showerror("Error", "The year is invalid, please try again, it should between 1000 and 9999.\ne.g. 2000")
    else:
        result = zellers(month, day, year)
        tkMessageBox.showinfo("Day of Week", str(month.capitalize())+" "+str(day)+", "+str(year)+" is " +str(result)+".")
        
month_label = Label(root, text="Month: ", width = 10, height = 1, bd=5).grid(row=1, column=1, sticky=E+W)
day_label = Label(root, text="Day: ", width = 10, height = 1, bd=5).grid(row=2, column=1, sticky=E+W)
year_label = Label(root, text="Year: ", width = 10, height = 1, bd=5).grid(row=3, column=1, sticky=E+W)

month_entry = Entry(root, width = 10, justify='center')
month_entry.grid(row=1, column=2, sticky=E+W)
month_entry.focus_set()
day_entry = Entry(root, width = 10, justify='center')
day_entry.grid(row=2, column=2, sticky=E+W)
year_entry = Entry(root, width = 10, justify='center')
year_entry.grid(row=3, column=2, sticky=E+W)

button = Button(root, text = "Get the day of week", height = 3, width = 20, command = gui_function).grid(row=1, column=3, rowspan = 3)

root.mainloop()
