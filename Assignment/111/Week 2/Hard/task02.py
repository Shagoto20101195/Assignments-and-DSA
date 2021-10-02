def calculate(n):
    years = n // 365
    months = (n - (365 * years)) // 30
    days = n - (years * 365) - (months * 30)
    print(years," years, ",months," months and ",days," days", sep = "")

n = int(input("Enter number of days: "))
calculate(n)