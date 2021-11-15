"""Personal DataBase."""
import sqlite3

def create_DB():
    """Create DB."""
    con = sqlite3.connect("data.db")
    c= con.cursor()
    c.execute("""CREATE TABLE users(
            first text,
            last text,
            email text  
            )""")
    print("DB Created...")
    con.commit()
    con.close()


def show_all():
    """Show all what's stored in DB."""
    con = sqlite3.connect("data.db")
    c= con.cursor()
    c.execute("SELECT rowid, * FROM users LIMIT 20")
    all_documents = c.fetchall()
    for data in all_documents:
        print(data)
    con.commit()
    con.close()

   
def search_specific(email):
    """Search Specific Thingin DB.""" 
    con = sqlite3.connect("data.db")
    c= con.cursor()
    c.execute("""SELECT * FROM users WHERE email= '?'
                    """,email)
    all_documents = c.fetchone()
    print(all_documents)
    con.commit()
    con.close()


def add_data(first,last,email):
    """ADD data to DB."""
    con = sqlite3.connect("data.db")
    c= con.cursor()
    c.execute("INSERT INTO users VALUES(?,?,?)",(first,last,email))
    con.commit()
    con.close()

def remove_data(first):
    con = sqlite3.connect("data.db")
    c= con.cursor()
    show_all()
    c.execute("DELETE FROM users WHERE first =(?)",first)
    print(f"Data of {first} has been Removed...")
    con.commit()
    con.close()
    
def remove(id):
    con = sqlite3.connect("data.db")
    c= con.cursor()
    c.execute("DELETE FROM users WHERE rowid =(?)",id)
    print(f"Data of {id} has been Removed...")
    con.commit()
    con.close()