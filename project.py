import tkinter as tk
CONVERSION_RATES = {
    'USD': 2.60,
    'EUR': 2.45,
    'GBP': 2.19,
    'JPY': 355.20,
    'BHD': 0.98,
    'AED': 9.54,
    'THB': 90.91,
    'SAR': 9.75,
    'QAR': 9.46,
    'PKR': 716.18,
    'MXN': 47.01,
    'ARS': 518.75,
    'BRL': 13.45,
    'BND': 3.50,
    'KWD': 0.80,
    'IQD': 3792.62,
    'IDR': 40037.50,
    'NOK': 27.66,
    'YER': 650.33,
    'TRY': 49.15,
    'SDG': 1541.73,
    'SGD': 3.51,
    'PHP': 143.52,
    'NZD': 4.24,
    'MKD': 150.16,
    'JOD': 1.84,
    'IRR': 109744.42,
    'INR': 212.84,
    'HKD': 20.39,
    'GYD': 547.94,
    'EGP': 79.82,
    'DOP': 143.25,
    'CUP': 62.32,
    'COP': 12361.64,
    'CNY': 18.08,
    'CLP': 2084.96,
    'KYD': 2.16,
    'KHR': 10522.48,
    'BGN': 4.80,
    'BZD': 5.23,
    'BDT': 273.42,
    'AZN': 4.42,
    'ALL': 279.17,
    'BOB': 17.95,
    'BWP': 34.53,
    'CAD': 3.57,
    'BIF': 5397.61,
    'CRC': 1435.08,
    'HUF': 929.12,
    'LBP': 39657.35
}
app = tk.Tk()
app.title('Currency Converter')

def convert():
    amount = float(amount_entry.get())
    from_currency = 'OMR'
    to_currency = currency_var.get()
    converted_amount = amount * CONVERSION_RATES[to_currency]
    result_entry.delete(0, tk.END)
    result_entry.insert(0, round(converted_amount, 3))

amount_label = tk.Label(app, text='Enter amount in OMR:')
amount_label.pack()
amount_entry = tk.Entry(app)
amount_entry.pack()

currency_label = tk.Label(app, text='Select currency to convert to:')
currency_label.pack()
currency_var = tk.StringVar(app)
currency_var.set('Select..') 
currency_menu = tk.OptionMenu(app, currency_var, *CONVERSION_RATES.keys())
currency_menu.pack()

convert_button = tk.Button(app, text='Convert', command=convert)
convert_button.pack()

result_label = tk.Label(app, text='Converted amount:')
result_label.pack()
result_entry = tk.Entry(app)
result_entry.pack()

app.mainloop()
