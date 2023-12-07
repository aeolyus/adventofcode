from functools import cmp_to_key

FIVE = 7
FOUR = 6
FULL_HOUSE = 5
THREE = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1


def part2(input_file: str):
    hand_bets = {}
    buckets = {i: [] for i in range(1, 8)}
    with open(input_file) as f:
        for line in f:
            hand = line.split(" ")[0].strip()
            bet = int(line.split(" ")[1].strip())
            hand_bets[hand] = bet
            hand_type = calc_hands(hand)
            buckets[hand_type].append(hand)
    for b in buckets.values():
        b.sort(key=cmp_to_key(sort_same_hand))
    flat_list = []
    for b in buckets.values():
        flat_list.extend(b)
    ans = 0
    for i in range(0, len(flat_list)):
        hand = flat_list[i]
        bet = hand_bets[hand]
        ans += bet * (i+1)
    return ans


def sort_same_hand(hand1: str, hand2: str):
    m = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 1,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
    }
    for i in range(0, len(hand1)):
        if m[hand1[i]] > m[hand2[i]]:
            return 1
        elif m[hand1[i]] < m[hand2[i]]:
            return -1
    return 0


def calc_hands(hand: str):
    matching = {}
    for char in hand:
        matching[char] = matching.get(char, 0) + 1
    values = list(v for k, v in matching.items() if k != 'J')
    num_wildcards = matching.get('J', 0)
    if len(values) > 0:
        idx = values.index(max(values))
        values[idx] += num_wildcards
    else:
        return FIVE
    if 5 in values:
        return FIVE
    elif 4 in values:
        return FOUR
    elif 3 in values and 2 in values:
        return FULL_HOUSE
    elif 3 in values:
        return THREE
    elif values.count(2) == 2:
        return TWO_PAIR
    elif 2 in values:
        return ONE_PAIR
    else:
        return HIGH_CARD


if __name__ == '__main__':
    print(part2("input.txt"))
