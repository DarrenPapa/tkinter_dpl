if __name__ != "__dpl__":
	raise Exception("This project is used for DPl!")

import tkinter as tk

temp = {
	"version":"0.1.0",
	"help":"Documentation will be soon written. As of now look at the readme in`https://github.com/DarrenPapa/tkinter_dpl/`"
}

@add_func(frame=temp)
def tk_window(_, __, title=None, geometry=None):
	temp =  tk.Tk()
	if title is not None:
		temp.title(title)
	if geometry is not None:
		temp.geometry(geometry)
	return temp,

@add_func(frame=temp)
def tk_label(_, __, root, text="Label"):
	return tk.Label(root, text=text),

@add_func(frame=temp)
def tk_button(_, __, root, text="Button", command=None):
	return tk.Button(root, text=text, command=command),

@add_func(frame=temp)
def tk_pack(_, __, obj, *args, **kwargs):
	obj.pack(*args, **kwargs)

@add_func(frame=temp)
def tk_config(_, __, obj, *args, **kwargs):
	obj.config(*args, **kwargs)

@add_func(frame=temp)
def tk_grid(_, __, obj, *args, **kwargs):
	obj.grid(*args, **kwargs)

@add_func(frame=temp)
def tk_mainloop(_, __, tk_window):
	tk_window.mainloop()

varproc.rset(frame[-1], "_mods.py.tkinter", temp)