# This program takes an input in the form of principal and interest rate
# Program then determines the amount of time it takes for an investment to double in value

# initiates sentinel values to run initially
keepGoing = 'yes'

# statements after this while should loop until keepGoing no longer is equal to yes
while keepGoing == 'yes':
    # resets the principal and rate sentinels
    invalidPrincipal = 'yes'
    invalidRate = 'yes'
    # prompts for principal and interest rate
    while invalidPrincipal == 'yes':
        initialPrincipal = input('Enter principal: ')
        if initialPrincipal.isnumeric():
            initialPrincipal = float(initialPrincipal)
            if initialPrincipal >= 0:
                invalidPrincipal = 'no'
                while invalidRate == 'yes':
                    interestRate = input('Enter interest rate: ')
                    if interestRate.isnumeric():
                        interestRate = float(interestRate)
                        if interestRate >= 0:
                            invalidRate = 'no'
                            # resets the year and current principal when looping through
                            year = 0
                            currentPrincipal = initialPrincipal
                            # calculates the years needed
                            while currentPrincipal <= initialPrincipal * 2:
                                currentPrincipal = currentPrincipal + (currentPrincipal * interestRate / 100)
                                year = year + 1
                                # prints the number of years, initial principal and interest rates
                            print(year, 'years for', format(initialPrincipal, '12.2f'), 'to double to',
                                  format(currentPrincipal, '5.2f'), 'at', format(interestRate / 100, '12.2f'),
                                  'interest rate.')
                            # prompts for continuing loop
                            keepGoing = input('Another calculation?').strip().lower()
                        else:
                            print(interestRate, 'is not a valid value. Rate must be an integer > 0 ')
                    else:
                        print(interestRate, 'is not a valid value. Rate must be an integer > 0 ')
            else:
                print(initialPrincipal, 'is not a valid value. Principal must be an integer > 0 ')
        else:
            print(initialPrincipal, 'is not a valid value. Principal must be an integer > 0 ')
