from alphabet import english_alphabet as alphabet


def caesar_cypher(message: str, shift_value: int, abc:str=alphabet) -> str:
    # ord('a') = 97; ord('z) = 122; 
    # ord('A') = 65; ord('Z') = 90
    message_lower = message.lower()  # capitalization is lost, don't care
    
    message_decoded = ''
    for l in message_lower:
        index_ = alphabet.find(l)
        if index_ == -1:  # not found char in alphabet
            # can be removed, or left as original
            message_decoded += l
            continue  # we skip/remove these characters
        shifted_index = (index_ + shift_value) % len(alphabet)
        message_decoded += alphabet[shifted_index]
    return message_decoded


if __name__ == '__main__':
    print(caesar_cypher('abcdefghijklm -------124nopqrstuvwxyz', 5))
    # decoding done with negative shift value
    print(caesar_cypher('fghijklmnopqrstuvwxyzabcde', -5)) 