from colorama import Fore
import sys
from pathlib import Path


def view_files(path_name: str, i: int):
    try:
        directory = Path(path_name)
        try:
            for x in sorted(directory.iterdir()):
                if x.is_dir():
                    print(f"{' '*i}┣ 📂 {Fore.YELLOW}[FOLDER] {Fore.RESET} {x.name}")
                    view_files(x.absolute(), i+3)
                if x.is_file():
                    if x.suffix in [".jpg", ".png", ".svg"]:
                        print(f"{' '*i}┣ 🎨 {Fore.BLUE}[IMAGE] {Fore.RESET} {x.name}")
                    else:
                        print(f"{' '*i}┣ 📜 {Fore.GREEN}[File] {Fore.RESET} {x.name}")
        except IndexError as e:
            print(f"{Fore.RED}[WARMING] {e} {Fore.RESET}")
    except FileNotFoundError:
        print(f"{Fore.RED}[WARMING] Не вдалось знайти директорію за вказаним шляхом!{Fore.RESET}")


path = sys.argv[1] + " " + sys.argv[2] if len(sys.argv) > 2 else sys.argv[1]
print(f"📦 {path}")
view_files(path, 1)
