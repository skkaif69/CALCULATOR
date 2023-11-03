import tkinter as tk


# Function to update the input field when a button is clicked
def button_click(char):
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(0, current + char)


# Function to clear the input field
def clear_entry():
    input_field.delete(0, tk.END)


# Function to perform the calculation
def calculate():
    try:
        expression = input_field.get()
        result = eval(expression)
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except Exception as e:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")


# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Entry field for input
input_field = tk.Entry(root, font=('Arial', 16))
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Buttons for numbers, operators, "AC" and "CE"
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'AC', 'CE'
]

row_val, col_val = 1, 0

for button_text in button_texts:
    if button_text == '=':
        tk.Button(root, text=button_text, command=calculate, font=('Arial', 16)).grid(row=row_val, column=col_val,
                                                                                      padx=5, pady=5, ipadx=5, ipady=5)
    elif button_text == 'AC':
        tk.Button(root, text=button_text, command=clear_entry, font=('Arial', 16)).grid(row=row_val, column=col_val,
                                                                                        padx=5, pady=5, ipadx=5,
                                                                                        ipady=5)
    elif button_text == 'CE':
        tk.Button(root, text=button_text, command=lambda b=button_text: button_click(b), font=('Arial', 16)).grid(
            row=row_val, column=col_val, padx=5, pady=5, ipadx=5, ipady=5)
    else:
        tk.Button(root, text=button_text, command=lambda b=button_text: button_click(b), font=('Arial', 16)).grid(
            row=row_val, column=col_val, padx=5, pady=5, ipadx=5, ipady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
