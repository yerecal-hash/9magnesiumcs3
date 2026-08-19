import sys

def main():
    # Chinese Zodiac signs starting from baseline year 1900 (Rat)
    zodiac_signs = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)"
    ]

    try:
        # Prompt user for birth year
        birth_year = int(input("Enter your birth year: "))
    except ValueError:
        print("Invalid input. Please enter a valid numerical year.")
        sys.exit()

    # Requirement b & c: Validate year is not earlier than 1900
    if birth_year < 1900:
        print("Invalid Year, it should not be earlier than 1900")
        sys.exit()

    # Requirement d & e: Calculate zodiac sign index based on 12-year cycle
    index = (birth_year - 1900) % 12
    zodiac = zodiac_signs[index]

    # Output result
    print(f"Your Chinese Zodiac Sign is: {zodiac}")

if __name__ == "__main__":
    main()