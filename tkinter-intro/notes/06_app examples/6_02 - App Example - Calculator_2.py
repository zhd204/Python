# Example from https://github.com/CharlesPikachu/Tools/tree/master/Calculator
# Colors from https://www.rapidtables.com/web/color/RGB_Color.html
import tkinter as tk
import math

win = tk.Tk()
win.resizable(0, 0)

current_show = tk.StringVar()
current_show.set("0")  # support up to 46 characters

memory = ""  # track the math expression in the memory
expression = ""  # track the live math expression
is_calc = False  # current expression is in calculation process (e.g. after "+" is pressed)
is_result = False  # current displayed value is a result of one kind of calculation (e.g. after "=" or "sqrt" is pressed)


# press MC button to clear memory
def btn_mc_clicked():
    global memory
    memory = ""
    print(f"memory: {memory}")


# press MR button to read the calculation result from the memory
def btn_mr_clicked():
    global memory
    global is_result

    if len(memory) == 0:
        current_show.set("0")
    else:
        current_show.set(str(eval(memory)))
        is_result = True
    print(f"memory: {memory}")


# press MS button to save the current displayed value into memory
# existing memory contents will be replaced
def btn_ms_clicked():
    global memory

    memory = current_show.get()
    print(f"memory: {memory}")


# press M+ button to add current displayed value to memory
def btn_mplus_clicked():
    global memory
    memory = memory + "+" + current_show.get()
    print(f"memory: {memory}")


# press M- button to subtract current displayed value from memory
def btn_mminus_clicked():
    global memory
    memory = memory + "-" + current_show.get()
    print(f"memory: {memory}")


# buttons 0 - 9, .
def btn_numbers_clicked(number):
    global expression
    global current_show
    global is_calc
    global is_result

    if current_show.get() == "0" and number == "0":  # do not take 0 if current value is 0
        pass
    else:
        if current_show.get() == "0":
            current_show.set(number)
        elif is_calc:
            current_show.set(number)
            is_calc = False
        elif is_result:
            expression = ""
            current_show.set(number)
            is_result = False
        else:
            current_show.set(current_show.get() + number)

        if len(expression) > 0 and expression[-1] == "0":  # avoid string with leading 0 (e.g. 02) being recorded in expression
            expression = expression[:-1]
        expression = expression + number

    print(expression)


# buttons + - * / %
def btn_math_clicked(operator):
    global expression
    global is_calc
    global is_result

    if is_result:  # continue to calculate on top of the previous result
        expression = current_show.get()
        is_result = False

    expression = expression + operator
    is_calc = True

    print(expression)


# button 1/x
def btn_invert_clicked():
    global expression
    global current_show
    global is_result

    try:
        inverted_value = 1 / float(current_show.get())
        current_show.set(str(inverted_value))
        is_result = True
    except:
        current_show.set("Invalid Operation\nReset Required!")  # 1/0 case
        is_result = False

    print(expression)


# button equal
def btn_equal_clicked():
    global expression
    global current_show
    global is_calc
    global is_result

    if len(expression) == 0:
        result = "0"
    else:
        try:
            result = str(eval(expression))
        except:
            result = "Invalid Operation\nReset Required!"   # 1/0 case
    current_show.set(result)
    is_result = True
    is_calc = False

    print(expression)


# button del, delete the last digit of current display until it becomes 0.
def btn_del_clicked():
    global expression
    global current_show
    global is_result

    if current_show.get() == "0":
        pass
    if is_result:  # button del does not work on a result
        pass
    else:
        current_value_length = len(current_show.get())
        if current_value_length == 1:
            current_show.set("0")
        else:
            current_show.set(current_show.get()[: -1])

        expression = expression[:-current_value_length]
        expression += current_show.get()

    print(expression)


