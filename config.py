__author__ = 'Administrator'
# -*- coding: cp936 -*-
from tkinter import *
import sys
root = Tk()
root.title("GUI")
root.geometry('500x700')

def config():
    global vlist
    for i in range(0,10):
        vlist[i]=vlist[i].get()
    f=open('config.json','w')
    f.write('{\n')
    for i in range (0,10):
        s='   '+'"'+str[i]+'":'+'"'+vlist[i]+'"'
        f.write(s)
        if i!=9:
            f.write(',')
        f.write('\n')
    f.write('}')
    vlist=[remote_control_host,
    remote_control_port,
    local_host,
    local_port,
    remote_host,
    remote_port,
    number,
    local_cert,
    local_cert_pub,
    remote_cert,]
def read():
    global vlist
    s=open('config.json','r').read()
    s=eval(s)
    for i in range(0,10):
        vlist[i].delete(0,END)
    for i in range(0,10):
        vlist[i].insert(0,s[str[i]])
def clear():
    for i in range(0,10):
        vlist[i].delete(0,END)
global str,vlist
Label(root, text="*remote control host", font=("Arial", 12), height=2).pack(side=TOP)
remote_control_host = Entry(root)
remote_control_host.pack(side=TOP)
Label(root, text="remote control port", font=("Arial", 12), height=2).pack(side=TOP)
remote_control_port = Entry(root)
remote_control_port.pack(side=TOP)
Label(root, text="local host", font=("Arial", 12), height=2).pack(side=TOP)
local_host = Entry(root)
local_host.pack(side=TOP)
Label(root, text="local port", font=("Arial", 12), height=2).pack(side=TOP)
local_port = Entry(root)
local_port.pack(side=TOP)
Label(root, text="remote host", font=("Arial", 12), height=2).pack(side=TOP)
remote_host = Entry(root)
remote_host.pack(side=TOP)
Label(root, text="remote port", font=("Arial", 12), height=2).pack(side=TOP)
remote_port = Entry(root)
remote_port.pack(side=TOP)
Label(root, text="number", font=("Arial", 12), height=2).pack(side=TOP)
number = Entry(root)
number.pack(side=TOP)
Label(root, text="*local cert", font=("Arial", 12), height=2).pack(side=TOP)
local_cert = Entry(root)
local_cert.pack(side=TOP)
Label(root, text="*local cert pub", font=("Arial", 12), height=2).pack(side=TOP)
local_cert_pub = Entry(root)
local_cert_pub.pack(side=TOP)
Label(root, text="*remote cert", font=("Arial", 12), height=2).pack(side=TOP)
remote_cert = Entry(root)
remote_cert.pack(side=TOP)
Label(root).pack(side=TOP)
frm=Frame(root)
Button(frm, text="config", command = config).pack(side=LEFT)
Button(frm, text="import", command = read).pack(side=LEFT)
Button(frm, text="clear", command = clear).pack(side=LEFT)
frm.pack()
vlist=[remote_control_host,
    remote_control_port,
    local_host,
    local_port,
    remote_host,
    remote_port,
    number,
    local_cert,
    local_cert_pub,
    remote_cert,]
str=[
    "remote_control_host",
    'remote_control_port',
    "local_host",
    "local_port",
    "remote_host",
    "remote_port",
    "number",
    "local_cert",
    "local_cert_pub",
    "remote_cert",
]
root.mainloop()