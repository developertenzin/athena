import csv

with open("rel_track.xlsx", "r") as playgroundFile:
    playgroundFileReader = csv.reader(playgroundFile)
    playgroundRows = []
    for row in playgroundFileReader:
        if len(row) != 0:
            playgroundRows.append(row)
    print(playgroundRows)

