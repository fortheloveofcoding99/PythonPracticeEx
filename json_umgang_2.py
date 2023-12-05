import json

var1 = {
    "Subjects": {
        "Maths": 90,
        "Physics": 25,
        "Maths1": 85,
        "Physics1": 90
    },
    "Name": {
        "Vorname": "Abu",
        "Nachname": "Naeem",
        "Vorname1": "Abu",
        "Nachname1": "Bodai"
    }

}

with open('sample.json','w') as file1:
    json.dump(var1, file1)

with open('sample.json','r') as file:
    datei = json.load(file)

format_data = json.dumps(datei,indent=1)

print(format_data)