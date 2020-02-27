import csv

def csv_reader(file_obj):
    """
    reader a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))


if __name__ == "__main__":
    csv_path = "TB_data_dictionary_2019-12-27.csv"
    with open(csv_path, "r") as f_obj:
        csv_reader(f_obj)
