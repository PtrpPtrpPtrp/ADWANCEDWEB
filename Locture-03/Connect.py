from re import error
import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                  password="PEMgvr72410",
                                  host="http://adv-mint.app.ruk-com.cloud/",
                                  port="11160",
                                  database="CloudDB")
    cursor = connection.cursor()

    print(connection.get_dsn_parameter(),"\n")

    cursor.execute("Select Version();")
    record = cursor.fetchone()
    print("You are connect to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error While connecting to PostgreSQL",error)
finally:
    
    if(connection):
        cursor.close()
        connection.close()
        print("ProgreSQL connection is close")

