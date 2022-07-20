def evalBoolArg(argument, defaultState):
    if argument == True or argument == False:
        pass
    elif argument.upper() == 'True':
        argument = True
    elif argument.upper() == 'FALSE':
        argument = False
    else:
        argument = defaultState
    return argument
    