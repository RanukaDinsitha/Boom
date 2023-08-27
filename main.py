# Imports

from tkinter import *

# Imports

# Main Code

compiler = Tk()
compiler.title("Boom! Code! [v.1.0.6]")


def run():
    print("[boom]: Code Is Being Runned")


menu_bar = Menu(compiler)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
run_bar.add_command(label="Run")
menu_bar.add_cascade(label="Run", menu=run_bar)
compiler.config(menu=menu_bar)

editor = Text()
editor.pack()
compiler.mainloop()

# Main Code
