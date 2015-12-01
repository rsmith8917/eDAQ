import psycopg2

def saveValues ( devName , data ):
    "Saves the specified values to the database"

    errorCode = 0    
    
    conn = psycopg2.connect(database="eDAQ", user="postgres", password="n17s21o1", host="192.168.0.102", port=5432)
    cur  = conn.cursor()

    for dataPoint in data:
        channelName = dataPoint[0]
        timestamp   = dataPoint[1]
        value       = dataPoint[2]
        try:
            cur.execute("INSERT INTO " + channelName  + " VALUES (%s, %s);", (timestamp, value))
        except Exception as e:
            errorCode = 1
            # print str(e)
            # print str(timestamp)
            pass

    conn.commit()
    cur.close()
    conn.close()

    return errorCode

