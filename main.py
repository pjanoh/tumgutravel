PRICES = {"msc": 13_000, "spb": 10_000, "ekb": 8_000}

def read_choice(prompt: str, options: set[str]) -> str:
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice

def read_nonneg_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if value >= 0:
                return value
        except ValueError:
            pass

def main() -> None:
    dist = read_choice("Введите пункт поездки (msc, spb, ekb): ", set(PRICES))
    adults = read_nonneg_int("Введите количество взрослых: ")
    kids = read_nonneg_int("Введите количество детей: ")
    total = PRICES[dist] * (2 * adults + kids) // 2
    print(f"Цена поездки: {total:,}".replace(",", " "))

if __name__ == "__main__":
    main()
