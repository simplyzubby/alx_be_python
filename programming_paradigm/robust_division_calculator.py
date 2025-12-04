def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Non-numeric input provided."

    try:

        result = num / denom
        return result
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."