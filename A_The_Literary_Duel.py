n = int(input())
books = list(map(int, input().split()))

def determine_winner(n, books):
    Hermione_books = 0
    Harry_books = 0


    for i in range(n):
        if i % 2 == 0:
            Hermione_books += max(books[0], books[-1])
            if books[0] > books[-1]:
                books.pop(0)
            else:
                books.pop(-1)
        else:
            Harry_books += max(books[0], books[-1])
            if books[0] > books[-1]:
                books.pop(0)
            else:
                books.pop(-1)

    return Hermione_books, Harry_books

Hermione_books, Harry_books = determine_winner(n, books)
print(Hermione_books, Harry_books)

