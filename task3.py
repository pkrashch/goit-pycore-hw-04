import sys
from pathlib import Path
from colorama import init, Fore, Style

def visualize_structure(path, prefix=''):
    for item in path.iterdir():
        if item.is_dir():
            # print directory name in blue color
            print(f"{prefix}{Fore.BLUE}📂 {item.name}/{Style.RESET_ALL}")
            #increasing prefix
            new_prefix = prefix + "|    "   
            # recursive call
            visualize_structure(item, new_prefix)
        else:
            # print file name
            print(f"{prefix}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")

def main():
    # Initialise Colorama 
    init()

    if len(sys.argv) != 2:
        print("Path and only path is expected") #uther either hasn't entered the path or entered extra arguments
        sys.exit(1)

    path_str = sys.argv[1]
    target_path = Path(path_str)
    #Check that provided path exists and leads to the directiry
    if not target_path.exists() or not target_path.is_dir(): 
        print("Provided path is either invalid or is not a directory.")
        sys.exit(1)
    
    print(f"\nStructure for: {Fore.CYAN}{target_path}{Style.RESET_ALL}")
    visualize_structure(target_path)

if __name__ == "__main__":
    main()