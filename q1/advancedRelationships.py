"""
Filename: advancedRelationships.py
Description: Advanced Class Relationships (Inheritance, Composition, Dependency)
             for the Fragrance System.
"""


# --- Composition Component ---
class Atomizer:
    """Represents an atomizer spray mechanism physically built into a fragrance bottle."""

    def __init__(self, spray_rate_ml: int = 1):
        self.spray_rate_ml = spray_rate_ml

    def dispense(self, sprays: int) -> int:
        """Calculates total liquid volume dispensed based on spray count."""
        return sprays * self.spray_rate_ml


# --- Parent Class ---
class FamousFragrance:
    """Parent class representing a general fragrance bottle."""

    def __init__(self, name: str, brand: str, projection: str, size: int):
        self.name = name
        self.brand = brand
        self._projection = projection
        self.__size = size  # Private attribute (in ml)

        # Composition: FamousFragrance HAS-A Atomizer
        self.atomizer = Atomizer(spray_rate_ml=1)

    @property
    def size(self) -> int:
        """Getter for private size attribute."""
        return self.__size

    @size.setter
    def size(self, new_size: int):
        """Setter for private size attribute with validation."""
        if new_size >= 0:
            self.__size = new_size

    def spray(self, sprays: int = 1):
        """Sprays fragrance using its internal atomizer component."""
        ml_used = self.atomizer.dispense(sprays)
        if self.__size >= ml_used:
            self.__size -= ml_used
            print(
                f">> Sprayed {self.name} {sprays} time(s) ({ml_used}ml"
                " dispensed)."
            )
        else:
            print(
                f">> Not enough fragrance left in {self.name} to spray"
                f" {sprays} time(s)!"
            )

    def smell(self):
        """Prints scent details."""
        print(
            f"Scent Profile: {self.name} by {self.brand} with"
            f" {self._projection} projection."
        )

    def get_details(self) -> str:
        """Safely reads and returns private attribute information as a string."""
        return (
            f"{self.name} by {self.brand} | Size: {self.__size}ml | Projection:"
            f" {self._projection}"
        )


# --- Child Class (Inheritance) ---
class LimitedEditionFragrance(FamousFragrance):
    """Child class inheriting from FamousFragrance with limited batch details."""

    def __init__(
        self,
        name: str,
        brand: str,
        projection: str,
        size: int,
        batch_number: str,
        bottle_number: int,
        total_produced: int,
    ):
        # Call Parent __init__ using super()
        super().__init__(name, brand, projection, size)
        self.batch_number = batch_number
        self.bottle_number = bottle_number
        self.total_produced = total_produced

    def verify_authenticity(self) -> str:
        """Verifies the bottle number against the batch production."""
        return (
            f"Authentic Bottle #{self.bottle_number} of {self.total_produced}"
            f" (Batch: {self.batch_number})"
        )

    def get_details(self) -> str:
        """Overrides parent get_details to include limited edition metadata."""
        base_details = super().get_details()
        return (
            f"{base_details} | Limited Edition [Batch: {self.batch_number} |"
            f" #{self.bottle_number}/{self.total_produced}]"
        )


# --- Dependency Class ---
class ScentTester:
    """Represents a temporary testing strip used to evaluate fragrances."""

    def __init__(self, material: str = "Blotting Paper"):
        self.material = material

    def evaluate_spray(self, fragrance_name: str):
        print(
            f"   [Tester Strip ({self.material})]: Absorbed spray of"
            f" '{fragrance_name}'. Analyzing top notes..."
        )


# --- Associated Class ---
class Collector:
    """Represents a fragrance collector managing a collection."""

    def __init__(self, name: str):
        self.name = name
        self.collection = []

    def add_fragrance(self, fragrance: FamousFragrance):
        self.collection.append(fragrance)
        print(f"Added '{fragrance.name}' to {self.name}'s collection.")

    def display_collection(self):
        print(f"\n--- {self.name}'s Fragrance Collection ---")
        if not self.collection:
            print("The collection is currently empty.")
        for item in self.collection:
            print(f"- {item.get_details()}")
        print("-" * 42 + "\n")

    def test_fragrance_sample(
        self, fragrance: FamousFragrance, tester: ScentTester
    ):
        """USES-A relationship: Temporarily uses ScentTester to test a fragrance."""
        print(
            f"{self.name} is testing '{fragrance.name}' using a"
            f" {tester.material} tester..."
        )
        tester.evaluate_spray(fragrance.name)


# --- Demonstration & Testing ---
if __name__ == "__main__":
    print("==================================================")
    print("      ADVANCED CLASS RELATIONSHIPS DEMO           ")
    print("==================================================\n")

    # 1. Test Inheritance
    print("--- Test 1: Inheritance (Child Class Uses Parent & Super) ---")
    standard_fragrance = FamousFragrance(
        name="Bleu de Chanel", brand="Chanel", projection="Strong", size=100
    )
    limited_fragrance = LimitedEditionFragrance(
        name="Santal 33 Collector Edition",
        brand="Le Labo",
        projection="Moderate",
        size=50,
        batch_number="BATCH-2026-X",
        bottle_number=42,
        total_produced=500,
    )

    print("Standard Fragrance Details:", standard_fragrance.get_details())
    print("Limited Edition Details:   ", limited_fragrance.get_details())
    print("Authenticity Check:        ", limited_fragrance.verify_authenticity())
    print()

    # 2. Test Composition
    print("--- Test 2: Composition (Fragrance HAS-A Atomizer) ---")
    print(
        f"Initial size of {limited_fragrance.name}: {limited_fragrance.size}ml"
    )
    limited_fragrance.spray(5)
    print(
        f"Updated size of {limited_fragrance.name}: {limited_fragrance.size}ml"
    )
    print()

    # 3. Test Aggregation & Dependency
    print("--- Test 3: Aggregation & Dependency ---")
    collector = Collector(name="John Doe")

    collector.add_fragrance(standard_fragrance)
    collector.add_fragrance(limited_fragrance)

    disposable_tester = ScentTester(material="Cotton Blotter")
    collector.test_fragrance_sample(limited_fragrance, disposable_tester)

    collector.display_collection()