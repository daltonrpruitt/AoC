# day 7 : Over 1.5 hours...
from __future__ import annotations

inputs = open("input.txt", 'r').read().splitlines()

class file:
    name = ""
    parent = None
    sub_files = None
    size = 0
    def __init__(self, name, size=None) -> None:
        self.name = name
        if size is not None:
            self.size = size
    
    @classmethod
    def createFile(cls, name, size=None) -> file:
        return cls(name, size)
    
    def set_parent(self, f) -> None:
        self.parent = f
        
    def get_parent(self) -> file:
        return self.parent
        
    # def sub(self, f) -> None:
    #     if self.sub_files is None:
    #         self.sub_files = []
    #     self.sub_files.append(f)
    #     f.set_parent(self)
        # print(str(self), str(f))
        
    def sub(self, name, size=None) -> None:
        f = self.createFile(name, size)
        if self.sub_files is None:
            self.sub_files = []
        self.sub_files.append(f)
        self.sub_files[-1].set_parent(self)
        # print(str(self), str(f))

    def __repr__(self) -> str:
        full_path = ""
        cur = self
        while cur.get_parent() != None:
            full_path = cur.name + "/" + full_path
            cur = cur.get_parent()
        return "/" + full_path

    def calc_size(self):
        if self.size != 0:
            return
        if self.sub_files is None:
            raise Exception("Error: no files but size is 0!")
        total = 0
        for i in self.sub_files:
            if i.size != 0:
                total += i.size
            else:
                i.calc_size()
                total+=i.size
        self.size = total

    # def __str__(self) -> str:
    #     return self.__repr__()


curr_dir = file("/")
i = 1
while i < len(inputs):
    tokens = inputs[i].split(" ")
    if tokens[0] == "$":
        if tokens[1] == "cd":
            # continue
            if tokens[2] == "..":
                curr_dir = curr_dir.get_parent()
            else:
                found = False
                for f in curr_dir.sub_files:
                    if tokens[2] == f.name:
                        found = True
                        curr_dir = f
                if not found:
                    raise Exception("Could not find file with name " + tokens[2] + " in dir "+ curr_dir.name)
            i += 1
        elif tokens[1] == "ls":
            i += 1
            next_line = inputs[i].split(" ")
            while next_line[0] != "$":
                if next_line[0] == "dir":
                    curr_dir.sub(next_line[1])
                else:
                    curr_dir.sub(next_line[1], int(next_line[0]))
                i += 1
                if i >= len(inputs):
                    break
                next_line = inputs[i].split(" ")
            # break

while(curr_dir.get_parent() != None):
    curr_dir = curr_dir.get_parent()

# print(str(curr_dir))

curr_dir.calc_size()

sizes = []

def size_less_than(f: file, size: int):
    if f.sub_files is None:
        return
    
    if f.size <= size:
        # print(str(f), f.size)
        sizes.append(f.size)
        for fs in f.sub_files:
            size_less_than(fs, size)

    else:
        for fs in f.sub_files:
            size_less_than(fs, size)

size_less_than(curr_dir, 100000)

print(len(sizes), sizes)
print(sum(sizes))

curr_size = curr_dir.size
required_to_delete = 30_000_000 - (70_000_000- curr_size)

big_enough = []
def size_greater_than(f: file, size: int):
    if f.sub_files is None:
        return
    if f.size < size:
        return
    
    big_enough.append(f.size)

    for fs in f.sub_files:
        size_greater_than(fs, size)


size_greater_than(curr_dir, required_to_delete)

print(len(big_enough), big_enough)

print(min(big_enough))
