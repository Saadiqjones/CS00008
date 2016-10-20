units = input("Which measurement system would you like to use? Metric or USC? ")
distance = input("How far did you drive? ")
amount = input("How much gasoline was used? ")

distance = float(distance)
amount = float(amount)

# liters per 100 Km
kmconsumption = 100 * amount / distance
# miles per gallon
mpgconsumption = distance / amount

distance = format(distance, '.3f')
amount = format(amount, '.3f')
kmconsumption = format(kmconsumption, '.3f')
mpgconsumption = format(mpgconsumption, '.3f')

print("                         ", units)
if (units.upper() == "METRIC"):
    print("Distance ________:    ", distance, 'Km')
    print("Gas _____________:    ", amount, 'Liters')
    print("Consumption _____:    ", kmconsumption, '1/100Km')
    rating = ''
    kmconsumption = float(kmconsumption)
    if (kmconsumption > 20):
        rating = 'Extremely poor'
    elif (15 < kmconsumption <= 20):
        rating = 'Poor'
    elif (10 < kmconsumption <= 15):
        rating = 'Average'
    elif (9 < kmconsumption <= 10):
        rating = 'Good'
    elif (kmconsumption <= 8):
        rating = 'Excellent'

    print("Gas Consumption Rating :", rating)
else:
    print("Distance ________:    ", distance, 'miles')
    print("Gas _____________:    ", amount, 'gallons')
    print("Consumption _____:    ", mpgconsumption, 'mpg')







