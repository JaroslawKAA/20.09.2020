import sys


NAME_INDEX = 0

def generate_raport(data_list):
    output = []

    output.append(f"Ilość danych: {len(data_list)}.")
    output.append(f"\nImiona: {get_names(data_list)}")

    return output


def get_names(data_list):
    names = []

    for line in data_list:
        names.append(line[NAME_INDEX])

    return ", ".join(names)


def save_raport_to_file(raport, filename):
    with open(filename, "w+") as file_to_read:
        for raport_data in raport:
            file_to_read.write(raport_data)



def get_filename():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        return filename
    else:
        print("[ WARNING ] You should run this program by calling: python parser.py filename.")
        return ""


def read_file_to_list(filename):
    output = []
    with open(filename, "r") as file_to_read:
        for line in file_to_read.readlines():
            row = line.replace("\n", ""). split(" ")
            output.append(row)
    return output


def main():
    filename = get_filename()
    if len(filename) == 0:
        return

    print(f"File opened: {filename}")
    data_list = read_file_to_list(filename)
    print(data_list)
    raport = generate_raport(data_list)
    print(raport)
    save_raport_to_file(raport, "raport.txt")

if __name__ == "__main__":
    main()