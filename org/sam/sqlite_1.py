#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Mar 14, 2018

Course work: 

@author: raja

Source:
    http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
    http://www.sqlitetutorial.net/sqlite-python/insert/
    
    https://docs.python.org/3/library/sqlite3.html
    https://stackoverflow.com/questions/7831371/is-there-a-way-to-get-a-list-of-column-names-in-sqlite
    https://stackoverflow.com/questions/228912/sqlite-parameter-substitution-problem
    
    Create table
        http://www.sqlitetutorial.net/sqlite-python/create-tables/
    
    Date format readable:
        https://stackoverflow.com/questions/2158347/how-do-i-turn-a-python-datetime-into-a-string-with-readable-format-date
        
    Geo Location
        http://en.mygeoposition.com/        
    
    DB:
    tasks:
        id, name, priority
    projects:
        id, name, begin_date, end_date
'''

# Import necessary modules
import sqlite3
from sqlite3 import Error
from random import randint
from datetime import datetime 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        
        print('table created')
    except Error as e:
        print(e)


def select_all_from_table(conn, table):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+table)
 
    rows = cur.fetchall()
    
    print('rows : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available');
 
    for row in rows:
        print(row) 
 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

def add_task(conn, task):
    """
    Create a new task into the projects table
    :param conn:
    :param task:
    :return: task id
    """
    sql = ''' INSERT INTO tasks(name, priority)
              VALUES(:name, :priority) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid        
        
def add_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name, begin_date, end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    
    
    
    return cur.lastrowid


def get_columns(conn, table):
    """
    Get All Columns     
    """
    cur = conn.cursor();
    cur = cur.execute('select * from '+table)
    names = list(map(lambda x: x[0], cur.description))
    
    print(names)
    

def get_random_city():
    words  = [
        'Chennai',
        'Bengaluru',
        'Cape Town',
        'Toronto',
        'Montreal',
        'six',
        ];
    
    return words[randint(0, len(words)-1)];    

def get_random_word():
    words  = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        ];
    
    return words[randint(0, len(words)-1)];

def get_dummy_task():
    task = {
            "id" : "2",
            "name" : get_random_word(),
            "priority" : randint(0, 9)
         }
    return task
 
def main():
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    
    
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
    
    with conn:
        
        #create_table(conn, sql_create_projects_table)
        
        '''
        #proj = {"name" : "yx", "begin_date" : "", "end_date" : ""}
        
        #get_columns(conn, 'tasks')
        #get_columns(conn, 'projects')  
        
        #print("1. Insert task : "+r_word)
        '''
        
        
        #result = add_task(conn, get_dummy_task())
        #print(result)      
        
        
        #r_word = str(get_random_word())
        #print("1. Insert task : "+r_word)        
                        
        
        #print("1. Query task by priority:")
        #select_task_by_priority(conn, 1)
        
        '''
 
        print("2. Query all tasks")
        select_all_tasks(conn)
        '''
        
        
        
        date1 = "{:%B %d, %Y}".format(datetime.now())
        date2 = "{:%B %d, %Y}".format(datetime.now())
        project2 = (get_random_word(), date1, date2)
        id = add_project(conn, project2)
        print('Newly created id  : '+str(id))     
           
        
        
        select_all_from_table(conn, 'projects')
 
 
if __name__ == '__main__':
    main()