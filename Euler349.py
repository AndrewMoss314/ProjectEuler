def colourCurrentLocation(location, grid):
    if grid == []:
        return "W"
    if location in grid:
        return "B"
    else:
        return "W"


# print(colourCurrentLocation([0, 0], [[0, 0], [1, 0]]))
# print(colourCurrentLocation([0, 1], [[0, 0], [1, 0]]))
# print(colourCurrentLocation([0, 1], []))


# print(currentGrid)
# print(type(currentGrid))

def run():
    maxT = 20

    currentLocation = [0, 0]
    currentOrientation = 0  # 0=Up, 1=Right, 2=Down, 3 = right
    currentGrid = []  # records black cells

    for t in range(0, maxT):
        currentLocationColour = colourCurrentLocation(
            currentLocation, currentGrid)

        if currentLocation in currentGrid:
            currentGrid.remove(currentLocation)
        else:
            currentGrid.append(currentLocation)

        if currentLocationColour == "W":
            currentOrientation = (currentOrientation + 1) % 4
        else:  # on black
            currentOrientation = (currentOrientation - 1) % 4

        if currentOrientation == 0:
            currentLocation[0] = currentLocation[0]
            currentLocation[1] = currentLocation[1] + 1
        elif currentOrientation == 1:
            currentLocation[0] = currentLocation[0] + 1
            currentLocation[1] = currentLocation[1]
        elif currentOrientation == 2:
            currentLocation[0] = currentLocation[0]
            currentLocation[1] = currentLocation[1] - 1
        elif currentOrientation == 3:
            currentLocation[0] = currentLocation[0] - 1
            currentLocation[1] = currentLocation[1]

        print(t, currentGrid, currentLocation,
              currentOrientation, currentLocationColour)


run()
