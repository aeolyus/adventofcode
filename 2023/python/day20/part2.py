from collections import defaultdict
from typing import List
import math

FLIP_FLOP = '%'
CONJUNCTION = '&'
BROADCAST = "broadcaster"
OUTPUT = "output"

PULSE_TYPE_LO = "lo"
PULSE_TYPE_HI = "hi"

PARENT_MODULE = "mf"


class BiMap:
    forward: dict
    inverse: dict

    def __init__(self):
        self.forward = defaultdict(list)
        self.inverse = defaultdict(list)

    def insert(self, k, v):
        f = self.forward[k]
        f.append(v)
        self.forward[k] = f

        i = self.inverse[v]
        i.append(k)
        self.inverse[v] = i

    def get(self, k):
        return self.forward[k]

    def get_inverse(self, v):
        return self.inverse[v]


class Module:
    name: str
    module_type: str
    children: List[str]
    count: dict
    module_map: dict
    relations_bimap: BiMap
    work_queue: List

    def __init__(self,
                 name: str,
                 mod: str,
                 children: List[str],
                 module_map,
                 relations_bimap,
                 work_queue,
                 ):
        self.name = name
        self.module_type = mod
        self.children = children
        self.count = {PULSE_TYPE_LO: 0, PULSE_TYPE_HI: 0}
        self.module_map = module_map
        self.relations_bimap = relations_bimap
        self.work_queue = work_queue

    def pulse(self, parent: str, pulse_type: str):
        for child_name in self.children:
            self.count[pulse_type] += 1
            self.work_queue.append((self.name, pulse_type, child_name))


class FlipFlop(Module):
    is_on: bool

    def __init__(self, *args):
        super().__init__(*args)
        self.is_on = False

    def pulse(self, parent: str, pulse_type: str):
        if pulse_type == PULSE_TYPE_HI:
            return
        elif pulse_type == PULSE_TYPE_LO:
            self.is_on = not self.is_on

        if self.is_on:
            pulse_type = PULSE_TYPE_HI
        else:
            pulse_type = PULSE_TYPE_LO

        for child_name in self.children:
            self.count[pulse_type] += 1
            self.work_queue.append((self.name, pulse_type, child_name))


class Conjunction(Module):
    most_recent_pulse: dict

    def __init__(self, *args):
        super().__init__(*args)
        self.most_recent_pulse = defaultdict(lambda: PULSE_TYPE_LO)

    def set_parents(self, parents: List[str]):
        for p in parents:
            self.most_recent_pulse[p] = PULSE_TYPE_LO

    def pulse(self, parent: str, pulse_type: str):
        self.most_recent_pulse[parent] = pulse_type

        s = set(self.most_recent_pulse.values())
        if len(s) == 1 and s.pop() == PULSE_TYPE_HI:
            pulse_type = PULSE_TYPE_LO
        else:
            pulse_type = PULSE_TYPE_HI
        for child_name in self.children:
            self.count[pulse_type] += 1
            self.work_queue.append((self.name, pulse_type, child_name))


def part2(input_file: str):
    module_map = dict()
    relations_bimap = BiMap()
    work_queue = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            temp = line.split("->")
            module_str = temp[0].strip()

            module_name = ""
            module_type = ""
            if BROADCAST in module_str:
                module_type = BROADCAST
                module_name = module_str
            else:
                module_type = module_str[0]
                module_name = module_str[1:]
            children = [s.strip() for s in temp[1].split(",")]

            if module_type == FLIP_FLOP:
                module = FlipFlop(
                    module_name,
                    module_type,
                    children,
                    module_map,
                    relations_bimap,
                    work_queue,
                )
                module_map[module_name] = module
            elif module_type == CONJUNCTION:
                module = Conjunction(
                    module_name,
                    module_type,
                    children,
                    module_map,
                    relations_bimap,
                    work_queue,
                )
                module_map[module_name] = module
            elif module_type == BROADCAST:
                module = Module(
                    module_name,
                    module_type,
                    children,
                    module_map,
                    relations_bimap,
                    work_queue,
                )
                module_map[module_name] = module
            elif module_type == OUTPUT:
                module = Module(
                    module_name,
                    module_type,
                    children,
                    module_map,
                    relations_bimap,
                    work_queue,
                )
                module_map[module_name] = module

            for c in children:
                relations_bimap.insert(module_name, c)
    button = Module(
        "button",
        "button",
        [BROADCAST],
        module_map,
        relations_bimap,
        work_queue,
    )
    module_map["button"] = button

    # Setup conjunctions
    for module_name, module in module_map.items():
        if type(module) is Conjunction:
            parents = relations_bimap.get_inverse(module_name)
            module.set_parents(parents)

    cycle_info = {name: (False, 0)
                  for name in relations_bimap.get_inverse(PARENT_MODULE)}

    button_presses = 0
    while True:
        button_presses += 1
        button.pulse(None, PULSE_TYPE_LO)
        while work_queue:
            parent_module_name, pulse_type, module_name = work_queue.pop(0)

            if parent_module_name in cycle_info.keys() \
                    and pulse_type == PULSE_TYPE_HI \
                    and module_name == PARENT_MODULE:
                cycled, num = cycle_info[parent_module_name]
                if num == 0:
                    cycle_info[parent_module_name] = (
                        cycled, button_presses)
                else:
                    cycle_info[parent_module_name] = (
                        not cycled, button_presses - num)

            if all(map(lambda x: x[0], cycle_info.values())):
                return math.lcm(*map(lambda x: x[1], cycle_info.values()))

            if module_name not in module_map:
                continue
            module = module_map[module_name]
            module.pulse(parent_module_name, pulse_type)
    return button_presses


if __name__ == "__main__":
    print(part2("input.txt"))
