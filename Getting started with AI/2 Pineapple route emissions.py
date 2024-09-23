portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):

    global smallest, bestroute

    # When there are now port left, calculate emissions for the route
    # and keep up with the best route.
    if len(ports) < 1:

        # Calculate emissions for the route.
        emissions = 0
        for i in range(len(route)-1):
            emissions += D[route[i]][route[i+1]]*co2

        # Update the best route.
        if emissions < smallest:
            smallest = emissions
            bestroute = route
    else:
        for i in range(len(ports)):
            permutations(route + [ports[i]], ports[:i] + ports[i+1:] )
    pass

def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing

    # this will start the recursion 
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()
