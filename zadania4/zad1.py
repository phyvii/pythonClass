from math import ceil


def panels():
    floorLength = float(input("Input floor length: "))
    floorWidth = float(input("Input floor width: "))
    panelLength = float(input("Input panel length: "))
    panelWidth= float(input("Input panel width: "))
    number = float(input("Input panel number in box: "))

    neededMetrage = floorLength * floorWidth + (floorLength*floorWidth)*0.1;
    panelMetrage = panelLength * panelWidth;

    panelsNedded = ceil(neededMetrage/panelMetrage);

    numberOfBoxes = ceil(panelsNedded/number)

    print(f"You need : {panelsNedded} pannels, which are in {numberOfBoxes} boxes")

panels()
