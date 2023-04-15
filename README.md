# showMySQL.py


https://user-images.githubusercontent.com/35376790/232251467-27ee3d7b-fe26-4f98-b35c-40a3ae7f8681.mov


This Python script, named `showMySQL.py`, displays data from a MySQL table in a terminal with a scrolling interface. The script uses the `mysql.connector`, `pandas`, and `curses` libraries to interact with the MySQL database and display the data in a tabular format.

## Features

- Connect to a MySQL database
- Retrieve data from the selected table
- Display the data in a terminal with a scrolling interface
- Navigate the data using arrow keys (up/down)

## How to Use

1.  Ensure the required dependencies are installed (see Dependencies section below)
2.  Configure the connection information to your MySQL database in the `config` dictionary (host, user, password, database, table)
3.  Run the script with the command: `python showMySQL.py`
4.  Use the arrow keys (up/down) to navigate the displayed data
5.  Press 'q' or 'Q' to exit the program

## Dependencies

- python 3.6+
- mysql.connector
- pandas
- curses (pre-installed on Unix systems)

## requirements.txt

Install the dependencies using the `requirements.txt` file:
run: `pip install -r requirements.txt`

## Sample Output

The script displays the data from the selected MySQL table in a terminal, with column names at the top and data below. You can navigate the data using the arrow keys (up/down) and exit the program by pressing 'q' or 'Q'.
```
id   name         age  city
1    Alice        28   Bern
2    Bob          32   Geneva
3    Carol        45   Zürich
```
