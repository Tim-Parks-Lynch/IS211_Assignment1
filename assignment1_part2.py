
class Book:
    def __init__(self, author, title):
        """
        Constructor of Book class
        :param author: The author of the book
        :param title: The title of the book
        """

        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title} written by {self.author}")


if __name__ == "__main__":
    book1 = Book("John Steinbeck", "Of Mice and Men")
    book2 = Book("Harper Lee", "To Kill a Mockinbird")

    book1.display()
    book2.display()
