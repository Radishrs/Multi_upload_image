import tkinter as tk
#import tkinter.ttk
from tkinter import filedialog
import savepix3

fn = ''


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
    global fn
    big, mini = savepix3.get_image_url(savepix3.send(fn))
    textbox.insert('end', '\n--------------\n')
    textbox.insert('end', 'Orig: ' + big + '\n')
    textbox.insert('end', 'Prev: ' + mini + '\n')
    textbox.insert('end', '--------------\n')

root = tk.Tk()

panelFrame = tk.Frame(root, height=40, bg='gray')
textFrame = tk.Frame(root, height=340, width=600)

panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

textbox = tk.Text(textFrame, font='Arial 10', wrap='word')
scrollbar = tk.Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

loadBtn = tk.Button(panelFrame, text='Load')
sendBtn = tk.Button(panelFrame, text='send')
quitBtn = tk.Button(panelFrame, text='quit')

loadBtn.bind('<Button-1>', load_file)
sendBtn.bind('<Button-1>', send)
quitBtn.bind('<Button-1>', quit)

loadBtn.place(x=10, y=10, width=40, height=20)
sendBtn.place(x=60, y=10, width=40, height=20)
quitBtn.place(x=110, y=10, width=40, height=20)

root.mainloop()
