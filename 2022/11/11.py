# day 11

import numpy as np
from copy import deepcopy


sample = False
# sample = True
debug = False
# debug = True



if not sample:
    lines = open("input.txt", 'r').read().splitlines()
else:
    lines = open("sample_input.txt", 'r').read().splitlines()

gcm_tests = None

class monkey:
    operation_ = None
    test_ = None
    items_ = None
    started_ = False
    inspections_ = 0
    div_by_3 = True
    
    def __init__(self) -> None:
        return
    
    def set_start(self, starting_items, true_m, false_m, test_v, op, op_v=None) -> None:
        self.items_ = starting_items
        self.op_ = op
        self.op_v = op_v
        self.true_m = true_m
        self.false_m = false_m
        self.test_v = test_v
        self.started_ = True
        
    def add_item(self, item):
        self.items_.append(item)
        
    def turn(self):
        if not self.started_: 
            raise Exception("monkey not started!")

        for i in range(len(self.items_)):
            self.inspections_ += 1
            item = self.items_.pop(0)
            item = self.op_(item, item) if self.op_v is None else self.op_(item, self.op_v)
            if self.div_by_3: 
                item = item // 3
            elif gcm_tests is not None:
                item = item % gcm_tests
            if (item % self.test_v) == 0:
                self.true_m.add_item(item)
            else: 
                self.false_m.add_item(item)
        
    def print_items(self, prefix=""):
        for item in self.items_:
            print(prefix, item)

monkeys = []
for i in range(4 if sample else 8):
    monkeys.append(monkey())

i = 0
for li in range(len(lines)):
    if lines[li] == "":
        continue
    starting_items = None
    operation = None
    op_v = None
    test = None
    true_m = None
    false_m = None

    if lines[li].find("Monkey") != -1:
        _, items = lines[li+1].split("items: ")
        starting_items =  [int(x) for x in items.split(", ")]
        _, op = lines[li+2].split("Operation: new = old ")
        op = op.split(" ")
        if op[0] == "*":
                operation = lambda n,m: n*m
        elif op[0] == "+":
            operation = lambda n,m : n+m
        else:
            raise Exception("Should not get here, bad op?")
        if op[1] != "old":
            op_v = int(op[1])
        _, test_v = lines[li+3].split("Test: divisible by ")
        # test_f = lambda n: (n%int(test_v)) == 0
        _, true_m = lines[li+4].split("If true: throw to monkey ")
        true_m = int(true_m)
        _, false_m = lines[li+5].split("If false: throw to monkey ")
        false_m = int(false_m)

        monkeys[i].set_start(
                starting_items,
                monkeys[true_m],
                monkeys[false_m],
                int(test_v),
                operation,
                op_v
        )
        i += 1
        if i >= len(monkeys):
            break
        li += 6
monkeys_copy = deepcopy(monkeys)

for i in range(20):
    for m in monkeys:
        m.turn()
    
    for mi in range(len(monkeys)):
        print("Monkey ",mi, ":")
        monkeys[mi].print_items("\t")

inspections = []
for m in monkeys:
    inspections.append(m.inspections_)
inspections.sort(reverse=True)
most = inspections[:2]
print("Part 1 monkey business = ", most[0]*most[1])

gcm_tests = 1
for m in monkeys_copy:
    m.div_by_3 = False
    gcm_tests*= m.test_v

for i in range(10000):
    for m in monkeys_copy:
        m.turn()
    
    # for mi in range(len(monkeys_copy)):
        # print("Monkey ",mi, ":")
        # monkeys_copy[mi].print_items("\t")

inspections = []
for m in monkeys_copy:
    inspections.append(m.inspections_)
inspections.sort(reverse=True)
most = inspections[:2]
print("Part 2 monkey business = ", most[0]*most[1])
