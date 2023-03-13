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

# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
#
# print(add(3, 5, 6))

# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)
#
#
# print(bar(1, 2))


# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)
#
#
# bar(toast='nah', spam=4, eggs=2)

# def test(*args):
#     print(args)
#
#
# print(test(1, 2, 3, 5))

def all_aboard(a, *args, **kw):
    print(a, args, kw)


print(all_aboard(4, 7, 3, 0, x=10, y=64))




