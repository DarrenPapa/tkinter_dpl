if __name__ != "__dpl__":
	raise Exception("This project is used for DPl!")

import tkinter as tk

temp = {
	"version":"0.1.0",
	"help":"Documentation will be soon written. As of now look at the readme in`https://github.com/DarrenPapa/tkinter_dpl/`",
	"start_text_2d":"1.0",
	"start_text":"0",
	"end":tk.END
}

@add_func(frame=temp)
def tk_window(_, __, title=None, geometry=None, **kwargs):
	temp =  tk.Tk(**kwargs)
	if title is not None:
		temp.title(title)
	if geometry is not None:
		temp.geometry(geometry)
	def window_config(_, __, *args, **kwargs):
		temp.config(*args, **kwargs)
	return window_config, temp

@add_func(frame=temp)
def tk_toplevel(_, __, title=None, geometry=None, **kwargs):
	temp =  tk.Tk(**kwargs)
	if title is not None:
		temp.title(title)
	if geometry is not None:
		temp.geometry(geometry)
	def window_config(_, __, *args, **kwargs):
		temp.config(*args, **kwargs)
	return window_config, temp

@add_func(frame=temp)
def tk_label(_, __, root, text="Label", **kwargs):
	return tk.Label(root, text=text, **kwargs),

@add_func(frame=temp)
def tk_entry(_, __, root, **kwargs):
	return tk.Entry(root, **kwargs),

@add_func(frame=temp)
def tk_text(_, __, root, **kwargs):
	return tk.Text(root, **kwargs),

@add_func(frame=temp)
def tk_button(_, __, root, text="Button", command=None, **kwargs):
	return tk.Button(root, text=text, command=command, **kwargs),

@add_func(frame=temp)
def tk_grid(_, __, obj, *args, **kwargs):
	obj.grid(*args, **kwargs)

@add_func(frame=temp)
def tk_pack(_, __, obj, *args, **kwargs):
	obj.pack(*args, **kwargs)

@add_func(frame=temp)
def tk_pack_forget(_, __, obj):
	obj.pack_forget()

@add_func(frame=temp)
def tk_forget(_, __, obj):
	obj.forget()

@add_func(frame=temp)
def tk_config(_, __, obj, *args):
	obj.config(*args, **kwargs)

@add_func(frame=temp)
def tk_call_method(_, __, obj, method, *args, **kwargs):
	if not hasattr(obj, method):
		return f"err:{error.RUNTIME_ERROR}:Object {obj} does not have method {method!r}!"
	return getattr(obj, method)(*args, **kwargs),

@add_func(frame=temp)
def tk_mainloop(_, __, tk_window):
	tk_window.mainloop()

varproc.rset(frame[-1], "_mods.py.tkinter", temp)