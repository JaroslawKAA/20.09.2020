import sys


NAME_INDEX = 0

def generate_raport(data_list, filename, reportname):
    output = []

    output.append(f"Nazwa pliku wejściowego: {filename}")
    output.append(f"Nazwa pliku wejściowego: {reportname}")
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


def get_filename_raportname():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        reportname = sys.argv[2]
        return filename, reportname
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
    filename, raportname = get_filename_raportname()
    if len(filename) == 0:
        return

    print(f"File opened: {filename}")
    data_list = read_file_to_list(filename)
    print(data_list)
    raport = generate_raport(data_list, filename, raportname)
    print(raport)
    save_raport_to_file(raport, raportname)

if __name__ == "__main__":
    main()