class Directory:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}
        self.total_size = 0

    def __repr__(self):
        return f"{self.name}: {len(self.children)} {self.total_size}"


def part_1(file_path: str) -> int:
    root_dir = parse_file(file_path)

    directory_sizes = []
    get_directory_sizes(root_dir, directory_sizes)

    total_size = sum([dir_size for dir_size in directory_sizes if dir_size <= 100000])
    return total_size


def part_2(file_path: str) -> int:
    root_dir = parse_file(file_path)

    free_space = 70000000 - root_dir.total_size
    required_space = 30000000 - free_space

    directory_sizes = []
    get_directory_sizes(root_dir, directory_sizes)

    min_dir_size = min([x for x in directory_sizes if x >= required_space])
    return min_dir_size


def parse_file(file_path: str) -> Directory:
    root_dir = Directory('root', None)
    current_dir = None
    with open(file_path, 'r') as f:
        for line in f:
            line_parts = line.rstrip('\n').split(' ')
            if line_parts[1] == 'cd':
                directory = line_parts[2]
                if directory == '..':
                    current_dir = current_dir.parent
                else:
                    if current_dir is None:
                        current_dir = root_dir
                    elif directory in current_dir.children:
                        current_dir = current_dir.children[directory]
                    else:
                        new_dir = Directory(directory, current_dir)
                        current_dir.children[directory] = new_dir
                        current_dir = new_dir
            elif line_parts[1] == 'ls':
                continue
            elif line_parts[0] == 'dir':
                directory = line_parts[1]
                if directory not in current_dir.children:
                    new_dir = Directory(directory, current_dir)
                    current_dir.children[directory] = new_dir
            else:
                file_size = int(line_parts[0])
                file_name = line_parts[1]
                current_dir.files[file_name] = file_size

    calc_dir_size(root_dir)
    return root_dir


def calc_dir_size(directory: Directory) -> int:
    for file_size in directory.files.values():
        directory.total_size += file_size

    for sub_directory in directory.children.values():
        directory.total_size += calc_dir_size(sub_directory)

    return directory.total_size


def get_directory_sizes(directory, directory_sizes):
    directory_sizes.append(directory.total_size)
    for sub_directory in directory.children.values():
        get_directory_sizes(sub_directory, directory_sizes)
