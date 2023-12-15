ADD = "add"
REMOVE = "remove"


def part2(input_file: str):
    with open(input_file) as f:
        line = ""
        lines = f.readlines()
        for li in lines:
            line = li.strip()
        line = line.split(",")
    boxes = [[] for i in range(256)]
    for word in line:
        lab = label(word)
        box_num = hash(lab)
        act = action(word)
        foc = 0
        if act == ADD:
            foc = focal_length(word)

        box = boxes[box_num]

        if act == ADD:
            idx = -1
            for i, item in enumerate(box):
                if item[0] == lab:
                    idx = i
            if idx != -1:
                box[idx] = (lab, foc)
            else:
                box.append((lab, foc))
        elif act == REMOVE:
            new_box = []
            for i, item in enumerate(box):
                if item[0] != lab:
                    new_box.append(item)
            boxes[box_num] = new_box

    v = score(boxes)
    return v


def score(boxes):
    v = 0
    for box_num, box in enumerate(boxes):
        for j, item in enumerate(box):
            temp = 0
            temp = (1+box_num)
            foc = item[1]
            slot_num = j + 1
            temp *= slot_num
            temp *= foc
            v += temp
    return v


def focal_length(word):
    return int(word.split("=")[-1])


def action(word):
    result = ""
    if "=" in word:
        return ADD
    elif "-" in word:
        return REMOVE
    return result


def label(word):
    result = ""
    if "=" in word:
        result = word.split("=")[0]
    elif "-" in word:
        result = word.split("-")[0]
    return result


def hashmap(string):
    pass


def hash(string):
    curr_value = 0
    for c in string:
        curr_value += ord(c)
        curr_value *= 17
        curr_value %= 256
    return curr_value


if __name__ == '__main__':
    print(part2("input.txt"))
