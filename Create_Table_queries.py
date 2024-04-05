# DROP TABLES
# Write queries to drop each table, please don't change variable names,
# You should write respective queries against each varibale

Videoplay_table_drop = "DROP TABLE IF EXISTS VIDEOPLAY_FACT CASCADE"
Users_table_drop = "DROP TABLE IF EXISTS USERS_DIM"
Videos_table_drop = "DROP TABLE IF EXISTS VIDEOS_DIM"
Youtubers_table_drop = "DROP TABLE IF EXISTS YOUTUBERS_DIM"
Time_table_drop = "DROP TABLE IF EXISTS TIME_DIM"

# CREATE TABLES
# Write queries to create each table, please don't change variable names, you can refer to star schema table
# You should write respective queries against each varibale

Videoplay_table_create = ("""
CREATE TABLE IF NOT EXISTS
VIDEOPLAY_FACT
(VIDEOPLAY_ID SERIAL PRIMARY KEY,
START_TIME TIME REFERENCES TIME_DIM,
USER_ID NUMERIC REFERENCES USERS_DIM,
LEVEL VARCHAR,
VIDEO_ID VARCHAR REFERENCES VIDEOS_DIM,
YOUTUBER_ID VARCHAR REFERENCES YOUTUBERS_DIM,
SESSION_ID NUMERIC,
LOCATION VARCHAR,
USER_AGENT VARCHAR)
""")

commit = ("""
COMMIT;
""")

Users_table_create = ("""
CREATE TABLE IF NOT EXISTS
USERS_DIM
(USER_ID NUMERIC PRIMARY KEY,
FIRST_NAME VARCHAR,
LAST_NAME VARCHAR,
GENDER VARCHAR,
LEVEL VARCHAR)
""")

Videos_table_create = ("""
CREATE TABLE IF NOT EXISTS
VIDEOS_DIM
(VIDEO_ID VARCHAR PRIMARY KEY,
TITLE VARCHAR,
YOUTUBER_ID VARCHAR,
YEAR INT,
DURATION TIME)
""")


Youtubers_table_create = ("""
CREATE TABLE IF NOT EXISTS
YOUTUBERS_DIM
(YOUTUBER_ID VARCHAR PRIMARY KEY,
NAME VARCHAR,
LOCATION VARCHAR,
LATITUDE NUMERIC,
LONGITUDE NUMERIC)
""")

Time_table_create = ("""
CREATE TABLE IF NOT EXISTS
TIME_DIM
(START_TIME TIME PRIMARY KEY,
HOUR INT,
DAY INT,
WEEK INT,
MONTH INT,
YEAR INT,
WEEKDAY VARCHAR)
""")

# INSERT RECORDS
# Write queries to insert record to each table, please don't change variable names, you can refer to star schema table
# You should write respective queries against each varibale

Videoplay_table_insert = ("""
INSERT INTO VIDEOPLAY_FACT
(VIDEOPLAY_ID, START_TIME, USER_ID, LEVEL, VIDEO_ID, YOUTUBER_ID, SESSION_ID, LOCATION, USER_AGENT)
VALUES
(?, ?, ?, ?, ?, ?, ?, ?, ?)
""")

Users_table_insert = ("""

INSERT INTO USERS_DIM
(USER_ID, FIRST_NAME, LAST_NAME, GENDER, LEVEL)
VALUES
(?, ?, ?, ?, ?)

""")

Videos_table_insert = ("""
INSERT INTO VIDEOS_DIM
(VIDEO_ID, TITLE, YOUTUBER_ID, YEAR, DURATION)
VALUES
(?, ?, ?, ?, ?)
""")

Youtubers_table_insert = ("""
INSERT INTO YOUTUBERS_DIM
(YOUTUBER_ID, NAME, LOCATION, LATITUDE, LONGITUDE)
VALUES
(?, ?, ?, ?, ?)
""")


Time_table_insert = ("""
INSERT INTO TIME_DIM
(START_TIME, HOUR, DAY, WEEK, MONTH, YEAR, WEEKDAY)
VALUES
(?, ?, ?, ?, ?, ?, ?)
""")

# QUERY LISTS

create_table_queries = [Users_table_create, Time_table_create, Youtubers_table_create, Videos_table_create, Videoplay_table_create]
drop_table_queries = [Videoplay_table_drop, Users_table_drop, Videos_table_drop, Youtubers_table_drop, Time_table_drop]
