import copy


def part2(input_file: str):
    rules_map = {}
    parts = []
    with open(input_file) as f:
        lines = f.readlines()
        is_parts = False
        for line in lines:
            line = line.strip()
            if line == "":
                is_parts = True
                continue
            if not is_parts:
                temp = line.split('{')
                rule_name = temp[0]
                rule_content = temp[1][:-1]
                rules_map[rule_name] = rule_content
            else:
                temp = line[1:-1].split(",")
                part = {}
                for piece in temp:
                    k, v = piece.split("=")
                    part[k] = int(v)
                parts.append(part)

    start_rule = "in"
    part = {k: (1, 4000) for k in "xmas"}

    result = eval_loop(part, rules_map, start_rule)

    sum = 0
    for item in result:
        temp = 1
        for rnge in item:
            lo, hi = rnge
            temp = temp * (hi - lo + 1)
        sum += temp
    return sum


def eval_loop(start_part, rules_map, start_rule_name):
    parts = [(start_rule_name, start_part)]
    total_accepted_parts = set()
    while parts:
        rule_name, part = parts.pop()
        if rule_name == "A":
            total_accepted_parts.add(tuple(part.values()))
            continue
        elif rule_name == "R":
            continue
        todo = eval_rule(part, rules_map, rule_name)
        parts.extend(todo)
    return total_accepted_parts


def eval_rule(part, rules_map, rule_name):
    todo = []
    rule = rules_map[rule_name]
    rules = rule.split(",")
    for r in rules[:-1]:
        condition, next = r.split(":")
        if '<' in condition:
            k, v = condition.split('<')
            v = int(v)
            rnges = range_split(part[k], '<', v)
            for idx, rnge in enumerate(rnges):
                new_part = copy.deepcopy(part)
                new_part[k] = rnge
                if idx == 0:
                    todo.append((next, new_part))
                else:
                    part = copy.deepcopy(new_part)
        elif '>' in condition:
            k, v = condition.split('>')
            v = int(v)
            rnges = range_split(part[k], '>', v)
            for idx, rnge in enumerate(rnges):
                new_part = copy.deepcopy(part)
                new_part[k] = rnge
                if idx == 0:
                    todo.append((next, new_part))
                else:
                    part = new_part
    todo.append((rules[-1], part))
    return todo


def range_split(rnge, op, num):
    result = []
    lo, hi = rnge
    if op == '<':
        if hi < num:
            result.append(rnge)
        elif lo >= num:
            pass
        else:
            result.extend([(lo, num - 1), (num, hi)])
    elif op == '>':
        if lo > num:
            result.append(rnge)
        elif hi <= num:
            pass
        else:
            result.extend([(num + 1, hi), (lo, num)])
    return result


if __name__ == "__main__":
    print(part2("input.txt"))
