def computepay(h, r):
    if h <= 40:
        return (h * r)
    else:
        overh = h - 40
        h = 40
        return ((h * r) + (overh * r * 1.5))


hrs = input('enter hours : ')
rate = input('enter rate : ')
hrs = float(hrs)
rate = float(rate)
pay = computepay(hrs, rate)
print('Pay', pay)
