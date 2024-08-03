import tkinter as tk

calculation = ""

def add_to_calc(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calc():
    global calculation
    try:
        calculation= str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


window = tk.Tk()

window.geometry("300x275")
window.title("Calculator")
text_result = tk.Text(window, height = 2, width = 16, font = ("Arial", 24))
text_result.grid(columnspan = 5)

btn_1 = tk.Button(window, text="1", command=lambda: add_to_calc(1), width = 5, font = ("Arial", 14))  #<----- Yaha pe lambda function ko pura bulata nhi hai, agar galat hua tho error nhi aayega
btn_1.grid(row=2, column=1)         #         ^ lambda sirf number k liye use karna hai, baki function k liye nhi

btn_2 = tk.Button(window, text="2", command=lambda: add_to_calc(2), width = 5, font = ("Arial", 14))  
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(window, text="3", command=lambda: add_to_calc(3), width = 5, font = ("Arial", 14))  
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(window, text="4", command=lambda: add_to_calc(4), width = 5, font = ("Arial", 14))  
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(window, text="5", command=lambda: add_to_calc(5), width = 5, font = ("Arial", 14))  
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(window, text="6", command=lambda: add_to_calc(6), width = 5, font = ("Arial", 14))  
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(window, text="7", command=lambda: add_to_calc(7), width = 5, font = ("Arial", 14))  
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(window, text="8", command=lambda: add_to_calc(8), width = 5, font = ("Arial", 14))  
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(window, text="9", command=lambda: add_to_calc(9), width = 5, font = ("Arial", 14))  
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(window, text="0", command=lambda: add_to_calc(0), width = 5, font = ("Arial", 14))  
btn_0.grid(row=5, column=2)

btn_open = tk.Button(window, text="(", command=lambda: add_to_calc("("), width = 5, font = ("Arial", 14))  
btn_open.grid(row=5, column=1)

btn_close = tk.Button(window, text=")", command=lambda: add_to_calc(")"), width = 5, font = ("Arial", 14))  
btn_close.grid(row=5, column=3)

btn_plus = tk.Button(window, text = "+", command = lambda: add_to_calc("+"), width = 5, font = ("Arial, 14"))
btn_plus.grid(row = 2, column = 4)

btn_minus = tk.Button(window, text = "-", command= lambda: add_to_calc("-"), width = 5,font=("Arial", 14))
btn_minus.grid(row=3, column=4)

btn_mult = tk.Button(window, text = "*", command=lambda: add_to_calc("*"), width = 5, font = ("Arial", 14))
btn_mult.grid(row=4, column=4)

btn_div = tk.Button(window, text="/", command=lambda:add_to_calc("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)

btn_clear = tk.Button(window, text="clear", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)

btn_equal = tk.Button(window, text="=", command=evaluate_calc, width=11, font=("Arial", 14))
btn_equal.grid(row=6, column=3, columnspan=2)

window.mainloop()      #<--- ye hamesha last mai he atta hai