class Luhn:
    def __init__(self, card_num: str):
        self.raw = card_num

    def valid(self) -> bool:
        # reject if contains characters other than digits or spaces
        for ch in self.raw:
            if not (ch.isdigit() or ch == " "):
                return False

        # remove spaces only
        card_num = self.raw.replace(" ", "")

        # must be at least 2 digits
        if len(card_num) <= 1:
            return False

        digits = [int(d) for d in card_num][::-1]

        # double every second digit
        for i in range(1, len(digits), 2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

        return sum(digits) % 10 == 0



