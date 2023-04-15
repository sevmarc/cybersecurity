from alphabet import english_alphabet as alphabet


def caesar_cypher(
    message: str, shift_value: int, abc: str = alphabet, reverse: bool = False
) -> str:
    # ord('a') = 97; ord('z) = 122;
    # ord('A') = 65; ord('Z') = 90
    if reverse:
        shift_value *= -1

    message_decoded = ""
    for l in message:
        if l.islower():
            abc = abc.lower()
        elif l.isupper():
            abc = abc.upper()
        index_ = abc.find(l)
        if index_ == -1:  # not found char in alphabet
            # can be removed, or left as original
            message_decoded += l
            continue  # we skip/remove these characters
        shifted_index = (index_ + shift_value) % len(abc)
        message_decoded += abc[shifted_index]
    return message_decoded


if __name__ == "__main__":
    print(
        caesar_cypher(
            "Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh", 13, reverse=True
        )
    )
