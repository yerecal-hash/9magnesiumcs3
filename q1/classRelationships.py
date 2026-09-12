class FamousFragrance:
    def __init__(self, name: str, brand: str, projection: str, size: int):
        self.name = name
        self.brand = brand
        self.__projection = projection
        self.__size = size 

    def spray(self, sprays: int = 1):
        ml_used = sprays * 1 
        if self.__size >= ml_used:
            self.__size -= ml_used
            print(f">> Sprayed {self.name} {sprays} time(s).")
        else:
            print(f">> Not enough fragrance left to spray {sprays} time(s)!")

    def smell(self):
        print(f"Scent Profile: {self.name} by {self.brand} with {self.__projection} projection.")

    def get_details(self) -> str:
        return f"{self.name} by {self.brand} | Size: {self.__size}ml | Projection: {self.__projection}"


class Collector:
    def __init__(self, name: str):
        self.name = name
        self.collection = [] 

    def add_fragrance(self, fragrance: FamousFragrance):
        self.collection.append(fragrance)
        print(f"Added {fragrance.name} to {self.name}'s collection.")

    def display_collection(self):
        print(f"\n--- {self.name}'s Fragrance Collection ---")
        if not self.collection:
            print("The collection is currently empty.")
        for item in self.collection:
            print(f"- {item.get_details()}")
        print("------------------------------------------\n")


if __name__ == "__main__":
    # A. Objects before association
    print("--- BEFORE RELATIONSHIP ---")
    fragrance1 = FamousFragrance(name="Bleu de Chanel", brand="Chanel", projection="Strong", size=100)
    fragrance2 = FamousFragrance(name="Santal 33", brand="Le Labo", projection="Moderate", size=50)
    fragrance3 = FamousFragrance(name="Sauvage", brand="Dior", projection="Strong", size=200)

    collector1 = Collector(name="John Doe")
    print(f"Created collector: {collector1.name}")
    print(f"Created independent fragrances: {fragrance1.name}, {fragrance2.name}, {fragrance3.name}\n")

    # B. Association being formed
    print("--- BUILDING RELATIONSHIP ---")
    collector1.add_fragrance(fragrance1)
    collector1.add_fragrance(fragrance2)
    collector1.add_fragrance(fragrance3)

    # C. Relationship after association
    print("\n--- AFTER RELATIONSHIP ---")
    print("Related objects accessed through the Collector:")
    collector1.display_collection()
    
    # Demonstrating object interaction
    print("Action: Performing spray(15) on the first item in the collection...")
    collector1.collection[0].spray(15)
    collector1.display_collection()