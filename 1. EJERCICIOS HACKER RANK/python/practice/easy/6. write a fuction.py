def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year != 1800 and year != 1900 and year != 2100 and year != 2200 and year != 2300 and year != 2500:
        leap = True
    
    return leap

if __name__ == "__main__":
    year = int(input('Ingrese el año: '))
    print(is_leap(year))