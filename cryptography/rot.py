def rot(message: str, 
        shift_value: int, 
        reverse:bool = False) -> str:
    if reverse:
        shift_value *= -1

    return ''.join([ chr( ord(l) + shift_value ) for l in message])


if __name__ == '__main__':
    print(rot('abcdefghijklm -------124nopqrstuvwxyz', 5))
    print(rot('fghijklmnopqrstuvwxyzabcde', 5, True)) 