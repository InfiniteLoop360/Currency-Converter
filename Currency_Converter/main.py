import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # For handling images
import requests

# Function to convert the currency
def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combo_from_currency.get()
    to_currency = combo_to_currency.get()

    # API URL for ExchangeRate-API
    api_key = 'e7eff5b68e2ff4b1d5477cc2'  # Replace with your API key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

    # Get the response from the API
    response = requests.get(url)
    data = response.json()

    if data['result'] == 'success':
        # Get the conversion rate from the API response
        conversion_rate = data['conversion_rates'].get(to_currency)
        if conversion_rate:
            converted_amount = amount * conversion_rate
            label_result.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            label_result.config(text="Error: Invalid target currency.")
    else:
        label_result.config(text="Error: Could not fetch conversion rate.")

# Function to exchange the currencies
def exchange_currencies():
    # Swap the selected currencies
    from_currency = combo_from_currency.get()
    to_currency = combo_to_currency.get()

    # Swap the values in the dropdowns
    combo_from_currency.set(to_currency)
    combo_to_currency.set(from_currency)

# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x400")
root.config(bg="black")  # Set the background color to black

# Load images
currency_icon_img = Image.open("currency_icon.png")  # Replace with your currency icon image path
currency_icon_img = currency_icon_img.resize((40, 40), Image.Resampling.LANCZOS)# Resize the image
currency_icon = ImageTk.PhotoImage(currency_icon_img)

exchange_icon_img = Image.open("exchange_icon.png")  # Replace with your exchange icon image path
exchange_icon_img = exchange_icon_img.resize((30, 30), Image.Resampling.LANCZOS) # Resize the image
exchange_icon = ImageTk.PhotoImage(exchange_icon_img)

# Title Label with currency icon
frame_header = tk.Frame(root, bg="black")
frame_header.pack(pady=10)

label_currency_icon = tk.Label(frame_header, image=currency_icon, bg="black")
label_currency_icon.pack(side="left", padx=5)

label_title = tk.Label(frame_header, text="Currency Converter", font=("Helvetica", 20, "bold"), bg="black", fg="white")
label_title.pack(side="left", padx=10)

# Label for amount input
label_amount = tk.Label(root, text="Enter Amount:", font=("Arial", 14), bg="black", fg="white")
label_amount.pack(pady=10)

# Entry widget to input amount
entry_amount = tk.Entry(root, font=("Arial", 14), width=20, bd=5, relief="solid", borderwidth=2, bg="white", fg="black")
entry_amount.pack(pady=10)

# Frame to hold dropdowns and exchange button
frame_currencies = tk.Frame(root, bg="black")
frame_currencies.pack(pady=20)

# Dropdown for selecting from currency
combo_from_currency = ttk.Combobox(frame_currencies, values=["USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY", "CNY"], font=("Arial", 14), state="readonly", width=10)
combo_from_currency.set("USD")  # Default value
combo_from_currency.grid(row=0, column=0, padx=10)

# Exchange button with exchange icon
button_exchange = tk.Button(frame_currencies, image=exchange_icon, bg="black", relief="solid", bd=2, command=exchange_currencies)
button_exchange.grid(row=0, column=1, padx=10)

# Dropdown for selecting to currency
combo_to_currency = ttk.Combobox(frame_currencies, values=["USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY", "CNY"], font=("Arial", 14), state="readonly", width=10)
combo_to_currency.set("INR")  # Default value
combo_to_currency.grid(row=0, column=2, padx=10)

# Convert button
button_convert = tk.Button(root, text="Convert", font=("Arial", 16), bg="#007bff", fg="white", relief="solid", bd=2, width=20, height=2, command=convert_currency)
button_convert.pack(pady=20)

# Result label
label_result = tk.Label(root, text="Converted Amount: 0.00 INR", font=("Arial", 16, "bold"), bg="black", fg="white")
label_result.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
