import json

with open("input.txt", 'r') as readFile:
    lines = int(readFile.readline())
    offers = []

    for _ in range(0, lines):
        offersDict = json.loads(readFile.readline())
        offers += offersDict["offers"]
    
    offers = str(sorted(offers, key=lambda d: (d["price"], d["offer_id"]))).replace("'", '"')
    with open("output.txt", 'w') as writefile:
        writefile.writelines("{\"offers\":" + offers + "}")
