def kadanesmaxintpositionformaxsubarray(intarray):
    maxsubarraystart = 0
    #maxsubarrayend = 0
    maxsubarraysum = 0
    for i in range(0, len(intarray)):
        val = intarray[i]
        maxsubarraysum += val
        if val >= maxsubarraysum:
            maxsubarraystart = i
            #maxsubarrayend = i
            maxsubarraysum = val
        #else:
            #maxsubarrayend = i
    #maxsubarray = intarray[maxsubarraystart:maxsubarrayend]
    return maxsubarraystart
