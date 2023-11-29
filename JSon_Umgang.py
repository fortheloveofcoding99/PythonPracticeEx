import json

#serialization - verwandlung von python objekte zur json objekte
var = {
      "Subjects": {
                  "Maths":85,
                  "Physics":90 },
        "name": {
            "Vorname":"Abu",
            "Nachname":"Bodai"}
      }

with open('sample.json','w') as p:
    json.dump(var , p)

#deserialization - verwandlung von json obkekte zur python objekte
with open('sample.json','r') as p:
    inhalt = json.load(p)

read_inhalt = inhalt

print(inhalt)

