import json

def modify(ss) : 

    json_obj = json.dumps(ss, indent=4)

    with open("scores.json","w") as scor :
        scor.write(json_obj)

def add(chap,ex) :

    with open("scores.json","r") as thing :
        scores = json.load(thing)

    scores[f"chapter{chap}"][f"ex{ex}"] += 1
    
    modify(scores)

def show(chap,ex) :

    with open("scores.json","r") as thing :
        scores = json.load(thing)

    return scores[f"chapter{chap}"][f"ex{ex}"]

def reset(chap,ex) :

    with open("scores.json","r") as thing :
        scores = json.load(thing)

    scores[f"chapter{chap}"][f"ex{ex}"] = 0
    
    modify(scores)

def reset_all(chap) :

    with open("scores.json","r") as thing :
        scores = json.load(thing)

    for i in scores[f"chapter{chap}"] :
        
        scores[f"chapter{chap}"][i] = 0
    
    modify(scores)

def sum_all() :

    with open("scores.json","r") as thing :
        scores = json.load(thing)

    total = 0
    for e in scores.keys() :
        for i in scores[e] :
            
            total += scores[e][i] 
    
    return total 

def progress() :

    ques = sum_all()
    px = ques*0.64

    return int(px)


