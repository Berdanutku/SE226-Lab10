import tkinter as tk
r=tk.Tk()
r.title("Marvel")

def Read():
    textBox.delete("1.0",tk.END)
    file=open("Marvel.txt")
    text = file.read()
    textBox.insert("end", text)

def Calculate():
    textBox.delete('1.0', tk.END)
    file=open("Marvel.txt")
    a = file.read()
    list = []
    for i in a.split():
        list.append(i)

    for i in list:
        x=str("The frequency of "+ str(i)+ ":"+ str(list.count(i))+ "\n")
        textBox.insert(tk.INSERT, (x))

    textBox.pack()

l1=tk.Label(r,text="Press the READ button to read the file.\n Press the CALCULATE button to calculate the word frequency.")
l1.pack()

textBox = tk.Text()
textBox.pack()

b1=tk.Button(text="READ",bg="orange",fg="black",font="helvetica 20",command=Read)
b1.pack()

b2=tk.Button(text="CALCULATE",bg="orange",fg="black",font="helvetica 20",command=Calculate)
b2.pack()

r.mainloop()