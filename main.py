# import tkinter
#
# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
#
# #Label
# my_label = tkinter.Label(text="I Am a label", font=("Arial", 24, "bold"))
# my_label.pack()
#
#
#
#
# window.mainloop()

def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(3, 5, 6))






