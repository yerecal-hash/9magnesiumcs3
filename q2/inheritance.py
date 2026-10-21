# Parent Class: Publication
class Publication:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    # Getters
    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    # Setters
    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

    # Display Information Method
    def display_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")


# Child Class: Book
class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.set_number_of_pages(number_of_pages)

    # Getter
    def get_number_of_pages(self):
        return self._number_of_pages

    # Setter with data validation
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self._number_of_pages = number_of_pages
        else:
            print("Number of pages must be positive.")


# Child Class: Magazine
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.set_issue_number(issue_number)

    # Getter
    def get_issue_number(self):
        return self._issue_number

    # Setter with data validation (optional consistency)
    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self._issue_number = issue_number
        else:
            print("Issue number must be positive.")


# Sample Object Creation and Testing

# Creating objects
pub1 = Publication("Journal of Experimental Psychology", "Ratcliff, R. & Van Dongen, H.")
pub2 = Publication("Python Programming Basics", "John Smith")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Clean Code", "Robert C. Martin", 464)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Time Magazine", "Staff Writers", 150)

# Printing Information
print("Publication Information:")
pub1.display_info()
print()

print("Book Information:")
book1.set_number_of_pages(-310)  # Testing invalid value validation
book1.display_info()
print(book1.get_number_of_pages())
print()

print("Magazine Information:")
mag1.display_info()
print(f"Issue number: {mag1.get_issue_number()}")