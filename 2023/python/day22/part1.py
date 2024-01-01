from typing import List, Dict, Set


class Brick:
    name: int
    start: List[int]
    end: List[int]
    z: int
    supporting: Set[str]
    supported_by: Set[str]

    def __init__(self, name, start, end, z, supporting, supported_by):
        self.name = name
        self.start = start
        self.end = end
        self.z = z
        self.supporting = supporting
        self.supported_by = supported_by

    def __repr__(self):
        return " ".join(str(s) for s in [
            self.name,
            self.start,
            self.end,
            self.z,
            self.supporting,
            self.supported_by,
        ])


def part1(input_file: str):
    bricks = []
    brick_map: Dict[int, Brick] = {}
    with open(input_file) as f:
        lines = f.readlines()
        for brick_name, line in enumerate(lines):
            brick_name += 1
            line = line.strip()
            start, end = line.split("~")
            start = tuple(int(c) for c in start.split(","))
            end = tuple(int(c) for c in end.split(","))
            z = start[2]
            brick = Brick(brick_name, start, end, z, set(), set())
            brick_map[brick_name] = brick
            bricks.append(brick)

    # Process bricks from the bottom most ones first
    bricks.sort(key=lambda brick: brick.start[2])

    stack_bricks(bricks, brick_map)

    result = 0
    for brick in brick_map.values():
        can_remove = True
        for b_id in brick.supporting:
            b = brick_map[b_id]
            if len(b.supported_by) == 1:
                can_remove = False
                break
        if can_remove:
            result += 1
    return result


def stack_bricks(bricks: List[Brick], brick_map: Dict[int, Brick]):
    ground = [[0 for _ in range(10)] for _ in range(10)]
    for brick in bricks:
        start_x, start_y, start_z = brick.start
        end_x, end_y, end_z = brick.end
        max_z = 0
        # Find highest brick(s)
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                supporting_brick_id = ground[x][y]
                if supporting_brick_id == 0:
                    continue
                supporting_brick = brick_map[supporting_brick_id]
                if brick.z > supporting_brick.z:
                    max_z = max(max_z, supporting_brick.z)
        # Have those highest brick support you
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                supporting_brick_id = ground[x][y]
                if supporting_brick_id == 0:
                    continue
                supporting_brick = brick_map[supporting_brick_id]
                if supporting_brick.z == max_z:
                    brick.supported_by.add(supporting_brick_id)
                    supporting_brick.supporting.add(brick.name)

        # Put yourself in
        brick.z = (end_z - start_z + max_z + 1)
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                ground[x][y] = brick.name
    return ground


if __name__ == "__main__":
    print(part1("input.txt"))
