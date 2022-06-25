import json

def getJSONAnimals() :
    data = json.load(open("./18.0_pets.json"))
    abilities = list(map(lambda ability: ability["Abilities"][0]["About"] , data))
    words = {}
    keywords = {}
    triggers = {}
    for ability in abilities :
        abilityWords = ability.split()
        keywordWords = ability.split(":")
        if keywordWords[0] in triggers :
            triggers[keywordWords[0]] += 1
        else :
            triggers[keywordWords[0]] = 1 
        for word in abilityWords :
            if word in words :
                words[word] += 1
            else :
                words[word] = 1 
        for word in keywordWords :
            if word in keywords :
                keywords[word] += 1
            else :
                keywords[word] = 1
    words = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))
    keywords = dict(sorted(keywords.items(), key=lambda item: item[1], reverse=True))
    triggers = dict(sorted(triggers.items(), key=lambda item: item[1], reverse=True))
    print(words)
    with open('words.json', 'w') as outfile:
        json.dump(words, outfile, indent=4)
    with open('keywords.json', 'w') as outfile:
        json.dump(keywords, outfile, indent=4)
    with open('triggers.json', 'w') as outfile:
        json.dump(triggers, outfile, indent=4)



getJSONAnimals()