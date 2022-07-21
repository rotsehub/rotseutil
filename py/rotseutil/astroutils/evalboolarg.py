def evalBoolArg(argument, default):
    if isinstance(argument, bool):
        return argument
    elif argument == None:
        return default
    elif argument.upper() == 'TRUE':
        return True
    elif argument.upper() == 'FALSE':
        return False
    else:
        return default