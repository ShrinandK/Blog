# function to create connection
def createConnection(dbname):
    # this executes when no database has been created
    if dbname == 'default':
        con = psycopg2.connect(user="postgres",
                               password="your_password",
                               host="localhost",
                               port="5432")
        # this is required for auto committing changes
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    # this executes when database has been created
    else:
        con = psycopg2.connect(user="postgres",
                               database=dbname,
                               password="your_password",
                               host="localhost",
                               port="5432")
    return con
	
# function to destroy connection
def destroyConnection(con):
    try:
        cursor = con.cursor()
        cursor.close()
        con.close()
        print("PostgreSQL connection is closed")
    except :
        pass	
		
		
# function to create database and insert data
def createData(processedData):
    # creates connection to databse with some default settings
    con = createConnection('default')
    cursor = con.cursor()
    # database name and code to create table in the database
    name_Database = "gamedata"
    tableCreation = "CREATE TABLE gamewarehouse (id serial PRIMARY KEY,teams varchar(200),year integer,\
    wins integer,losses integer)"
    
    try:
        # this checks if database is available or not
        checkDatabase = "SELECT datname FROM pg_catalog.pg_database WHERE datname='gamedata';"
        cursor.execute(checkDatabase)
        result = cursor.fetchone()
        # this will create database if not available
        if not result:
            # first create database
            sqlCreateDatabase = "create database "+name_Database+";"
            cursor.execute(sqlCreateDatabase)
            destroyConnection(con)
            
            # second create table
            con = createConnection(name_Database)            
            cursor = con.cursor()
            cursor.execute(tableCreation)
            con.commit() 
            destroyConnection(con)
            
            # this is required to insert pandas dataframe directly into database
            engine = create_engine('postgresql+psycopg2://postgres:your_password@localhost:5432/gamedata')
            processedData.to_sql('gamewarehouse', engine, if_exists='append',index=False)            
            engine.dispose()
            print('Database created successfully!');           
            
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (con):
            destroyConnection(con)
			
def readData():
    # connect to database
    name_Database = "gamedata" 
    con = createConnection(name_Database) 
    cursor = con.cursor()    
         
    # check if database is available
    checkDatabase = "SELECT datname FROM pg_catalog.pg_database WHERE datname='gamedata';"
    cursor.execute(checkDatabase)
    result = cursor.fetchone()
    if result:
        # select all data from table and give in dataframe
        selectQuery = "SELECT * from gamewarehouse"
        allRecords = pandas.read_sql_query(selectQuery,con)
        if (con):
            destroyConnection(con)
    return allRecords	

def updateData(setColumnName,setColumnData,whereColumnName,whereColumnData):
    name_Database = "gamedata" 
    con = createConnection(name_Database) 
    cursor = con.cursor()
    sqlQuery =  (f"UPDATE gamewarehouse SET {setColumnName} = {setColumnData} "
                 f"WHERE {whereColumnName} = {whereColumnData};")
    cursor.execute(sqlQuery)
    con.commit()
    if (con):
        destroyConnection(con)	
		
		
def deleteData(whereColumnName,whereColumnData):
    name_Database = "gamedata" 
    con = createConnection(name_Database) 
    cursor = con.cursor()
    sqlQuery =  (f"DELETE FROM gamewarehouse WHERE {whereColumnName} = {whereColumnData};")
    cursor.execute(sqlQuery)
    con.commit()
    if (con):
        destroyConnection(con)		
		
		
# some preprocessing		
dataToLoad = getData()
dataToLoad = dataToLoad.rename(columns={'Team Name':'Teams'})
dataToLoad.columns = dataToLoad.columns.str.lower()
# Create
createData(dataToLoad)
# Read
getDataFrame = readData()
# Update
updateData('wins',100,'id',50)
# Delete
deleteData('id',1)	