import os


def find_string_in_catalogue(path, string):
    print(stringToFind + " found in files:")
    for x in os.listdir(path):
        with open(path + x) as f:
            if string in f.read():
                print(f.name)


directoryToSearch = input("Podaj pelna sciezke do katalogu (separator - /): ")
stringToFind = input("Podaj slowo do znalezienia: ")

find_string_in_catalogue(directoryToSearch, stringToFind)