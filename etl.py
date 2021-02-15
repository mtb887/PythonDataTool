# Import these python modules so that the code works, this is very important
import mysql.connector
import pyodbc
import fdb
# we will import the datawarehouse database name from the localy created variables file

from variables import datawarehouse

#This is where most of the heavy lifting will be done, the instances from other files will
#be called and everything will be processed here. Mess this up and this whole thing would have been a waste of time

def ETLProcess1(RunQuery, SourceConnection, TargetConnection):
  # Extract data from the source databases using the sql queries that have already been defined
  SourceCursor = SourceConnection.cursor()
  SourceCursor.execute(RunQuery.ExtractionQuery)
  SourcedData = SourceCursor.fetchall()
  SourceCursor.close()

  # This is the loop that we will use to load the data into the data warehouse database.

  if SourceData:
    TargetCursor = TargetConnection.cursor()
    TargetCursor.execute("USE the database {}".format(datawarehouse))
    TargetCursor.executemany(RunQuery.LoadingQuery, SourceData)
    print('The data has been successfully loaded into the datawarehouse.')
    TargetCursor.close()
  else:
    print('There is no data to be imported, Please verify your data sources')

def ETLProcess2(ProcessQueries, TargetConnection, SourceDbConfiguration, DatabasePlatform):
  # A source of data is establised, and depending on the source that is required, the corresponding 
  #sql connection will be established and the correct set of queries run.
  if DatabasePlatform == 'mysql':
    SourceConnection = mysql.connector.connect(Mysql_config)
  elif DatabasePlatform == 'sqlserver':
    SourceConnection = pyodbc.connect(Mssql_config)
  elif DatabasePlatform == 'firebird':
    SourceConnection = fdb.connect(firebird_config)
  else:
    return 'The platform is currently not supported, but soon, it will...watch the space'
  
  # This look will initiate the above steps untill there is no data to be imported.
  for RunQuery in ProcessQueriess:
    ETLProcess1(RunQuery, SourceConnection, TargetConnection)
    
  # close the source database connection
  SourceConnection.close()