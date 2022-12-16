import json

with open('Deutschland-Spanien-Dialog.json', encoding="utf8") as f:
    data = json.load(f)
    
with open('template.json', encoding="utf8") as f:
    template = json.load(f)


for i in range (0, len(data['intents'])):
        print(i, data['intents'][i]['intent'])


trigger = []
z = 247
for i in range(0, len(data['intents'][z]['examples'])):
    dict_value = data['intents'][z]['examples'][i]
    list_of_value = list(dict_value.values())
    string_value = ''.join(list_of_value[0])
    trigger.append(string_value)
    
template[0]['name'] = data['intents'][z]['intent']
template[0]['trigger'] = []
template[0]['trigger'] = trigger

fileName = "test.json"
jsonString = json.dumps(template)
jsonString = json.loads(jsonString)

file = open(fileName, "w")
json.dump(jsonString, file)
file.close()
