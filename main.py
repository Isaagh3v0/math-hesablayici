from colorama import Fore
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    clear_console()
    title = 'Salam, sən nə etmək istəyirsən?'
    options = ['Üçbucağın perimetrini tapmağ', 'Düzbucağın perimetrini tapmağ', 'Kvadratın sahəsini tapmağ', 'Trapesianın sahəsini tapmağ']

    print(Fore.YELLOW + """⣀⡀⠀⣀⠀⣀⡀⠀⢀⣀⣀⣀⢀⣀⢀⣀
⢸⢱⢰⢹⠀⡜⢣⠀⠘⠀⡇⠘⠀⡧⠤⡇
⠼⠄⠁⠼⠴⠍⠩⠦⠀⠤⠧⠄⠠⠧⠠⠧

⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀
⢸⠔⠒⡄⠐⡖⠐⡖⠀⠀⠀⠀⢠⣒⣒⡄⠐⡦⠒⡄⠀⠒⡆⠀⢠⠒⠢⡖⢲⠔⡤⢢⠠⣒⣒⡄
⠼⠢⠤⠃⠀⠘⡜⠀⠀⠀⠀⠀⠘⠤⠤⠄⠠⠧⠠⠧⠠⠤⠧⠤⠘⠤⠔⡇⠼⠄⠧⠸⠘⠤⠔⠧
⠀⠀⠀⠀⠀⠚⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠁""" + Fore.WHITE)
    print(title)
    
    for i, option in enumerate(options, 1):
        print(Fore.GREEN + f"{i}. " + Fore.WHITE + option)
    
    choice = input(Fore.CYAN + "Zəhmət olmasa bir seçim edin (rəqəm daxil edin): " + Fore.WHITE)
    
    try:
        choice = int(choice)
        if 1 <= choice <= len(options):
            clear_console()
            match choice:
                case 1:
                    try:
                        aPos = int(input(Fore.BLUE + "> " + Fore.MAGENTA + "A tərəfinin uzunluğunu daxil edin: " + Fore.WHITE))
                        bPos = int(input(Fore.BLUE + "> " + Fore.MAGENTA + "B tərəfinin uzunluğunu daxil edin: " + Fore.WHITE))
                        cPos = int(input(Fore.BLUE + "> " + Fore.MAGENTA + "C tərəfinin uzunluğunu daxil edin: " + Fore.WHITE))

                        print(Fore.BLUE + f"Üçbucaqın perimetri: {aPos + bPos + cPos}")
                    except:
                        raise ValueError
                case 2:
                    try:
                        aPos = int(input(Fore.BLUE + "> " + Fore.MAGENTA + "A tərəfinin uzunluğunu daxil edin: " + Fore.WHITE))
                        bPos = int(input(Fore.BLUE + "> " + Fore.MAGENTA + "B tərəfinin uzunluğunu daxil edin: " + Fore.WHITE))

                        print(Fore.BLUE + f"Düzbucaqın perimetri: {2 * (aPos + bPos)}")
                    except:
                        raise ValueError
                case 3:
                    try:
                        aPos = int(input(Fore.BLUE + "> " + Fore.MAGENTA + "A tərəfinin uzunluğunu daxil edin: " + Fore.WHITE))

                        print(Fore.BLUE + f"Kvadratın sahəsi: {aPos ** 2}")
                    except:
                        raise ValueError
                case 4:
                    try:
                        aPos = int(input(Fore.BLUE + "> " + Fore.MAGENTA + "A tərəfinin uzunluğunu daxil edin: " + Fore.WHITE))
                        bPos = int(input(Fore.BLUE + "> " + Fore.MAGENTA + "B tərəfinin uzunluğunu daxil edin: " + Fore.WHITE))
                        hPos = int(input(Fore.BLUE + "> " + Fore.MAGENTA + "h tərəfinin uzunluğunu daxil edin: " + Fore.WHITE))

                        print(Fore.BLUE + f"Trapesianın sahəsi: {(aPos + bPos) * hPos / 2}")
                    except:
                        raise ValueError
        else:
            raise ValueError
    except ValueError:
        print(Fore.RED + "Düzgün seçim edin!")
