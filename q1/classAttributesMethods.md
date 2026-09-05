# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
No major changes were needed from my original design.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| Name | String | Public | No point in smelling the fragrance if you won't know what it is |
| Brand | String | Public | How will you be able to find the exact fragrance without it's brand |
| Projection | String | Private | People won;t need to know exactly how strong it is, they can tell through their smell |
| Size | Int | Private | A fragrance is used for its scent, not to be measured |
## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
Because, in the words of pro programmers, they are just abstractions, things that are not needed to know, so they might as well not be shown.
### Which method changes the state of your object?
The spray method, it changes the "Size" of the object, if we assume one spray is minus 1ml, then every 20 sprays is minues 20ml from the "Size"(which is measured through ml).
### How did your two objects demonstrate that instances are independent?
It presented it by showing that when you use method 1(spray) on only fragrance1, then only fragrance1 will have it's size changed, not fragrance2; showing that both objects have their seperate independent memory locations.
### What is the difference between your class diagram and your object diagram?
The difference between them is that my class diagram just shows the class itself, the blueprint, the general; while my object diagram shows 2 object, which are both different from each other, the specifics.