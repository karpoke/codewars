# https://www.codewars.com/kata/who-likes-it/train/python

def likes(names):
    i = len(names)
    
    what = "likes this" if i < 2 else "like this"
    
    if i == 0:
        who = "no one"
    elif i == 1:
        who = names[0]
    elif i == 2:
        who = " and ".join(names[:2])
    elif i == 3:
        who = "{} and {}".format(", ".join(names[:2]), names[2])
    elif i >= 4:
        who = "{} and {} others".format(", ".join(names[:2]), i-2)

    return "{} {}".format(who, what)

def likes(names):
    i = len(names)
    
    phrases = {
        0: "no one likes this",
        1: "{} likes this", 
        2: "{} and {} like this", 
        3: "{}, {} and {} like this", 
        4: "{}, {} and {others} others like this"
    }
    who = *names[:3]
    phrase = phrases.get(i, phrases[4]).format(who, others=i-2)

    return phrase
