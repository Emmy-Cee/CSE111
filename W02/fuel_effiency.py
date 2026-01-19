def main():
    # Get user input
    start_miles = float(input("Enter the starting odometer value in miles: "))
    end_miles = float(input("Enter the ending odometer values in miles: "))
    amount_gallons = float(input("Enter the gallons of gas used: "))
    
    #Initialaize variables
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
    lp100k = lp100k_from_mpg(mpg)
    
    # Display results
    print(f"\nMiles per gallon: {mpg:.2f} mpg")
    print(f"Liters per 100 kilometers: {lp100k:.2f} L/100km")
    pass

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    miles_driven = end_miles - start_miles
    mpg = miles_driven / amount_gallons
    return mpg

def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

main()