# button CE, reset current show (clean what are displaying)
def btn_ce_clicked():
    global expression
    global current_show
    global is_result

    if current_show.get() == "0":
        pass
    if is_result:
        current_show.set("0")
        expression = ""
        is_result = False
    else:
        current_value = current_show.get()
        current_value_length = len(current_value)
        expression_last_section = expression[-current_value_length:]
        if current_value == expression_last_section:
            expression = expression[:-current_value_length]
        current_show.set("0")

    print(expression)


# button C, reset everything (reboot)
def btn_c_clicked():
    global expression
    global current_show
    global is_calc
    global is_result
    global memory

    memory = ""
    expression = ""
    is_calc = False
    is_result = False
    current_show.set("0")

    print(expression)


# button reverse, change the +/- sign of current displayed value
def btn_reverse_clicked():
    global expression
    global current_show

    if current_show.get() == "0":
        pass
    else:
        current_value = current_show.get()
        current_value_length = len(current_value)
        reversed_value = ""

        if current_value[0] != "-":
            reversed_value = "-" + current_value
        else:
            reversed_value = current_value[1:]
        current_show.set(reversed_value)

        expression_last_section = expression[-current_value_length:]
        if current_value == expression_last_section:
            expression = expression[:-current_value_length]
            expression += reversed_value

    print(expression)


# button square root
def btn_sqrt_clicked():
    global expression
    global current_show
    global is_result

    sqrt_value = math.sqrt(float(current_show.get()))
    current_show.set(str(sqrt_value))
    is_result = True

    print(expression)


