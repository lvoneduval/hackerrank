def is_leap(year):
    leap = (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
    
    # Write your logic here
    
    return leap
