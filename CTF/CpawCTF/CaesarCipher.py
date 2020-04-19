alphabet_lower = set('abcdefghijklmnopqrstuvwxyz')
alphabet_upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def ceasar_cipher(target, offsets):
    decoded = []
    for i in range(len(target)):
        if target[i] in alphabet_lower:
            decoded.append(
                chr((ord(target[i]) - ord('a') + offsets) % 26 + ord('a')))
        elif target[i] in alphabet_upper:
            decoded.append(
                chr((ord(target[i]) - ord('A') + offsets) % 26 + ord('A')))
        else:
            decoded.append(target[i])

    return ''.join(decoded)

if __name__ == "__main__":
    target_sentence =  input("Enter sentence (str) :").strip()
    offsets = int(input("Enter offsets (num) :"))
    print(ceasar_cipher(target_sentence, offsets))