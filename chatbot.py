from nltk.chat.util import Chat

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is Robot002",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm fine", "I am great!"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Apology accepted",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Good to know","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Python's NLTK library ","Top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Worldwide',]
    ],
    [
        r"(.*)love (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of football",]
    ],
    [
        r"who (.*) (Striker|Footballer)?",
        ["It used to be messi, but now I have no idea"]
    ],
    [
        r"quit",
        ["Bye human!", "Talk to you soon :)"]
    ],
    [
        r"(.*)",
        ["That's great!"]
    ],
]

reflections ={
        'i am': 'you are',
        'i was': 'you were',
        'i': 'you',
        "i'm": 'you are',
        "i'd": 'you would',
        "i've": 'you have',
        "i'll": 'you will',
        'my': 'your',
        'you are': 'I am',
        'you were': 'I was',
        "you've": 'I have',
        "you'll": 'I will',
        'your': 'my',
        'yours': 'mine',
        'you': 'me',
        'me': 'you'
}

#default message at the start of chat
print("Hi there, I'm Robot002\n Use lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)

#Start conversation
chat.converse()