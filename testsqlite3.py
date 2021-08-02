import sqlite3
a = 'author'
c = 'Citat'


def create_bd() -> tuple:
    db_author = sqlite3.connect('quotes.db')
    cur = db_author.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS authors(
        AuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        age INTEGER);
    """)
    db_author.commit()

    db = sqlite3.connect('quotes.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS users (
        QuotesID INTEGER PRIMARY KEY AUTOINCREMENT,
        quote TEXT,
        AuthorID int,        
        FOREIGN KEY (AuthorID) REFERENCES authors(AuthorID));    
        """)
    db.commit()
    return db, sql, db_author, cur


def get_bd():
    _, sql, _, cur = create_bd()
    sql.execute('SELECT rowid, author, quote FROM users')
    
    return sql.fetchall()


def post_bd(inp_author, inp_quote) -> int:
    
    db, sql, db_author, cur = create_bd()
    sql.execute(f"SELECT quote FROM users WHERE quote = '{inp_quote}' ")
    if not sql.fetchone():
        sql.execute(f"INSERT INTO users(AuthorID, quote)  VALUES ('{inp_author}', '{inp_quote}')")
        db.commit()
    else: 
        print('Такая цитата существует')

    sql.execute('SELECT * FROM users')
    
    return sql.fetchall()


def put_bd(inp_author, inp_quote, id):
    
    db, sql, db_author, cur = create_bd()
    print(inp_author,inp_quote)
    sql.execute(f"SELECT quote FROM users WHERE rowid = '{id}' ")
    if not sql.fetchone():
        print('Такая цитата не существует')                
    else:         
        sql.execute(f"UPDATE users SET quote = ('{inp_quote}'), author = ('{inp_author}') WHERE rowid = '{id}' ")
        db.commit()
        print('Цитата изменина')

    sql.execute('SELECT * FROM users')
    
    return sql.fetchall()


def delete_bd(id):
    
    db, sql, db_author, cur = create_bd()
    sql.execute(f"DELETE FROM users WHERE rowid = '{id}' ")
    db.commit()


def post_bd_authors(name, surname, age) -> int:
    db, sql, db_author, cur = create_bd()
    cur.execute(f"SELECT name FROM authors WHERE name = '{name}' ")
    if not cur.fetchone():
        cur.execute(f"INSERT INTO authors(name, surname, age) VALUES ('{name}', '{surname}', '{age}')")
        db_author.commit()
    else:
        print('Такая цитата существует')

    cur.execute('SELECT * FROM authors')

    return cur.fetchall()

print(create_bd())
print(post_bd_authors('lehfr', 'Klemberh', 23))
print(post_bd(5, 'Hjllhsdvhdvjsbhsdfvdbhf sdfhj s hgl'))
