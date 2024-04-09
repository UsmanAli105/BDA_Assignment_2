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
(
    VIDEOPLAY_ID SERIAL PRIMARY KEY,
    START_TIME   INTEGER,
    USER_ID      INTEGER,
    LEVEL        VARCHAR,
    VIDEO_ID     INTEGER,
    YOUTUBER_ID  INTEGER,
    SESSION_ID   INTEGER,
    LOCATION     VARCHAR,
    USER_AGENT   VARCHAR,
    FOREIGN KEY (USER_ID) REFERENCES USERS_DIM (ID_ENTITY),
    FOREIGN KEY (VIDEO_ID) REFERENCES VIDEOS_DIM (ID_ENTITY),
    FOREIGN KEY (START_TIME) REFERENCES TIME_DIM (ID_ENTITY),
    FOREIGN KEY (YOUTUBER_ID) REFERENCES YOUTUBERS_DIM (ID_ENTITY)
)
""")

Users_table_create = ("""
CREATE TABLE IF NOT EXISTS
    USERS_DIM
(
    ID_ENTITY  SERIAL,
    USER_ID    VARCHAR,
    FIRST_NAME VARCHAR,
    LAST_NAME  VARCHAR,
    GENDER     VARCHAR,
    LEVEL      VARCHAR,
    PRIMARY KEY (ID_ENTITY)
)
""")

Videos_table_create = ("""
CREATE TABLE IF NOT EXISTS
    VIDEOS_DIM
(
    ID_ENTITY   SERIAL,
    VIDEO_ID    VARCHAR,
    TITLE       VARCHAR,
    YEAR        INT,
    DURATION    NUMERIC,
    PRIMARY KEY (ID_ENTITY)
)
""")


Youtubers_table_create = ("""
CREATE TABLE IF NOT EXISTS
    YOUTUBERS_DIM
(
    ID_ENTITY   SERIAL,
    YOUTUBER_ID VARCHAR,
    NAME        VARCHAR,
    LOCATION    VARCHAR,
    LATITUDE    NUMERIC,
    LONGITUDE   NUMERIC,
    PRIMARY KEY (ID_ENTITY)
)
""")

Time_table_create = ("""
CREATE TABLE IF NOT EXISTS
    TIME_DIM
(
    ID_ENTITY  SERIAL,
    START_TIME TIME,
    HOUR       INT,
    DAY        INT,
    WEEK       INT,
    MONTH      INT,
    YEAR       INT,
    WEEKDAY    VARCHAR,
    PRIMARY KEY (ID_ENTITY)
)
""")

# INSERT RECORDS
# Write queries to insert record to each table, please don't change variable names, you can refer to star schema table
# You should write respective queries against each varibale

Videoplay_table_insert = ("""
INSERT INTO VIDEOPLAY_FACT (START_TIME, USER_ID, LEVEL, VIDEO_ID, YOUTUBER_ID, SESSION_ID, LOCATION, USER_AGENT)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

Users_table_insert = ("""
INSERT INTO USERS_DIM (USER_ID, FIRST_NAME, LAST_NAME, GENDER, LEVEL)
VALUES (%s, %s, %s, %s, %s)
""")

Videos_table_insert = ("""
INSERT INTO VIDEOS_DIM (VIDEO_ID, TITLE, YEAR, DURATION)
VALUES (%s, %s, %s, %s)
""")

Youtubers_table_insert = ("""
INSERT INTO YOUTUBERS_DIM (YOUTUBER_ID, NAME, LOCATION, LATITUDE, LONGITUDE)
VALUES (%s, %s, %s, %s, %s)
""")


Time_table_insert = ("""
INSERT INTO TIME_DIM (START_TIME, HOUR, DAY, WEEK, MONTH, YEAR, WEEKDAY)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# QUERY LISTS

create_table_queries = [Users_table_create, Time_table_create, Youtubers_table_create, Videos_table_create, Videoplay_table_create]
drop_table_queries = [Videoplay_table_drop, Users_table_drop, Videos_table_drop, Youtubers_table_drop, Time_table_drop]
