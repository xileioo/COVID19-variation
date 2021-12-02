# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 16:40:37 2021

@author: lixue
"""
from tkinter import*
from tkinter.messagebox import*
#from tkinter.ttk import *
from tkinter import ttk
import os
import numpy as np
import matplotlib.pylab as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
                                               NavigationToolbar2Tk)
        
v_table = {}
range_table = {}
# Ckeck string could convert to float or not 
# =============================================================================
# def is_float(value):
#   try:
#     float(value)
#     return True
#   except:
#     return False
# =============================================================================

def write():
    with open('1_variation_COVID19_Sarbecovirus.csv') as file:
        next(file)
        for line in file:
            line = line.rstrip('\n')
            loc,A,Matchcount_COVID19,variation_COVID19,\
                Matchcount_Sarbecovirus,variation_Sarbecovirus,\
                loc2,loc3=line.split(',')
            loc3.rstrip('\n')
            tmp = '_'.join([loc3,loc,Matchcount_COVID19,variation_COVID19,Matchcount_Sarbecovirus,variation_Sarbecovirus])
            variation_COVID19 = float("{:.4f}".format(float(variation_COVID19))) * 100
            variation_Sarbecovirus = float("{:.3f}".format(float(variation_Sarbecovirus))) * 100
            variation_COVID19 = str(variation_COVID19)
            variation_Sarbecovirus = str(variation_Sarbecovirus)
            v_table[loc3] = [loc,variation_COVID19,variation_Sarbecovirus]
            v_table[loc2] = [loc,variation_COVID19,variation_Sarbecovirus]


# def search1(): # search single loc
#     x = singleloc_text.get()
#     try:
#         if int(x) >= 1 & int(x) <= 201:
#             loc = v_table[x][0]
#             variation_COVID19 = v_table[x][1]
#             variation_Sarbecovirus = v_table[x][2]
#             string =  'Loc: ' + loc + '\nCOVID19 Variation: ' + variation_COVID19 + '%\nSarbecovirus Variation: ' + variation_Sarbecovirus + '%'
#             messagebox.showinfo(title='N331-T531:1-201', message = string)
#         else:
#             if int(x) >= 331 & int(x) <= 531:
#                 variation_COVID19 = v_table[x][1]
#                 variation_Sarbecovirus = v_table[x][2]
#                 string =  'Loc: ' + loc + '\nCOVID19 Variation: ' + variation_COVID19 + '%\nSarbecovirus Variation: ' + variation_Sarbecovirus + '%'
#                 messagebox.showinfo(title='N331-T531:1-201', message = string)
#     except KeyError:
#         showwarning('warning','Please enter the correct loc:1-201 or 331-531')
        

def search2(): # search locs by range
    x = rangeloc_text.get()
    start, end = x.split('-')
    try:
        if int(start) >=1 & int(start) <= 201 & int(end) >=1 & int(end) <= 201:
            for i in range(int(start), int(end)+1):
                range_table[i] = v_table[str(i)]
        else:
            if int(start) >=331 & int(start) <= 531 & int(end) >=331 & int(end) <= 531:
                for i in range(int(start), int(end)):
                    range_table[i] = v_table[str(i)]
            else:
                showwarning('warning','Please enter the correct range:1-201 or 331-531')
            
    except KeyError:
        showwarning('warning','Please enter the correct range:1-201 or 331-531')

def search3(): # search multiple locs
    x = multiloc_text.get()
    loc_list = x.split(',')
    for loc in loc_list:
        if (int(loc) >=1 & int(loc) <= 201) | (int(loc) >=331 & int(loc) <= 531):
            range_table[int(loc)] = v_table[str(loc)]
        else:
            showwarning('warning','Please enter the loc use comma-separated values: 12,14,30')


def build_table():
    if rangeloc_text.get():
        search2()
    elif multiloc_text.get():
        search3()
    else: 
        showwarning('warning','Please refer to the example')
    win=Tk()
    win.geometry('500x400+800+100')      
    tree=ttk.Treeview(win,height=40)
    tree["columns"]=("loc","variation_COVID19","variation_Sarbecovirus")
    tree.column("loc",width=60) 
    tree.column("variation_COVID19",width=150)
    tree.column("variation_Sarbecovirus",width=150)
    
    tree.heading("loc",text="loc")
    tree.heading("variation_COVID19",text="variation_COVID19")
    tree.heading("variation_Sarbecovirus",text="variation_Sarbecovirus")
    
    for key in range_table:
        tree.insert("",key, text=key, values=range_table[int(key)])
        #print(key)
        #range_table.pop(int(key))
    tree.pack()
    win.mainloop()


def plot_heatmap():
    plot_win = Tk()
    plot_win.geometry('800x500+800+200')   
    pdata = []
    loc_names = []
    y_names = ['COVID19','Sarbecovirus']
    for key in range_table:
        #print(key)
        #print(range_table[key])
        loc_names = np.append(loc_names,range_table[key][0])
        tmp = [float(range_table[key][1]),float(range_table[key][2])]
        #print(tmp)
        pdata = np.append(pdata,tmp,axis=0)
    pdata = np.array(pdata).reshape(-1,2)
    pdata = np.transpose(pdata)
    #print(loc_names)
    figure = Figure(figsize=(10,10))
    figure,ax = plt.subplots(figsize=(80, 80))
    im = ax.imshow(pdata)
    ax.set_xticks(np.arange(len(loc_names)))
    ax.set_xticklabels(loc_names,rotation=90)
    ax.set_yticks(np.arange(len(y_names)))
    ax.set_yticklabels(y_names)
    ax.tick_params(axis='both', which='major', labelsize=15)

    canvas = FigureCanvasTkAgg(figure, plot_win)                
    canvas.get_tk_widget().pack()    

def clear_record():
    global range_table
    range_table = {}
    
# 创建GUI窗口，使用Tk()函数，并且插入两个Combobox和一个按钮。
write()
root = Tk()
root.title("Search Variation")
root.geometry('500x300+100+200')      

# # search one loc
# l1 = Label(root, text="single loc：(1-201 or 331-531)")
# l1.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
# singleloc_text = StringVar()
# singleloc = Entry(root, textvariable = singleloc_text)
# #xls_text.set(" ")
# singleloc.pack()

# Button(root, text="press", command = search1).pack()

# search loc range
l2 = Label(root, text="range loc：(example: 10-14)")
l2.pack()  #这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
rangeloc_text = StringVar()
rangeloc = Entry(root, textvariable = rangeloc_text)
#xls_text.set(" ")
rangeloc.pack()

Button (root, text='Search',command = build_table).pack()

# search multi loc
l3 = Label(root, text="multiple loc：(example: 12,14,30)")
l3.pack()
multiloc_text = StringVar()
multiloc = Entry(root, textvariable = multiloc_text)
#xls_text.set(" ")
multiloc.pack()

Button (root, text='Search',command = build_table).pack()

Button (root, text='plot-heatmap',command = plot_heatmap).pack(padx=15, pady=15)

btn_clear = Button (root, text='clear-record',command = clear_record, 
                    bg='#567',fg='White')
btn_clear.pack(padx=15, pady=18)

root.mainloop()





