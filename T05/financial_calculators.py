import math

h = 1
while(h == 1):
   
    # Display menu options
    print("""
    investment  - to calculate the amount of interest you'll earn on your investment
    bond        - to calculate the amount you'll have to pay on a home loan
    """)

    # Prompt user for selection
    selection = input("Enter either \"investment\" or \"bond\" from the menu above to proceed:  ")

    if(selection.lower() == "investment"):
        # Calculate investment
        print("""
        Please enter the following information:
        """)

        # Prompt user for deposit amount
        deposit = input("The amount of money you are depositing:        ")

        # Validate and retrieve interest rate
        i = 1
        while(i == 1):  # Ensure user doesn't enter "%"
            rate = input("The percentage interest rate on your investment:      ")
            if("%" in rate):
                print("Please enter only the number.        ")
            else:
                i += 1

        # Prompt user for investment duration in years
        years = input("The number of years that you plan on investing:     ")

        # Determine interest type (simple or compound)
        j = 1
        while(j == 1):
            interest = input("Do you want \"simple\" or \"compound\" interest?      ")
            if(interest.lower() == "simple"):
                # Calculate total amount with simple interest
                total_amount = (float(deposit) * (1 + (float(rate) / 100) * float(years)))
                print(f"""
                The total amount that will be returned on your investment is {total_amount}.
                """)
                j += 1
            elif(interest.lower() == "compound"):
                # Calculate total amount with compound interest
                total_amount = (float(deposit) * ((1 + (float(rate) / 100)) ** float(years)))
                print(f"""
                The total amount that will be returned on your investment is {total_amount:.2f}
                """)
                j += 1
            else:
                print("Please enter either \"simple\" or \"compound\"")

        h += 1

    elif(selection.lower() == "bond"):
        # Calculate bond repayment amount
        value = input("Please enter the present value of the house:     ")

        # Validate and retrieve bond interest rate
        k = 1
        while(k == 1):
            bond_rate =  input("Please enter the interest rate:      ")
            if("%" in bond_rate):
                print("Please enter only the number.        ")
            else:
                k += 1

        # Prompt user for bond repayment duration in months
        months = input("Please enter the number of months you plan to take to repay your bond:      ")

        # Calculate monthly repayment amount
        repayment = (float(bond_rate) * float(value)) / (1 - ((1 + float(bond_rate))**(-float(months))))
        print(f"""
        The amount of money you will need to repay each month is {repayment:.2f}
        """)

        h += 1

    else:
        print("Please enter either \"Investment\" or \"Bond\".")