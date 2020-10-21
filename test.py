import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "100.167.140.122",
    database = "ardit700_pmldatabase"
)

cursor = con.cursor()