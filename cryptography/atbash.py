from alphabet import english_alphabet as alphabet


def atbash_cypher(message: str, abc: str = alphabet) -> str:
    message_lower = message.lower()  # capitalization is lost, don't care

    message_decoded = ""
    for l in message_lower:
        index_ = alphabet.find(l)
        if index_ == -1:  # not found char in alphabet
            # can be removed, or left as original
            message_decoded += l
            continue  # we skip/remove these characters
        message_decoded += list(reversed(alphabet))[index_]
    return message_decoded


if __name__ == "__main__":
    print(atbash_cypher("abcdefghijkl1111mnopqrstuvwxyz"))
    # applying it twice deciphers
    print(atbash_cypher(atbash_cypher("abcdefghijklmnopqrstuvwxyz")))
