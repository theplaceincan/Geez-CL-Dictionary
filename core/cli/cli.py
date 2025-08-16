# *******************************
# *** English-Geez Dictionary ***
# *******************************
# Written by theplaceincan (Github)

# import geezcore

HEADER = """
=================================================
Welcome to the Geez - English offline dictionary
=================================================
"""

def choose_search_type() -> str:
    while True:
        print("Select which type of search you'd like to use (you can change anytime).")
        print("1. Transliterated Geez (G)")
        print("2. English definition (E)")
        choice = input("\nEnter your choice (1/G or 2/E): ").strip().lower()
        if choice in ("1", "g"):
            print("\nYou selected Transliterated Geez search.\n")
            return "geez"
        elif choice in ("2", "e"):
            print("\nYou selected English definition search.\n")
            return "english"
        else:
            print("\nInvalid choice, please try again.\n")

def main() -> None:
    print(HEADER)
    mode = choose_search_type()

    print("Type ':mode' to change search mode, ':quit' to exit.\n")
    while True:
        query = input(f"{mode}> ").strip()
        if not query:
            continue
        cmd = query.lower()
        if cmd in (":quit", ":q", "quit", "exit"):
            print("Goodbye!")
            break
        if cmd in (":mode", ":m"):
            mode = choose_search_type()
            continue

        if mode == "geez":
            print("you've been trolled")
            # results = geezcore.search_geez(query)
        else:
            print("you've been trolled part 2")
            # results = geezcore.search_english(query)
        # print(results)

        print(f"[demo] Searching ({mode}) for: {query}")

if __name__ == "__main__":
    main()
