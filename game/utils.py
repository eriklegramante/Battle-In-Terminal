from colorama import Fore, Style

def divider():
    print("=" * 30)


def show_status(p1, p2, turn):
    divider()
    print(Fore.CYAN + Style.BRIGHT + f"TURN {turn}" + Style.RESET_ALL)
    print(f"{p1.name}: {Fore.RED}♥ {p1.life}{Style.RESET_ALL}  | {Fore.YELLOW}⚡ {p1.stamina}{Style.RESET_ALL}")
    print(f"{p2.name}: {Fore.RED}♥ {p2.life}{Style.RESET_ALL}  | {Fore.YELLOW}⚡ {p2.stamina}{Style.RESET_ALL}")
    divider()

