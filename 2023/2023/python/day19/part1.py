def part1(input_file: str):
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
    sum = 0
    for part in parts:
        sum += eval_loop(part, rules_map, start_rule)
    return sum


def eval_loop(part, rules_map, rule_name):
    result = rule_name
    while result not in ["R", "A"]:
        result = eval_rule(part, rules_map, result)
    if result == "A":
        return sum(part.values())
    else:
        return 0


def eval_rule(part, rules_map, rule_name):
    rule = rules_map[rule_name]
    rules = rule.split(",")
    for r in rules[:-1]:
        condition, next = r.split(":")
        if '<' in condition:
            k, v = condition.split('<')
            if part[k] < int(v):
                return next
        elif '>' in condition:
            k, v = condition.split('>')
            if part[k] > int(v):
                return next
    return rules[-1]


if __name__ == "__main__":
    print(part1("input.txt"))
