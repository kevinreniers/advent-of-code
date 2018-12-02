class FrequencyAdder(object):
    @staticmethod
    def calc(frequency_changes: list):
        frequency = 0
        for change in frequency_changes:
            frequency += int(change)
        return frequency


class FrequencyFinder(object):
    def __init__(self):
        self.frequency = 0
        self.frequencies = set()

    def find(self, all_changes: list):
        while self.frequency not in self.frequencies:
            freq = self.find_correct_frequency(all_changes)
            if freq is not None:
                return freq

    def find_correct_frequency(self, changes: list):
        for change in changes:
            self.frequencies.add(self.frequency)
            self.frequency += int(change.strip())
            if self.frequency in self.frequencies:
                return self.frequency
        return None


if __name__ == '__main__':
    print('-- Results --')
    with open(r'in.txt') as file:
        data = file.readlines()

    print('Solution for part 1: {}'.format(FrequencyAdder.calc(data)))
    print('Solution for part 2: {}'.format(FrequencyFinder().find(data)))
