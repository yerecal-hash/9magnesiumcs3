# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
In Part III, the fragrance management system comprised two core classes: FamousFragrance (representing the perfume bottles itselves) and Collector (representing a user holding a collection via an Aggregation relationship).   
## Inheritance Relationship
Parent: FamousFragrance
Child: LimitedEditionFragrance
Explanation: LimitedEditionFragrance IS-A FamousFragrance. It inherits general attributes like name, brand, _projection, and __size; and also inheriting its methods spray(), and smell(); while extending functionality with batch tracking (batch_number, bottle_number, total_produced) and authentication (verify_authenticity()).   
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship:Composition
Whole Class: FamousFragrance
Part Class: Atomizer
Explanation: An Atomizer instance is directly initialized inside FamousFragrance.__init__(). The atomizer is physically built into the bottle and cannot exist independently.
Bonus Relationship: Dependency
Using Class: Collector
Used Class: ScentTester
Explanation: Collector temporarily accepts a ScentTester instance as an argument inside test_fragrance_sample() to test scent notes, without storing ownership of the paper strip.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)
## Reflection
Answers:
1.LimitedEditionFragrance was derived from FamousFragrance because a limited edition perfume is basically just a special version/special fragrance bottle. It shares core traits such as brand, name, and scent projection, while extending baseline functionality with batch registration numbers and authenticity verification methods.
2.Inheritance eliminated the need to re-declare name, brand, _projection, and __size in the child class. By calling super().__init__(), parent attribute assignment logic is reused, and standard methods like spray() and smell() were inherited directly without repeating code.
3.The relationship between FamousFragrance and Atomizer is Composition because each bottle creates its own Atomizer upon "manifestation". The atomizer is an important component of the bottle and cannot exist independently; if the bottle object is destroyed, its atomizer is destroyed with it.
4.The basic Association in Part III represented a generic linkage where Collector owned instances of FamousFragrance. The advanced relationships enforce structural boundaries: Composition establishes tight lifecycle dependency, while Dependency represents a temporary "USES-A" interaction where Collector receives ScentTester as a parameter without storing it permanently.
5.The design adheres to DRY by centralizing shared perfume characteristics in FamousFragrance, preventing redundant attribute definitions in specialized child classes. Furthermore, liquid consumption calculations are delegated to Atomizer to prevent repetitive math, and super().get_details() reuses parent string formatting.