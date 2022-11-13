

class Morse:
    def __init__(self):

        self.LOOKUP_TABLE = {   
                'A': '.-',     'B' : '-...',
                'C': '-.-.',   'D' : '-..',    'E': '.',
                'F': '..-.',   'G' : '--.',    'H': '....',
                'I': '..',     'J' : '.---',   'K': '-.-',
                'L': '.-..',   'M' : '--',     'N': '-.',
                'O': '---',    'P' : '.--.',   'Q': '--.-',
                'R': '.-.',    'S' : '...',    'T': '-',
                'U': '..-',    'V' : '...-',   'W': '.--',
                'X': '-..-',   'Y' : '-.--',   'Z': '--..',
                '1': '.----',  '2' : '..---',  '3': '...--',
                '4': '....-',  '5' : '.....',  '6': '-....',
                '7': '--...',  '8' : '---..',  '9': '----.',
                '0': '-----',  ', ': '--..--', '.': '.-.-.-',
                '?': '..--..', '/' : '-..-.',  '-': '-....-',
                '(': '-.--.',  ')' : '-.--.-', ' ': '/',
                '!': '-.-.--', ';' : '-.-.-.', ':': '---...',
                '+': '.=.=.',  '=' : '-...-'
            }

        self.INVERSE_LOOKUP = dict(zip(self.LOOKUP_TABLE.values(), self.LOOKUP_TABLE.keys()))  

    def encode(self, value: str):
        resp = ""
        for i in value:
            if i.upper() not in self.LOOKUP_TABLE:
                resp += "*"
                continue
            resp += self.LOOKUP_TABLE[i.upper()] + " "
        return resp
    
    def decode(self, value: str):
        resp = ""
        
        characters = value.split(" ")
        for character in characters:
            
            resp += self.INVERSE_LOOKUP[character]

        return resp



morse = Morse()

encoded = morse.encode("Hello world!")
decoded = morse.decode(encoded)
print(decoded)

