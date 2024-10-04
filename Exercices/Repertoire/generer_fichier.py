def generate_file(file_name):
    open(file_name, 'a').close()

def generate_example_files(core_name):
    generate_file(f"{core_name}.py")
    generate_file(f"test_{core_name}.py")
    generate_file(f"{core_name}.txt")

core_names = ["one", "two", "three", "four", "five", "six", "seven", "height", "nine", "ten"]

for core_name in core_names:
    generate_example_files(core_name)
