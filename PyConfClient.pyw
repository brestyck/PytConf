# -*- coding: utf-8 -*- 

import socket
import tkinter

tk=tkinter.Tk()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0',5081))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

text=tkinter.StringVar()
name=tkinter.StringVar()
name.set('Your name')
text.set('')
tk.title('PYTCONF')
tk.geometry('200x300')

log = tkinter.Text(tk)
nick = tkinter.Entry(tk, textvariable=name)
msg = tkinter.Entry(tk, textvariable=text)
msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both',expand='true')

def loopproc():
	log.see(tkinter.END)
	s.setblocking(False)
	try:
		message = s.recv(12800).decode("utf-8")
		log.insert(tkinter.END,message+'\n')
	except:
		tk.after(1,loopproc)
		return
	tk.after(1,loopproc)
	return

def sendproc(event):
	sock.sendto ((name.get()+':'+text.get()).encode("utf-8"),('255.255.255.255',5081))
	text.set('')

msg.bind('<Return>',sendproc)

msg.focus_set()

tk.after(1,loopproc)
tk.mainloop()