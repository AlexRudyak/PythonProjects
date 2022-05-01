# GUI with Tkinter
import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
frame1 = tk.Frame(master=window).pack()
frame2 = tk.Frame().pack()
frame3 = tk.Frame().pack()
# Minimum Power #######
label = tk.Label(
    text="Input Minimum Power:",
    foreground = "white",
    background = "#34A2FE",
    master=frame1
).pack(side=tk.LEFT)

entry = tk.Entry(
    width=3,
    master=frame1
).pack(side=tk.LEFT)
#######################
# Maximum Power #######
label = tk.Label(
    text="Input Maximum Power:",
    foreground = "white",
    background = "#34A2FE",
    master=frame2
).pack(side=tk.LEFT)

entry = tk.Entry(
    width=3,
    master=frame2
).pack(side=tk.LEFT)
#######################
# dB Increment ########
label = tk.Label(
    text="dB Increments:",
    foreground = "white",
    background = "#34A2FE",
    master=frame3
).pack(side=tk.LEFT)

entry = tk.Entry(
    width=3,
    master=frame3
).pack(side=tk.LEFT)
#######################
window.mainloop()
