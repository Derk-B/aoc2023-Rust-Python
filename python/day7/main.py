weights: dict = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12
}


def compare(left: (str, str), right: (str, str)) -> bool:
    a, _ = left
    b, _ = right
    for c1, c2 in list(zip(a, b)):
        print("C", c1, c2)
        if weights[c1] > weights[c2]:
            return True
        if weights[c1] < weights[c2]:
            return False

    return False


def quickSort(arr):
    if len(arr) <= 1:
        # print("Done sorting: ", arr)
        return arr

    # print("Sorting: ", arr)
    m: int = int(len(arr) / 2)
    # print(m)
    pivot: str = arr[m]
    # print("pivot", pivot)

    left = []
    right = []

    for i in range(0, m):
        # print("i", i)
        if compare(arr[i], pivot):
            right.append(arr[i])
        else:
            left.append(arr[i])

    for i in range(m+1, len(arr)):
        if compare(arr[i], pivot):
            right.append(arr[i])
        else:
            left.append(arr[i])

    # print("Left, right: ", left, right)
    # print("return: ", quickSort(left) + [pivot] + quickSort(right))
    return quickSort(left) + [pivot] + quickSort(right)


f = open("input.txt")
lines = f.readlines()

high_cards: list((str, int)) = []
onepair: list((str, int)) = []
twopair: list((str, int)) = []
threekind: list((str, int)) = []
fullhouse: list((str, int)) = []
fourkind: list((str, int)) = []
fivekind: list((str, int)) = []

# Gather hands into correct classes
for line in lines:
    card, value = line.split(" ")
    card_count: dict = {"A": 0, "K": 0, "Q": 0, "J": 0, "T": 0, "9": 0,
                        "8": 0, "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0}
    for c in card:
        card_count[c] += 1

    # xxxxx
    if max(card_count.values()) == 5:
        fivekind.append((card, value))
    # xxxx0
    if max(card_count.values()) == 4:
        fourkind.append((card, value))
    # 12345
    if max(card_count.values()) == 1:
        high_cards.append((card, value))
    # aabcd
    if max(card_count.values()) == 2 and len([x for x in card_count.values() if x == 2]) == 1:
        onepair.append((card, value))
    # aabbc
    if max(card_count.values()) == 2 and len([x for x in card_count.values() if x == 2]) == 2:
        twopair.append((card, value))
    # aaabb
    if max(card_count.values()) == 3 and len([x for x in card_count.values() if x > 0]) == 2:
        fullhouse.append((card, value))
    # aaabc
    if max(card_count.values()) == 3 and len([x for x in card_count.values() if x > 0]) == 3:
        threekind.append((card, value))

# calculate result
result: int = 0
rank: int = 1

# print(high_cards)
# print(onepair)
# print(twopair)
# print(threekind)
# print(fullhouse)
# print(fourkind)
# print(fivekind)

sorted_cards = quickSort(high_cards) + quickSort(onepair) + quickSort(twopair) + quickSort(
    threekind) + quickSort(fullhouse) + quickSort(fourkind) + quickSort(fivekind)

# print(sorted_cards)

for (_, value) in sorted_cards:
    result += rank * int(value)
    rank += 1

print(result)


# print(quickSort([("AAK", 1), ("AAQ", 2), ("AAA", 3)]))
