RED = 12
GREEN = 13
BLUE = 14


def part1(input_file: str):
    sum = 0
    with open(input_file) as f:
        for line in f:
            lst = line.split(":")
            game_num = int(lst[0].split(" ")[1])
            game_data = lst[1]
            sets = game_data.split(";")
            color_max_count = dict()
            for st in sets:
                for hand in st.split(","):
                    hand_data = hand.strip().split(" ")
                    hand_num = int(hand_data[0])
                    hand_color = hand_data[1]
                    color_max_count[hand_color] = max(
                        color_max_count.get(hand_color, float("-inf")),
                        hand_num,
                    )
            if color_max_count["red"] <= RED \
                    and color_max_count["blue"] <= BLUE \
                    and color_max_count["green"] <= GREEN:
                sum += game_num
    return sum


if __name__ == "__main__":
    print(part1("input.txt"))
