class FamousFragrance:

    def __init__(self, name: str, brand: str, projection: str, size: int):
        # Public attributes (+)
        self.name = name
        self.brand = brand

        self.__projection = projection
        self.__size = size  # size in ml

    def spray(self, sprays: int = 1):
        ml_used = sprays * 1  # 1 spray = 1 ml
        if self.__size >= ml_used:
            self.__size -= ml_used
            print(f">> Sprayed {self.name} {sprays} time(s).")
        else:
            print(f">> Not enough fragrance left to spray {sprays} time(s)!")

    def smell(self):
        """Prints scent details."""
        print(
            f"Scent Profile: {self.name} by {self.brand} with {self.__projection} projection."
        )

    def get_details(self) -> str:
        """Safely reads and returns private attribute information as a string."""
        return f"{self.name} by {self.brand} | Size: {self.__size}ml | Projection: {self.__projection}"


if __name__ == "__main__":
    fragrance1 = FamousFragrance(
        name="Bleu de Chanel", brand="Chanel", projection="Strong", size=100
    )
    fragrance2 = FamousFragrance(
        name="Santal 33", brand="Le Labo", projection="Moderate", size=50
    )

    print("--- BEFORE ---")
    print(f"Object 1: {fragrance1.get_details()}")
    print(f"Object 2: {fragrance2.get_details()}")
    print()

    print("Action: Performing spray(20) on Object 1...")
    fragrance1.spray(20)
    print()

    print("--- AFTER ---")
    print(f"Object 1: {fragrance1.get_details()}")
    print(f"Object 2: {fragrance2.get_details()}")