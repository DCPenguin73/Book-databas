import sqlite3
con = sqlite3.connect('books.db')

cur = con.cursor()

# create table
# cur.execute('''CREATE TABLE books
#                 (title, author, year, finished)''')
action = 1
while (action == 1) or (action == 2) or (action == 3) or (action == 4) or (action == 5):
    print()
    print('1-View list')
    print('2-Add book to list')
    print('3-Search for book in list')
    print('4-Edit entry in list')
    print('5-Delete book from list')
    print('6-Close list')
    action = int(input('Type number for action you want to do: '))
    print()
    if action == 1:
        for row in cur.execute('SELECT * FROM books'):
            print(row)
        print()

    elif action == 2:
        title = input('Title: ')
        author = input('Author: ')
        year = input('Published Year: ')
        finished = input('Read: ')
        print()
        book = [(title, author, year, finished)]
        # insert a row of data
        cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?)", book)
        # save (commit) the changes
        con.commit()
        print()

    elif action == 3:
        stitle = input('What book do you want to search for? ')
        stitle = (stitle,)
        cur.execute('SELECT * FROM books WHERE title=?', stitle)
        print(cur.fetchone())
        print()

    elif action == 4:
        etitle = input('What book entry do you want to edit? ')
        title = input('New Title: ')
        ntitle = (title, etitle)
        author = input('New Author: ')
        nauthor = (author, etitle)
        year = input('New Published Year: ')
        nyear = (year, etitle)
        finished = input('New Read: ')
        nfinished = (finished, etitle)

        # insert a row of data
        cur.execute("UPDATE books SET title=? WHERE title=?", ntitle)
        cur.execute("UPDATE books SET author=? WHERE title=?", nauthor)
        cur.execute("UPDATE books SET year=? WHERE title=?", nyear)
        cur.execute("UPDATE books SET finished=? WHERE title=?", nfinished)
        # save (commit) the changes
        con.commit()
        print()

    elif action == 5:
        dtitle = input('What book do you want to delete from the list? ')
        dtitle = (dtitle,)
        cur.execute('DELETE FROM books WHERE title=?', dtitle)
        con.commit()
        print()

con.close()