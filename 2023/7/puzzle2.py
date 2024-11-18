from collections import Counter
from functools import cmp_to_key

STRENGTH_ORDER = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def categorize_hand(hand: str):
    if "J" in hand:
        counts = Counter(hand)
        del counts["J"]

        if len(counts) > 0:
            most_common = sorted(counts.items(), key=lambda x: x[1], reverse=True)[0][0]

            for i, c in enumerate(hand):
                if c != "J":
                    continue
                hand = hand[:i] + most_common + hand[i + 1 :]

    counts = Counter(hand)
    unique_counts = set(counts.values())

    if 5 in unique_counts:
        return 7
    elif 4 in unique_counts:
        return 6
    elif 3 in unique_counts and 2 in unique_counts:
        return 5
    elif 3 in unique_counts:
        return 4
    elif unique_counts == set([1, 2]) and len(counts) == 3:
        return 3
    elif 2 in unique_counts:
        return 2
    else:
        return 1


def rank(t1, t2):
    t1_score, t2_score = categorize_hand(t1[0]), categorize_hand(t2[0])

    if t1_score != t2_score:
        return t1_score - t2_score

    for i in range(5):
        t1_strength_i = STRENGTH_ORDER.index(t1[0][i])
        t2_strength_i = STRENGTH_ORDER.index(t2[0][i])

        if t1_strength_i != t2_strength_i:
            return t2_strength_i - t1_strength_i

    return 0


def process_data(data):
    rank_bid = [(line.split()[0], line.split()[1]) for line in data]
    rank_bid.sort(key=cmp_to_key(rank))
    winnings = [i * int(rank_bid[1]) for i, rank_bid in enumerate(rank_bid, 1)]
    return sum(winnings)


with open("data.txt", "r") as file:
    data = process_data(file.read().split("\n"))
    print(f"The total winnings are: {data}")
