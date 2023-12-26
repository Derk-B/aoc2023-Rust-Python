class Sequence:
    def __init__(self, line):
        self.sequence = line
        self.steps = []
        prev: chr = line[0]
        for c in line[1:]:
            self.steps.append(int(c) - int(prev))
            prev = c

        if not all([x == 0 for x in self.steps]):
            self.next_sequence = Sequence(self.steps)

        print(self.steps)

    def next_number(self) -> int:
        if all([x == 0 for x in self.steps]):
            return self.sequence[-1]
        else:
            return self.sequence[-1] + self.next_sequence.next_number()
        
    def prev_number(self) -> int:
        if all([x == 0 for x in self.steps]):
            return self.sequence[0]
        else:
            # print(self.next_sequence.prev_number())
            return self.sequence[0] - self.next_sequence.prev_number()

f = open("input.txt")
lines = f.readlines()

result1 = 0
result2 = 0

for line in lines:
    sequence = Sequence([int(x) for x in line.split(" ")])

    result1 += sequence.next_number()
    result2 += sequence.prev_number()

print(result1)
print(result2)