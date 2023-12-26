weights: dict = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 0,
    "Q": 10,
    "K": 11,
    "A": 12
}


def compare(left: (str, str), right: (str, str)) -> bool:
    a, _ = left
    b, _ = right
    for c1, c2 in list(zip(a, b)):
        # print("C", c1, c2)
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
    card_count: dict = {"A": 0, "K": 0, "Q": 0, "T": 0, "9": 0,
                        "8": 0, "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0}
    j_count: int = 0
    for c in card:
        if c == "J":
            j_count += 1
        else:
            card_count[c] += 1

    most_popular_count: int = max(card_count.values())
    total: int = most_popular_count + j_count

    if total == 5:
        fivekind.append((card, value))
    elif total == 4:
        fourkind.append((card, value))
    elif total == 3:
        # Can be threekind or fullhouse
        # aaabc
        # aaabb
        # aajbb
        # aajbc
        if len([x for x in card_count.values() if x == 1]) >= 2:
            threekind.append((card, value))
        else:
            fullhouse.append((card, value))
    elif total == 2:
        # Can be twopair or onepair
        # ajbcd
        # aabcd
        # aabbc
        if len([x for x in card_count.values() if x == 2]) == 2:
            twopair.append((card, value))
        else:
            onepair.append((card, value))
    elif total == 1:
        high_cards.append((card, value))

# calculate result
result: int = 0
rank: int = 1

print(high_cards)
print(onepair)
print(twopair)
print(threekind)
print(fullhouse)
print(fourkind)
print(fivekind)

sorted_cards = quickSort(high_cards) + quickSort(onepair) + quickSort(twopair) + quickSort(
    threekind) + quickSort(fullhouse) + quickSort(fourkind) + quickSort(fivekind)

print(sorted_cards)

for (_, value) in sorted_cards:
    result += rank * int(value)
    rank += 1

print("y in highcards; ", len([x for (x, _) in high_cards if "J" in x]))
print("y in onepar; ", len([x for (x, _) in onepair if "J" in x]))
print("y in twopair; ", len([x for (x, _) in twopair if "J" in x]))
print("y in three; ", len([x for (x, _) in threekind if "J" in x]))
print("y in fullhouse; ", len([x for (x, _) in fullhouse if "J" in x]))
print("y in four; ", len([x for (x, _) in fourkind if "J" in x]))
print("y in five; ", len([x for (x, _) in fivekind if "J" in x]))
print(result)


# print(quickSort([("AAK", 1), ("AAQ", 2), ("AAA", 3)]))
