# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'music.erd.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice =''
while menu_choice !='z':
    menu_choice = input('Welcome to the Music database\n\b'
                        'Type the letter for the information you want:\n'
                        'A: All the music database\n'
                        'B: R&B music\n'
                        'C: Music published after year 2000\n'
                        'D: Music from latest to oldest\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('all data(2)')
    if menu_choice == 'B':
        print_query('r&b')
    if menu_choice == 'C':
        print_query('after y2000')
    if menu_choice == 'D':
        print_query('latest to oldest')
    
    
    