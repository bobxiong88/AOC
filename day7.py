import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

# code goes here

def parse_ls(s):
    items = s.split()
    result = []
    for i in range(0, len(items), 2):
        if items[i] == "dir":
            result.append({"type": "dir", "name": items[i + 1]})
        else:
            result.append({"type": "file", "name": items[i + 1], "size": int(items[i])})
    return result
def calculate_total_size(structure, dir):
    if dir not in structure:
        return 0
    total_size = 0
    for item in structure[dir]:
        if item["type"] == "file":
            total_size += item["size"]
        else:
            total_size += calculate_total_size(structure, dir + "/" + item["name"])
    return total_size
def solve(inp):
    structure = {"/": []}
    cur_dir = "/"
    for line in inp.strip().split("\n"):
        if line.startswith("$"):
            # Parse command
            cmd, *args = line[1:].split()
            if cmd == "cd":
                if args[0] == "..":
                    cur_dir = "/".join(cur_dir.split("/")[:-1])
                elif args[0] == "/":
                    cur_dir = "/"
                else:
                    cur_dir += "/" + args[0]
            elif cmd == "ls":
                items = parse_ls(args[0])
                structure[cur_dir] = items
    # Calculate the sum of the total sizes of the directories with a total size of at most 100000
    total_size = 0
    for dir in structure:
        dir_total_size = calculate_total_size(structure, dir)
        if dir_total_size <= 100000:
            total_size += dir_total_size
    return total_size
inp = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
print(solve(inp))


fin.close()
fout.close()
