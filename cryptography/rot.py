def rot(message: str, shift_value: int, reverse: bool = False) -> str:
    if reverse:
        shift_value *= -1

    return "".join([chr(ord(l) + shift_value) for l in message])


if __name__ == "__main__":
    print(rot("Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh", 13, True))
