import mysql.connector
import pandas as pd
import curses
import time

# CONFIGURING CONNECTION TO MYSQL | ADD YOUR OWN CONFIG IN '' BELOW
config = {
    'host': '',
    'user': '',
    'password': '',
    'database': '',
    'table': ''
}

connection = mysql.connector.connect(
    host=config['host'],
    user=config['user'],
    password=config['password'],
    database=config['database']
)
cursor = connection.cursor()

# RETRIEVING TABLE COLUMN NAMES
query = f"SELECT * FROM {config['table']} LIMIT 0"
cursor.execute(query)
cursor.fetchall()
column_names = [desc[0] for desc in cursor.description]

cursor.close()

# RETRIEVE DATA & DISPLAY IT IN WINDOW
def fetch_and_display_data(stdscr, max_y, max_x, start_row):
    # Commit pending changes
    connection.commit()
    cursor = connection.cursor()

    # Retrieve table data
    query = f"SELECT * FROM {config['table']}"
    cursor.execute(query)

    # Store retrieved data in pandas DataFrame
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=column_names)

    cursor.close()
    stdscr.clear()

    # Show column names
    for idx, col in enumerate(df.columns):
        if idx * 15 + len(col) < max_x:
            stdscr.addstr(0, idx * 15, col[:15])

    for row_count, row in enumerate(range(start_row, len(df))):
        if row_count + 1 >= max_y:
            break
        for idx, value in enumerate(df.iloc[row]):
            if idx * 15 + len(str(value)) < max_x:
                stdscr.addstr(row_count + 1, idx * 15, str(value)[:15])

    stdscr.refresh()
    return len(df)

# MAIN FUNCTION
def main(stdscr):
    try:
        curses.curs_set(0)
        stdscr.nodelay(True) # Put the window in non-blocking mode

        # Get window dimensions
        max_y, max_x = stdscr.getmaxyx()
        start_row = 0
        data_length = fetch_and_display_data(stdscr, max_y, max_x, start_row)

        fetch_and_display_data(stdscr, max_y, max_x, start_row)

        while True:
            key = stdscr.getch()
            if key == curses.KEY_UP and start_row > 0:
                start_row -= 1
            elif key == curses.KEY_DOWN and start_row < data_length - max_y:
                start_row += 1
            elif key == ord('q') or key == ord('Q'):
                break
            elif key == curses.KEY_RESIZE:
                max_y, max_x = stdscr.getmaxyx()

            data_length = fetch_and_display_data(stdscr, max_y, max_x, start_row)

            fetch_and_display_data(stdscr, max_y, max_x, start_row)

            # Wait 0 second before refreshing again
            time.sleep(0)

    except KeyboardInterrupt:
        pass
    finally:
        connection.close()


if __name__ == '__main__':
    curses.wrapper(main)
