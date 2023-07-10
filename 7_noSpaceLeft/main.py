import os
import string


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.name} (file, size={self.size})'


class Directory:

    def __init__(self, pd, name):
        self.parentDirectory = pd
        self.name = name
        self.files = []
        self.children = []
        self.size = 0

    def addFile(self, file):
        self.files.append(file)

    def addChild(self, dir):
        self.children.append(dir)

    def __str__(self):
        result = f'{self.name} (dir)\n'
        for f in self.files:
            result += f'  {f}\n'
        for c in self.children:
            result += f'    {str(c)}'
        return result

    def calculate_size(self):
        total = 0
        for f in self.files:
            total += f.size
        for c in self.children:
            total += c.calculate_size()
        self.size = total
        return total

    def sum_under_10000(self):
        total = 0
        for c in self.children:
            if c.size > 10000:
                total += c.size
        return total


        # PART 1
with open('7_noSpaceLeft\input0.txt') as f:
    lines = f.read().splitlines()
fileSystem = []
currentDirectory = Directory(None, '/')
fileSystem.append(currentDirectory)
l = 1
while (l < len(lines)):
    print(l)
    components = lines[l].split(' ')
    if components[0] == '$':
        command = components[1]
        match command:
            case 'cd':
                arg = components[2]
                match arg:
                    case '..':
                        currentDirectory = currentDirectory.parentDirectory
                    case _:
                        if any(x.name == arg for x in fileSystem):
                            currentDirectory = first(
                                x.name == arg for x in fileSystem)
                            continue
                        else:
                            newDirectory = Directory(currentDirectory, arg)
                            currentDirectory.addChild(newDirectory)
                            fileSystem.append(newDirectory)
                            currentDirectory = newDirectory
                l += 1
            case 'ls':
                l += 1
                element = lines[l]
                while element[0] != '$':
                    arg, name = element.split(' ')
                    if arg == 'dir':
                        childDirectory = Directory(currentDirectory, name)
                        if not any(x.name == name for x in currentDirectory.children):
                            currentDirectory.addChild(childDirectory)
                    else:
                        file = File(name, int(arg))
                        if not any(x.name == name for x in currentDirectory.files):
                            currentDirectory.addFile(file)
                    l += 1
                    if l > len(lines)-1:
                        break
                    element = lines[l]
fileSystem[0].calculate_size()
print(fileSystem[0].sum_under_10000())
