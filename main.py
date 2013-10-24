import tkinter as tk
#import tkinter.ttk
from tkinter import filedialog
from mod import savepix

import sql

fn = ''
big = ''
small = ''


def quit(ev):
    global root
    root.destroy()


def load_file(ev):
    global fn
    fn = filedialog.Open(root, filetypes=[('*.jpg files', '.jpg')]).show()
    if fn == '':
        return
    else:
        textbox.insert('end', 'file: ')
        textbox.insert('end', fn)


def send(ev):
    global fn, big, small
    big, small = savepix.get_image_url(savepix.send(fn))
    textbox.insert('end', '\n--------------\n')
    textbox.insert('end', 'Orig: ' + big + '\n')
    textbox.insert('end', 'Prev: ' + small + '\n')
    textbox.insert('end', '--------------\n')


def save_to_db(ev):
    sql.add_url('table1', 1, big, small)


root = tk.Tk()

button_panel_frame = tk.Frame(root, height=20, bg='gray')
textFrame = tk.Frame(root, height=340, width=600)

button_panel_frame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

textbox = tk.Text(textFrame, font='Arial 10', wrap='word')
scrollbar = tk.Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')


def add_button_to_panel(name, func, bt_panel=button_panel_frame):
    new_button = tk.Button(bt_panel, text=name)
    new_button.bind('<Button-1>', func)

    try:
        add_button_to_panel.x += 40
    except AttributeError:
        add_button_to_panel.x = 0

    new_button.place(x=add_button_to_panel.x, y=0, width=40, height=20)


add_button_to_panel('Load', load_file)
add_button_to_panel('Send', send)
add_button_to_panel('Quit', quit)
add_button_to_panel('Save', save_to_db)

#loadBtn = tk.Button(button_panel_frame, text='Load')
#sendBtn = tk.Button(button_panel_frame, text='send')
#quitBtn = tk.Button(button_panel_frame, text='quit')
#
#loadBtn.bind('<Button-1>', load_file)
#sendBtn.bind('<Button-1>', send)
#quitBtn.bind('<Button-1>', quit)
#
#loadBtn.place(x=10, y=10, width=40, height=20)
#sendBtn.place(x=60, y=10, width=40, height=20)
#quitBtn.place(x=110, y=10, width=40, height=20)

root.mainloop()
