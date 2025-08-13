import os
# run program to update index file to show updated gallery

def main():
    files = []
    existing = []

    with open("images/gallery/index", "r") as f:
        existing = f.read().splitlines()


    for file in os.listdir("images/gallery/"):
        if file != "index":
            files.append(file)
    
    for filename in files:
        if filename not in existing:
            with open("images/gallery/index", "a") as f:
                f.write(f"{filename}\n")
    

if __name__ == "__main__":
    main()