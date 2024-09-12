# Tee ratkaisusi tähän:
class Decreasingcounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.initial_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1
        else:
            self.value = 0

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.initial_value


if __name__ == "__main__":
    counter = DecreasingCounter(2)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()