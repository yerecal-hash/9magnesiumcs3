# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Famous Fragrances
Description: Represents a specific fragrance bottle, storing its scent profile, brand, size, and projection details.
## New Related Class
Class: Collector
Description: Represents a person who collects fragrances, keeping track of their name and the physical fragrances they own.
## Association
Relationship: owns
Explanation: A Collector owns and manages a collection of various FamousFragrance objects.
## Multiplicity
Multiplicity: 1 : 0..* (One-to-Many)
Explanation: One Collector can own zero or many (multiple) FamousFragrance objects, making it appropriate to store them as a collection.
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
The association is an "owns" or "manages" relationship. In my system, a "Collector" object acts as the owner of multiple "FamousFragrance" objects, mimicking a real person building a fragrance collection.
### What multiplicity did you choose and why?
I chose a one-to-many (1 : 0..*) multiplicity. This is appropriate because a single fragrance collector can own zero, one, or multiple fragrances at any given time, perfectly reflecting real-world habits.
### How did you implement the relationship in Python?
I implemented the relationship by creating a list attribute called self.collection inside the Collector class. This list is populated using the add_fragrance() method, which appends actual FamousFragrance object references into it.
### Why did you store an object reference instead of copying its data?
Storing an object reference allows the Collector to access the live state of the fragrance. For example, if I call spray(10) on a fragrance, its __size attribute dynamically decreases. If I only copied string data (like the name), I wouldn't be able to track the updated liquid volume or call its specific methods.
### If your relationship uses many, why is a list appropriate?
A Python list is the ideal data structure because it can dynamically hold multiple items in an ordered sequence. The list actually contains memory references to the independent FamousFragrance instances, allowing me to loop through the collection and access each object's unique attributes and methods.