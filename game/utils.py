from colorama import Fore, Style
from character import Character


def divider():
    print("=" * 30)


def show_status(p1, p2, turn):
    divider()
    print(Fore.CYAN + Style.BRIGHT + f"TURN {turn}" + Style.RESET_ALL)
    print(f"{p1.name}: {Fore.RED}♥ {p1.life}{Style.RESET_ALL}  | {Fore.YELLOW}⚡ {p1.stamina}{Style.RESET_ALL}")
    print(f"{p2.name}: {Fore.RED}♥ {p2.life}{Style.RESET_ALL}  | {Fore.YELLOW}⚡ {p2.stamina}{Style.RESET_ALL}")
    divider()
    

def show_status_manual(p1, p2, turn):
    divider()
    print(Fore.CYAN + Style.BRIGHT + f"TURN {turn}" + Style.RESET_ALL)
    print(f"{p1.name}: {Fore.RED}♥ {p1.life}{Style.RESET_ALL}  | {Fore.YELLOW}⚡ {p1.stamina}{Style.RESET_ALL} | {Fore.BLUE}⚔️ {p1.attack}{Style.RESET_ALL} | {Fore.GREEN}🛡️ {p1.defense}{Style.RESET_ALL}")
    print(f"{p2.name}: {Fore.RED}♥ {p2.life}{Style.RESET_ALL}  | {Fore.YELLOW}⚡ {p2.stamina}{Style.RESET_ALL} | {Fore.BLUE}⚔️ {p2.attack}{Style.RESET_ALL} | {Fore.GREEN}🛡️ {p2.defense}{Style.RESET_ALL}")
    divider()
    
def show_status_manual_started(p1, p2):
    divider()
    print(Fore.CYAN + Style.BRIGHT + f"Players Status:\n" + Style.RESET_ALL)
    print(f"{p1.name}: {Fore.RED}♥ {p1.life}{Style.RESET_ALL}  | {Fore.YELLOW}⚡ {p1.stamina}{Style.RESET_ALL} | {Fore.BLUE}⚔️ {p1.attack}{Style.RESET_ALL} | {Fore.GREEN}🛡️ {p1.defense}{Style.RESET_ALL}")
    print(f"{p2.name}: {Fore.RED}♥ {p2.life}{Style.RESET_ALL}  | {Fore.YELLOW}⚡ {p2.stamina}{Style.RESET_ALL} | {Fore.BLUE}⚔️ {p2.attack}{Style.RESET_ALL} | {Fore.GREEN}🛡️ {p2.defense}{Style.RESET_ALL}")
    divider()


def reset_players():
    return Character("Hero", 200, 40, 30, 30), Character("Villain", 200, 40, 30, 30)