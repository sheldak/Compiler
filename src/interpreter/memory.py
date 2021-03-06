from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Memory:
    name: str
    symbols: Dict[str, Any] = field(default_factory=dict)

    def __contains__(self, item):  # variable name
        return item in self.symbols

    def get(self, name):         # gets from memory current value of variable <name>
        return self.symbols[name]

    def put(self, name, value):  # puts into memory current value of variable <name>
        self.symbols[name] = value


@dataclass
class MemoryStack:
    stack: List[Memory] = field(default_factory=lambda: [Memory('global')])

    def __contains__(self, item):
        return self._find(item) is not None

    def get(self, name):             # gets from memory stack current value of variable <name>
        memory = self._find(name)
        if memory:
            return memory.get(name)
        else:
            return None

    def set(self, name, value):  # inserts into memory stack variable <name> with value <value>
        memory: Memory = self._find(name)
        if not memory:
            memory = self.stack[-1]

        memory.put(name, value)

    def push(self, name):  # creates new memory and pushes it onto the stack
        self.stack.append(Memory(name=name))

    def pop(self):          # pops the top memory from the stack
        self.stack.pop()

    def get_memory_name(self):
        return self.stack[-1].name

    def _find(self, name):  # finds first <memory> containing <name>
        for mem in self.stack[::-1]:
            if name in mem:
                return mem
        return None
