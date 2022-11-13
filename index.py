

class Morse:
    def __init__(self, *args, **kwargs):

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
                '+': '.=.=.',  '=' : '-...-',  '' : ''
            }

        self.INVERSE_LOOKUP = dict(zip(self.LOOKUP_TABLE.values(), self.LOOKUP_TABLE.keys()))  

    def encode(self, value: str, *args, **kwargs) -> str:
        """
        Encode
        ------


        - Returns a translation of the string given in morse code.



        :PARAM value: Translatable value
        
        :RETURN response: Encoded value

        """
        resp = ""
        for i in value:
            if i.upper() not in self.LOOKUP_TABLE:
                resp += "*"
                continue
            resp += self.LOOKUP_TABLE[i.upper()] + " "
        return resp
    
    def decode(self, value: str, *args, **kwargs) -> str:
        """
        Decode
        ------


        - Returns a string representation of the morse code value parameter



        :PARAM value: Morse code value

        :RETURN response: Decoded value

        """
        resp = ""
        characters = value.split(" ")
        for character in characters:
            resp += self.INVERSE_LOOKUP[character]
        return resp



morse = Morse()

encoded = morse.encode("Hello world!")
decoded = morse.decode(encoded)
morse.decode()
print(decoded)

