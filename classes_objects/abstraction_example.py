import sqlite3


class DataBaseOperations:

    def __init__(self, databasename):

        self.databasename = databasename

    def createDatabase(self):
        try:
            conn = sqlite3.connect(self.databasename)
        except ConnectionError:
            raise ConnectionError
        return conn

    def createTable(self, tablename, dictionaryOfcolumnNamesAndcolumnDatatypes):
        try:
            conn = self.createDatabase()
            c = conn.cursor()
            for key in dictionaryOfcolumnNamesAndcolumnDatatypes.keys():
                datatype = dictionaryOfcolumnNamesAndcolumnDatatypes[key]
                try:
                    conn.execute(
                        'ALTER TABLE {tableName} ADD COLUMN "{column_name}" {dataType}'.format(tableName=tablename,
                                                                                               column_name=key,
                                                                                               dataType=datatype))
                except:
                    conn.execute('CREATE TABLE {tableName} ({column_name} {dataType})'.format(tableName=tablename,
                                                                                              column_name=key,
                                                                                              dataType=datatype))
            print("Table {0} created in database {1}".format(tablename, self.databasename))
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
        except Exception as e:
            conn.rollback()
            self.closeDbConnection(conn)
            print("Connection to database closed!!")

            print("Exception occured: " + str(e))

    def insertIntoTable(self, tablename, listOfvaluesToInsert):
        try:
            conn = self.createDatabase()
            conn.execute(
                'INSERT INTO {tablename}  values ({values})'.format(tablename=tablename, values=(listOfvaluesToInsert)))
            conn.commit()
            print("Values Inserted Successfully!!!")
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
        except Exception as e:
            conn.rollback()
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
            print("Error occured: " + str(e))

        # self.closeDbconnection()

    def selectFromTable(self, tablename):

        try:
            conn = self.createDatabase()
            c = conn.cursor()
            c.execute("SELECT *  FROM {table}".format(table=tablename))
            print("values in table : ", c.fetchall())
            self.closeDbConnection(conn)
            print("Connection to database closed!!")

        except Exception as e:
            self.closeDbConnection(conn)
            print("Connection to database closed!!")
            print("Error occured: " + str(e))

    def closeDbConnection(self, connection):

        connection.close()


class StudentMarks(DataBaseOperations):  # inheriting the DatabaseOperation class

    def __init__(self, ID, RollNumber, Marks):
        self.id = ID
        self.RollNum = RollNumber
        self.Marks = Marks
        self.databasename = "StudentDetails"

student1 = StudentMarks(23,34,76)
student1.createDatabase()