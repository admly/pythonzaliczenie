def create_routes_config_file(path, filename, osSystem):
    if osSystem == "Windows":
        file_to_write = open("addRoutesWindows.bat", 'w')

        with open(path + filename) as f:
            for line in f:
                result = [x.strip() for x in line.split('/')]
                file_to_write.write("route add " + result[0]+" netmask "
                                    + result[1] + " " + result[2]+'\n')
            f.close()
            file_to_write.close()
        print("wygenerowano plik dla Windows")

    if osSystem == "Linux":
        file_to_write = open("addRoutesLinux.sh", 'w')

        with open(path + filename) as f:
            for line in f:
                result = [x.strip() for x in line.split('/')]
                file_to_write.write("route add -net " + result[0]+" netmask "
                                    + result[1] + " gw " + result[2]+'\n')
            f.close()
            file_to_write.close()
        print("wygenerowano plik dla Linux")

    if osSystem == "Cisco":
        file_to_write = open("addRoutesCisco", 'w')

        with open(path + filename) as f:
            for line in f:
                result = [x.strip() for x in line.split('/')]
                file_to_write.write("route " + result[0]+" "
                                    + result[1] + " " + result[2]+'\n')
            f.close()
            file_to_write.close()
        print("wygenerowano plik dla Cisco")


ipList = input("Podaj sciezke do pliku (separator - /): ")
filename = input("Podaj nazwe pliku: ")

while True:
    osSystem = input("Podaj dla jakiego systemu chcesz wygenerowac plik (Windows, Linux lub Cisco): ")
    if osSystem == "Windows" or osSystem == "Linux" or osSystem == "Cisco":
        break
    else:
        print("Podaj nazwe z dozwolonych - Linux, Windows lub Cisco")

create_routes_config_file(ipList, filename, osSystem)
