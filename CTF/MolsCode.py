from getpass import getpass

class MolsCodeConverter:
    def __init__(self):
        self.char_map =   {
                            "A": ".-",
                            "B": "-...",
                            "C": "-.-.",
                            "D": "-..",
                            "E": ".",
                            "F": "..-.",
                            "G": "--.",
                            "H": "....",
                            "I": "..",
                            "J": ".---",
                            "K": "-.-",
                            "L": ".-..",
                            "M": "--",
                            "N": "-.",
                            "O": "---",
                            "P": ".--.",
                            "Q": "--.-",
                            "R": ".-.",
                            "S": "...",
                            "T": "-",
                            "U": "..-",
                            "V": "...-",
                            "W": ".--",
                            "X": "-..-",
                            "Y": "-.--",
                            "Z": "--..",
                            "1": ".----",
                            "2": "..---",
                            "3": "...--",
                            "4": "....-",
                            "5": ".....",
                            "6": "-....",
                            "7": "--...",
                            "8": "---..",
                            "9": "----.",
                            "0": "-----",
                            ".": ".-.-.-",
                            ",": "--..--",
                            ":": "---...",
                            "?": "..--..",
                            "'": ".----.",
                            "-": "-....-",
                            "(": "-.--.",
                            ")": "-.--.-",
                            "/": "-..-.",
                            "=": "-...-",
                            "+": ".-.-.",
                            "\"": ".-..-.",
                            "*": "-..-",
                            "@": ".--.-.",
                            "_": "..--.-",
                            ";": "-.-.-.",
                            "!": "-.-.--",
                            "$": "...-..-",
                            }
        self.code = ""
        self.message = ""

    def listen(self):
        message = getpass("Enter your message:")
        return message
    
    def context_to_list(self, context, type="msg"):
        if type == "msg":
            context_to_upper = context.upper()
            context_rm_space = context_to_upper.replace(" ", "")
            context_list = [con for con in context_rm_space]
        elif type == "code":
            context_list = context.split()
        return context_list

    def message_to_code(self, msg_list):
        for msg in msg_list:
            code = self.char_map[msg]
            self.code += code + " "
        else:
            self.code.rstrip()
        
        return self.code
    
    def code_to_message(self, code_list):
        for code in code_list:
            char = [k for k, v in self.char_map.items() if v == code][0]
            self.message += char + " "
        else:
            self.message + "."
        
        return self.message

if __name__ == "__main__":
    converter = MolsCodeConverter()
    en_type = int(input("1:MESSAGE=>CODE/2:CODE=>MESSAGE? "))
    context  = converter.listen()
    if en_type == 1:
        message_list = converter.context_to_list(context)
        message = converter.message_to_code(message_list)
        print(message)
    elif en_type == 2:
        code_list = converter.context_to_list(context, type="code")
        code = converter.code_to_message(code_list)
        print(code)