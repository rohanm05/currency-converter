
def currency_converter(amount, from_currency, to_currency):
    
    conversion_rate = {
    'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
    'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
    'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
    'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }
    conversion = 0
    if amount <= 0:
        return 0.0
    match from_currency:
        case "GBP":
            if to_currency == "CNY":
                rate = float(conversion_rate['GBP']['CNY'])
                conversion = amount * rate
                return round(conversion, 2)
            elif to_currency == "PHP":
                rate = float(conversion_rate['GBP']['PHP'])
                conversion = amount * rate
                return round(conversion, 2)
            elif to_currency == "INR":
                rate = float(conversion_rate['GBP']['INR'])
                conversion = amount * rate
                return round(conversion, 2)
        case "CNY":
            if to_currency == "GBP":
                rate = float(conversion_rate['CNY']['GBP'])
                conversion = amount * rate
                return round(conversion, 2)
            elif to_currency == "PHP":
                rate = float(conversion_rate['CNY']['PHP'])
                conversion = amount * rate
                return round(conversion, 2)
            elif to_currency == "INR":
                rate = float(conversion_rate['CNY']['INR'])
                conversion = amount * rate
                return round(conversion, 2)
        case "PHP":
            if to_currency == "CNY":
                rate = float(conversion_rate['PHP']['CNY'])
                conversion = amount * rate
                return round(conversion, 2)
            elif to_currency == "GBP":
                rate = float(conversion_rate['PHP']['GBP'])
                conversion = amount * rate
                return round(conversion, 2)
            elif to_currency == "INR":
                rate = float(conversion_rate['PHP']['INR'])
                conversion = amount * rate
                return round(conversion, 2)
        case "INR":
            if to_currency == "PHP":
                rate = float(conversion_rate['INR']['PHP'])
                conversion = amount * rate
                return round(conversion, 2)
            elif to_currency == "CNY":
                rate = float(conversion_rate['INR']['CNY'])
                conversion = amount * rate
                return round(conversion, 2)
            elif to_currency == "GBP":
                rate = float(conversion_rate['INR']['GBP'])
                conversion = amount * rate
                return round(conversion, 2)

# Submit only this file currency_converter.py with the completed function.
# Do not add additional code for calling the function, or code to get user input.
