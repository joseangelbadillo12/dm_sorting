#MySQL Database Connection
import mysql.connector
from mysql.connector import errorcode
import json 
from decimal import *


#Connection Credentials
try:
    conn = mysql.connector.connect(user = "root", 
                                    password = "", 
                                    host ="localhost",
                                    database = "endutih")
#To handle errors
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something went wrong :(")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database does not exist :(")
    else:
        print(err)

#Query the database information
query = "SELECT `id_indicador`,`indicador`,`año`,`valor`,`unidad_medida` FROM `endutihhh` WHERE `id_indicador`='6206972692' UNION SELECT `id_indicador`,`indicador`,`año`,`valor`,`unidad_medida` FROM `endutihhh` WHERE `id_indicador`='6206972695'"


cursor = conn.cursor()
cursor.execute(query)

desc = cursor.description
column_names = [col[0] for col in desc]
data = [dict(zip(column_names, row))
        for row in cursor.fetchall()]

json_object = json.dumps(data, indent=9)

# Writing to sample.json
with open("quick sort.json", "w") as outfile:
    outfile.write(json_object)

#Close database connection
cursor.close()
conn.close()