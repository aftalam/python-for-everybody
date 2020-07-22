hrs = input('input hours : ')
rate = input('input rate  : ')
hrs = float(hrs)
rate = float(rate)
if hrs <= 40:
    print(hrs * rate)
else:
    ohrs = hrs - 40
    hrs = 40
    print((hrs * rate) + (ohrs * rate * 1.5))
