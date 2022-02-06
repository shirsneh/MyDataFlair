from tkinter import *
import base64

# initialize window
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root['background'] = '#FFDAB9'
root.title("MyDataFlair - Message Encode and Decode")
Label(root, text='ENCODE DECODE', font='david 20 bold', bg='#FFDAB9').place(x=130, y=30)
Label(root, text='MyDataFlair', font='david 16 bold', bg='#FFDAB9').pack(side=BOTTOM)

# define variables
Text = StringVar()
Private_key = StringVar()
Mode = StringVar()
Result = StringVar()


# define function
# function to encode
def encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# function to decode
def decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


# function to set mode
def mode():
    if Mode.get() == 'e':
        Result.set(encode(Private_key.get(), Text.get()))
    elif Mode.get() == 'd':
        Result.set(decode(Private_key.get(), Text.get()))
    else:
        Result.set('Invalid mode')


# Function to exit window
def Exit():
    root.destroy()


# Function to reset
def reset():
    Text.set("")
    Private_key.set("")
    Mode.set("")
    Result.set("")


# Message
Label(root, font='david 12 bold', text='Message', bg='#FFDAB9').place(x=100, y=80)
Entry(root, font='david 10', textvariable=Text, bg='ghost white').place(x=300, y=80)

# key
Label(root, font='david 12 bold', text='Key', bg='#FFDAB9').place(x=100, y=110)
Entry(root, font='david 10', textvariable=Private_key, bg='ghost white').place(x=300, y=110)

# mode
Label(root, font='david 12 bold', text='Mode(e-encode, d-decode)', bg='#FFDAB9').place(x=100, y=140)
Entry(root, font='david 10', textvariable=Mode, bg='ghost white').place(x=300, y=140)

# result
Entry(root, font='david 10 bold', textvariable=Result, bg='ghost white').place(x=300, y=170)
# result button
Button(root, font='david 10 bold', text='Result', padx=2, bg='LightGray', command=mode).place(x=100, y=170)

# reset button
Button(root, font='david 10 bold', text='Reset', width=6, command=reset, bg='LightGray', padx=2).place(x=160, y=200)

# exit button
Button(root, font='david 10 bold', text='Exit', width=6, command=Exit, bg='LightGray', padx=2, pady=2).place(x=250,
                                                                                                             y=200)
root.mainloop()
