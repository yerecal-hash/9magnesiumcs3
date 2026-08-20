# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
- Encapsulation bundles the store product's attributes, such as name, price, and quantity, together with methods that modify them into a single "Product" class while restricting direct access to internal data. For instance, private fields like "_quantity" can be modified using controlled public methods like "restock(amount)" or "sell(amount)" rather than allowing direct assignment. This ensures data integrity by preventing invalid states, such as setting a negative product price or selling items when stock is insufficient.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self._quantity = quantity  # Encapsulated state

    def sell(self, amount):
        if 0 < amount <= self._quantity:
            self._quantity -= amount
            return True
        return False

### 2. Abstraction
- Abstraction hides the complex internal details of inventory operations, exposing only simple interfaces for the user or main program to interact with. A Sari-Sari Store or Inventory class can provide clean, high-level methods like "checkout_cart()" or "generate_daily_report()". The user does not need to know how the system calculates totals, iterates through lists, or updates individual stock counts behind the scenes. This simplifies program interactions, reduces code complexity, and makes the system much easier to maintain and update.

class InventoryManager:
    def process_sale(self, product, quantity):
        # Hides stock check, calculation, and reporting details
        if product.sell(quantity):
            print(f"Sold {quantity} unit(s) of {product.name}.")
        else:
            print("Transaction failed: Insufficient stock.")

### 3. Inheritance
- Inheritance allows specialized product types to derive attributes and behaviors from a general "Product" base class without duplicating code. For example, a base "Product" class containing standard properties like name, price, and quantity can be extended by subclasses like "PerishableProduct" (adding an expiration_date attribute) or "BeverageProduct" (adding a is_chilled attribute). This reduces code repetition, promotes reuse, and makes adding new categories of sari-sari store items straightforward.

class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date  # Subclass-specific attribute

### 4. Polymorphism
- Polymorphism enables different product types to respond to the same method call in ways specific to their behavior. For instance, both "StandardProduct" and "DiscountedProduct" can implement a "get_total_price(quantity)" method, but "DiscountedProduct" applies a promotional discount calculation. The inventory system can iterate through a list of mixed products and calculate prices uniformly using "product.get_total_price()". This enhances program flexibility, allowing developers to add new pricing rules or product behavior without altering existing checkout logic.

class DiscountedProduct(Product):
    def __init__(self, name, price, quantity, discount_rate):
        super().__init__(name, price, quantity)
        self.discount_rate = discount_rate

    def calculate_price(self, amount):
        # Custom implementation for discounted items
        base_price = self.price * amount
        return base_price * (1 - self.discount_rate)

## Reflection
Among the four pillars, Encapsulation would be the most useful for improving a sari-sari store inventory system. In a store setting, maintaining accurate stock counts and valid pricing is critical to preventing financial losses and inventory discrepancies. By restricting direct access to product data and requiring all stock changes to pass through validated methods, encapsulation prevents human error such as setting negative stock or manually altering prices incorrectly. This ensures that the system's data remains consistent, trustworthy, and organized as the store grows.