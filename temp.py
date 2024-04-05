import os, glob
import pandas as pd
import psycopg2

def squeeze(x):
    return x['0']

if __name__ == '__main__':
    root_dir = r'D:\ITU\Semester 2\Big Data\Assignments\Assignment 2\Assignment 2\data\youtube_data'
    json_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))

    cols = ['youtuber_id', 'youtuber_name', 'youtuber_location', 'youtuber_latitude', 'youtuber_longitude']

    df = pd.read_json(json_files[0], lines=True)

    rows = []
    for i in range(len(json_files)):
        df = pd.read_json(json_files[i], lines=True)
        row = df.iloc[0][cols].apply(squeeze)
        row.fillna(0, inplace=True)
        rows.append(tuple(row.values))
    
    print(rows[0])

    # cols = ['video_id', 'video_id', 'youtuber_id', 'year', 'duration']
    
    # rows = []
    # for i in range(len(json_files)):
    #     df = pd.read_json(json_files[i], lines=True)
    #     row = df.iloc[0][cols].apply(squeeze)
    #     row.fillna(0, inplace=True)
    #     rows.append(tuple(row.values))



    # Establish a connection to your PostgreSQL database
    conn = psycopg2.connect(
        dbname="youtubedb",
        user="postgres",
        password="paybox",
        host="localhost",
        port="5432"
    )

    # Create a cursor object
    cur = conn.cursor()


    # Define your insert statement string
    insert_statement = """
        INSERT INTO YOUTUBERS_DIM
        (YOUTUBER_ID, NAME, LOCATION, LATITUDE, LONGITUDE)
        VALUES
        (%s, %s, %s, %s, %s)
    """

    # Execute the insert statement for each tuple in the data list
    cur.executemany(insert_statement, rows)

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()