def demo():
    win.title("Simple Calculator")
    win.geometry("320x380")

    # display
    display = tk.Label(win, textvariable=current_show, bg="#000000", fg="#FFFFFF", font=('Courier New', 20, "bold"),
                       anchor=tk.E, relief=tk.SUNKEN, padx=2, wraplength=280)
    display.place(x=20, y=30, width=280, height=50)

    # row 1 for memory buttons
    # https://stackoverflow.com/questions/1529847/how-to-change-the-foreground-or-background-colour-of-a-tkinter-button-on-mac-os
    btn_mc = tk.Button(win, text="MC", highlightbackground="#C0C0C0", fg="#000000",
                       font=('Courier New', 12, "bold"), command=lambda: btn_mc_clicked())
    btn_mc.place(x=20, y=90, width=50, height=35)

    btn_mr = tk.Button(win, text="MR", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                       command=lambda: btn_mr_clicked())
    btn_mr.place(x=77.5, y=90, width=50, height=35)

    btn_ms = tk.Button(win, text="MS", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                       command=lambda: btn_ms_clicked())
    btn_ms.place(x=135, y=90, width=50, height=35)

    btn_mplus = tk.Button(win, text="M+", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                          command=lambda: btn_mplus_clicked())
    btn_mplus.place(x=192.5, y=90, width=50, height=35)

    btn_mminus = tk.Button(win, text="M-", highlightbackground="#C0C0C0", fg="#000000",
                           font=('Courier New', 12, "bold"),
                           command=lambda: btn_mminus_clicked())
    btn_mminus.place(x=250, y=90, width=50, height=35)

    # row 2
    btn_del = tk.Button(win, text="del", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                        command=lambda: btn_del_clicked())
    btn_del.place(x=20, y=135, width=50, height=35)

    btn_ce = tk.Button(win, text="CE", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                       command=lambda: btn_ce_clicked())
    btn_ce.place(x=77.5, y=135, width=50, height=35)

    btn_c = tk.Button(win, text="C", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                      command=lambda: btn_c_clicked())
    btn_c.place(x=135, y=135, width=50, height=35)

    btn_reverse = tk.Button(win, text="+/-", highlightbackground="#C0C0C0", fg="#000000",
                            font=('Courier New', 12, "bold"),
                            command=lambda: btn_reverse_clicked())
    btn_reverse.place(x=192.5, y=135, width=50, height=35)

    btn_sqrt = tk.Button(win, text="sqrt", highlightbackground="#C0C0C0", fg="#000000",
                         font=('Courier New', 12, "bold"),
                         command=lambda: btn_sqrt_clicked())
    btn_sqrt.place(x=250, y=135, width=50, height=35)

    # row 3
    btn_7 = tk.Button(win, text="7", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                      command=lambda: btn_numbers_clicked("7"))
    btn_7.place(x=20, y=180, width=50, height=35)

    btn_8 = tk.Button(win, text="8", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                      command=lambda: btn_numbers_clicked("8"))
    btn_8.place(x=77.5, y=180, width=50, height=35)

    btn_9 = tk.Button(win, text="9", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                      command=lambda: btn_numbers_clicked("9"))
    btn_9.place(x=135, y=180, width=50, height=35)

    btn_div = tk.Button(win, text="/", highlightbackground="#C0C0C0", fg="#000000",
                        font=('Courier New', 12, "bold"),
                        command=lambda: btn_math_clicked("/"))
    btn_div.place(x=192.5, y=180, width=50, height=35)

    btn_mod = tk.Button(win, text="%", highlightbackground="#C0C0C0", fg="#000000",
                        font=('Courier New', 12, "bold"),
                        command=lambda: btn_math_clicked("%"))
    btn_mod.place(x=250, y=180, width=50, height=35)

    # row 4
    btn_4 = tk.Button(win, text="4", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                      command=lambda: btn_numbers_clicked("4"))
    btn_4.place(x=20, y=225, width=50, height=35)

    btn_5 = tk.Button(win, text="5", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                      command=lambda: btn_numbers_clicked("5"))
    btn_5.place(x=77.5, y=225, width=50, height=35)

    btn_6 = tk.Button(win, text="6", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                      command=lambda: btn_numbers_clicked("6"))
    btn_6.place(x=135, y=225, width=50, height=35)

    btn_mul = tk.Button(win, text="*", highlightbackground="#C0C0C0", fg="#000000",
                        font=('Courier New', 12, "bold"),
                        command=lambda: btn_math_clicked("*"))
    btn_mul.place(x=192.5, y=225, width=50, height=35)

    btn_invert = tk.Button(win, text="1/x", highlightbackground="#C0C0C0", fg="#000000",
                           font=('Courier New', 12, "bold"),
                           command=lambda: btn_invert_clicked())
    btn_invert.place(x=250, y=225, width=50, height=35)

    # row 5
    btn_3 = tk.Button(win, text="3", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                      command=lambda: btn_numbers_clicked("3"))
    btn_3.place(x=20, y=270, width=50, height=35)

    btn_2 = tk.Button(win, text="2", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                      command=lambda: btn_numbers_clicked("2"))
    btn_2.place(x=77.5, y=270, width=50, height=35)

    btn_1 = tk.Button(win, text="1", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                      command=lambda: btn_numbers_clicked("1"))
    btn_1.place(x=135, y=270, width=50, height=35)

    btn_minus = tk.Button(win, text="-", highlightbackground="#C0C0C0", fg="#000000",
                          font=('Courier New', 12, "bold"),
                          command=lambda: btn_math_clicked("-"))
    btn_minus.place(x=192.5, y=270, width=50, height=35)

    btn_equal = tk.Button(win, text="=", highlightbackground="#C0C0C0", fg="#000000",
                          font=('Courier New', 12, "bold"),
                          command=lambda: btn_equal_clicked())
    btn_equal.place(x=250, y=270, width=50, height=80)

    # row 6
    btn_0 = tk.Button(win, text="0", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                      command=lambda: btn_numbers_clicked("0"))
    btn_0.place(x=20, y=315, width=110, height=35)

    btn_dot = tk.Button(win, text=".", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                        command=lambda: btn_numbers_clicked("."))
    btn_dot.place(x=135, y=315, width=50, height=35)

    btn_add = tk.Button(win, text="+", highlightbackground="#C0C0C0", fg="#000000", font=('Courier New', 12, "bold"),
                        command=lambda: btn_math_clicked("+"))
    btn_add.place(x=192.5, y=315, width=50, height=35)

    win.mainloop()


if __name__ == "__main__":
    demo()
