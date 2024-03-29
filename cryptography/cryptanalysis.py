import pandas
from collections import Counter
from alphabet import english_alphabet as alphabet
from alphabet import english_keywordlist as keywords

from caesar import caesar_cypher
from atbash import atbash_cypher
from rot import rot


freq_table = pandas.read_csv("letter_freq.csv", index_col="Letter")

unchecked_characters = [" ", ".", ","]

known_ciphers_codes = {
    # method: keyrange
    caesar_cypher: range(1, len(alphabet)),
    atbash_cypher: None,
    rot: range(1, 50),  # this range is arbitrary (ascii)
}


def calculate_deviance(message: str, language: str = "English") -> float:
    message_low = message.lower()
    letter_counter = Counter(message_low)
    message_len = len(message_low)
    deviance = 0

    for letter in letter_counter:
        try:
            lc_percent = letter_counter[letter] / message_len * 100
            exp_freq = freq_table[language][letter]
            deviance += (exp_freq - lc_percent) ** 2
            # print(f'{letter}: exp={exp_freq}, lc={lc_percent}, dev={deviance}')
        except KeyError:
            if letter in unchecked_characters:
                continue
            else:
                deviance += 100  # character not in alphabet
    # the keyword lookup might need calibration, good first solution for now
    for word_ in message_low.split():
        if word_ in keywords:
            deviance /= 2
    return deviance / (message_len**2)


class CipherCode:
    def __init__(self, coded_message: str) -> None:
        self.coded_message = coded_message
        self.method = None
        self.decoded_dict = {}
        self.decoded_msg = None
        self.create_decode_dict()
        self.analyze_decode_dict()
        print(self.decoded_msg)

    def create_decode_dict(self):
        for method, keyrange in known_ciphers_codes.items():
            if keyrange:
                for key_ in keyrange:
                    try:
                        decoded_message = method(self.coded_message, key_, reverse=True)
                        self.decoded_dict.update(
                            {str(method) + str(key_): decoded_message}
                        )
                    except ValueError:
                        continue
            else:
                decoded_message = method(self.coded_message)
                self.decoded_dict.update({method: decoded_message})

    def analyze_decode_dict(self):
        deviance_dict = {}
        for method, decode in self.decoded_dict.items():
            deviance_dict.update(
                {str(method) + str(decode): calculate_deviance(decode)}
            )
            # print(f"{str(method)}: {decode} = {calculate_deviance(decode)}")
        dict_sorted_by_values = dict(
            sorted(deviance_dict.items(), key=lambda item: item[1])
        )
        for i, j in dict_sorted_by_values.items():
            print(i, j)
        self.decoded_msg = next(iter(dict_sorted_by_values.items()))


if __name__ == "__main__":
    coded_message = "Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh"

    trial = CipherCode(coded_message)
