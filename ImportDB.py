import pyodbc
import csv

SERVER = 'nmct-cloud1-labo2.database.windows.net'
DATABASE = 'JohannesDB'
USERNAME = 'student'
PASSWORD = '-Azerty2016'
DRIVER = '{ODBC Driver 13 for SQL Server}'


def create_table():
    create_table = """DROP TABLE IF EXISTS Websites;
                  CREATE TABLE Websites(
                  WebsiteID int IDENTITY(1,1) PRIMARY KEY,
                  GlobalRankID int NOT NULL,
                  TldRank int NOT NULL,
                  Domain nvarchar(150) NOT NULL,
                  TLD nvarchar(150)NOT NULL,
                  RefSubNets int NOT NULL,
                  RefIps int NOT NULL,
                  IDN_Domain nvarchar(150) NOT NULL,
                  IDN_TLD nvarchar(150) NOT NULL,
                  PrevGlobalRank int NOT NULL,
                  PrevTldRank int NOT NULL,
                  PrevRefSubnets int NOT NULL,
                  PrevRefIps int NOT NULL
                  );"""
    connection_string = 'DRIVER=' + DRIVER + ';PORT=1433;SERVER=' + SERVER + ';PORT1443;DATABASE=' + DATABASE + ';UID=' + USERNAME + ';PWD=' + PASSWORD
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    result = cursor.execute(create_table)
    cursor.commit()


def ingelezen_db(bestandsnaam):
    teller = 0
    try:
        fo = open(bestandsnaam)
        lijn = fo.readline()
        lijn = fo.readline()
        while lijn != "":
            lijn = lijn.rstrip('\n')
            delen = lijn.split(";")
            try:
                lokaal = Jeugdterrein(delen[1], delen[2], delen[5], delen[3], delen[6])
                jeugdlokalen.append(lokaal)
            except:
                teller += 1
            lijn = fo.readline()
        fo.close()
    except FileNotFoundError as fnf:
        print("Foutmelding: bestand niet gevonden.")
    print("Er werden " + str(teller) + " lijnen niet verwerkt.")
    return jeugdlokalen
