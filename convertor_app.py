'''
Let's create an app that converts the things below
1 - pounds to kilos
2 - foot to meter 
3 - miles to km
4 - gallon to liter

first thing is to create the gui and then create the functions

'''

import tkinter as tk 


root = tk.Tk()
root.title("convertor")
root.minsize(400, 350)




def update_label(): #changes the label based on the option chosen
    selected = var.get()
    if selected == 1:
        option1_label.config(text="Pounds")
        option2_label.config(text="Kilos")
    elif selected == 2:
        option1_label.config(text="Foot")
        option2_label.config(text="Meters")
    elif selected == 3:
        option1_label.config(text="Miles")
        option2_label.config(text="Km")
    elif selected == 4:
        option1_label.config(text="Gallon")
        option2_label.config(text="Liter")


var = tk.IntVar() #creating the buttons
pounds_kilos_button = tk.Radiobutton(text= "Pounds to Kilos", value= 1, variable= var, command= update_label)
pounds_kilos_button.place(x= 30, y= 100)

foot_meter_button = tk.Radiobutton(text="Foot to Meters", value= 2, variable= var, command= update_label)
foot_meter_button.place(x= 30, y= 130)

miles_km_button = tk.Radiobutton(text= "Miles to Km", value= 3, variable= var, command= update_label)
miles_km_button.place(x= 30, y= 160)

gallon_liter_button = tk.Radiobutton(text= "Gallon to Liter", value= 4, variable= var, command= update_label)
gallon_liter_button.place(x= 30, y= 190)


def calculate(): #makes the calculation and prints it out
    selected_option = var.get()
    input_number = float(input.get())

    if selected_option == 1:
        result = round(input_number / 2.2, 2)
        result_label.config(text= result)
    elif selected_option == 2:
        result = round(input_number / 3.281, 2)
        result_label.config(text= result)
    elif selected_option == 3:
        result = (input_number * 1.6)
        result_label.config(text= result)
    elif selected_option == 4:
        result = round(input_number * 3.785, 2)
        result_label.config(text= result)


#creating the input, labels, and button
input = tk.Entry(width= 5, )
input.place(x= 170, y= 151)

option1_label = tk.Label(text= "choose", font=("ariel", 10))
option1_label.place(x= 220, y= 150)

is_label = tk.Label(text= "is", font=("ariel", 10))
is_label.place(x= 270, y= 150)

result_label = tk.Label(text= "0", font=("ariel", 9), )
result_label.place(x= 290, y=151)

option2_label = tk.Label(text= "choose", font=("ariel", 10))
option2_label.place(x= 330, y= 150)

button = tk.Button(text= "calculate", command= calculate)
button.place(x= 200, y= 200)
root.mainloop()