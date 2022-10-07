def makePickledPlot(fig, title):
    from pickle import dump
    fileName = f'{title}.pkl'
    dump(fig, open(f'{fileName}', 'wb'))
    print(f"A pickled plot of the light curve named {fileName} has been saved in the current working directory")
