def computepay(h,r):
    ot = h - 40
    ot_pay = r*1.5
    tot = (40 * 10.50) + (ot * ot_pay)
    return tot

hrs = raw_input("Enter Hours:")
h_f = float(hrs)
if h_f > 40:
	p = computepay(h_f,10.50)
else :
	p = 40 * 10.50
print p