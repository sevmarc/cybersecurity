from alphabet import english_alphabet as alphabet


def caesar_cypher(message: str, shift_value: int, abc:str=alphabet) -> str:
    # ord('a') = 97; ord('z) = 122; 
    # ord('A') = 65; ord('Z') = 90
    message_lower = message.lower()  # capitalization is lost, don't care
    
    message_decoded = ''
    for l in message_lower:
        index_ = alphabet.find(l)
        shifted_index = (index_ + shift_value) % len(alphabet)
        message_decoded += alphabet[shifted_index]
    return message_decoded


if __name__ == '__main__':
    print(caesar_cypher('abcdefghijklmnopqrstuvwxyz', 5))
    # decoding done with negative shift value
    print(caesar_cypher('fghijklmnopqrstuvwxyzabcde', -5)) 