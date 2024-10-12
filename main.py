import tkinter as tk
from tkinter import messagebox

def calculate_tip():
    try:
        
        bill = float(bill_entry.get())
        tip = int(tip_entry.get())
        people = int(people_entry.get())
        
        
        tip_as_percent = tip / 100
        total_tip_amount = bill * tip_as_percent
        total_bill = bill + total_tip_amount
        bill_per_person = total_bill / people
        final_amount = round(bill_per_person, 2)
        
        
        result_label.config(text=f"Each person should pay: ${final_amount}")
    
    except ValueError:
        
        messagebox.showerror("Input Error", "Please enter valid numbers for bill, tip, and people.")


window = tk.Tk()
window.title("Tip Calculator")


bill_label = tk.Label(window, text="Total Bill: $")
bill_label.grid(row=0, column=0, padx=10, pady=10)
bill_entry = tk.Entry(window)
bill_entry.grid(row=0, column=1, padx=10, pady=10)

tip_label = tk.Label(window, text="Tip Percentage: %")
tip_label.grid(row=1, column=0, padx=10, pady=10)
tip_entry = tk.Entry(window)
tip_entry.grid(row=1, column=1, padx=10, pady=10)

people_label = tk.Label(window, text="Number of People:")
people_label.grid(row=2, column=0, padx=10, pady=10)
people_entry = tk.Entry(window)
people_entry.grid(row=2, column=1, padx=10, pady=10)


calculate_button = tk.Button(window, text="Calculate", command=calculate_tip)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)


result_label = tk.Label(window, text="Each person should pay: $0.00", font=("Helvetica", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)


window.mainloop()
