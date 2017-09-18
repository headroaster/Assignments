def gatherNotes (event = None):
    inputs = []
    with open (os.path.expanduser("~/Documents/notes/tempNotes." + datetime.date.today().strftime("%m.%d.%Y") + ".txt"), "r") as notes:
        for line in notes:
            inputs.append(line)

        gathered = {}
        for item in inputs:
            gathered[inputs.index(item)+1] = item
        return gathered
