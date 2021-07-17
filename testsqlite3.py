import sqlite3
a = 'Autor'
c = 'Citat'

def create_bd():
    db = sqlite3.connect('quotes.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS users(
    author TEXT,
    quote TEXT
    )""")
    db.commit()
    return db, sql

def get_bd(id=None):
    print(id)
    db, sql = create_bd()
    if not id:
        sql.execute('SELECT rowid, author, quote FROM users')
        return sql.fetchall()
    else:    
        sql.execute(f"SELECT rowid FROM users WHERE rowid = '{id}' ")
        if not sql.fetchone():
            print('Такая цитата не существует')
            return None                
        else:         
            sql.execute(f"SELECT rowid, author, quote FROM users WHERE rowid = '{id}'")
            return sql.fetchall()
        
    

    
def post_bd(inp_author, inp_quote):
    
    db, sql = create_bd() 
    sql.execute(f"SELECT quote FROM users WHERE quote = '{inp_quote}' ")
    if not sql.fetchone():
        sql.execute(f"INSERT INTO users VALUES ('{inp_author}', '{inp_quote}')")
        db.commit()
    else: 
        print('Такая цитата существует')

    sql.execute('SELECT * FROM users')
    
    return sql.fetchall()


def put_bd(inp_author, inp_quote, id):
    
    db, sql = create_bd()
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
    
    db, sql = create_bd()
    sql.execute(f"DELETE FROM users WHERE rowid = '{id}' ")
    db.commit()

#print(get_bd(input('Введите id для изменения ')))
#print(getid_bd())
#post_bd(input('Введите автора для реестрации '),input('Введите цитату для реестрации ' ))
# put_bd(a, c, input('Введите id для изменения '))
# delete_bd(input('Введите автора для удаления '))
# print(get_bd())