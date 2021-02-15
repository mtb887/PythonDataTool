#The main class will put everything together. this will loop through all the set credentials
# and perform all the necessary ETL from all the relevant databases.

# We will import all the necessary variables from all the local foles so that the main classs can process everything.

from connections import DataWarehouse, Mssql_config, Mysql_config, firebird_config
from SqlQueries import MSsqlQueries, MySqlQueries, FireBirdQueries
from variables import *
# The method below will also be imported into the main as it is already created on it
#own file, makes everything nice and coordinated.
from etl import ETLProcess2

def main():
  print('The ETL Process has started, you will be notified once done!!')
	
  # Establish a connection the target database, which is the datawarehouse database
  TargetConnection = pyodbc.connect(DataWarehouse)
	
  # lets now loop through the credentials with simple try-except loops so that the correct connections are made to the correct databases

  # Connection to MySql configuration
  for config in Mssql_config: 
    try:
      print("Database Loading: " + config['database'])
      ETLProcess2(MysqlQueries, TargetConnection, config, 'mysql')
    except Exception as error:
      print("ETL Processes for {} has error".format(config['database']))
      print('With error: {}'.format(error))
      continue
	
  # Connection to MSsql configuration
  for config in MSsql_config: 
    try:
      print("Database Loading: " + config['database'])
      ETLProcess2(MSsqlQueries, TargetConnection, config, 'MSsql')
    except Exception as error:
      print("ETL Processes for {} has error".format(config['database']))
      print('With error: {}'.format(error))
      continue

  # Connection to FireBird  database connection
  for config in Firebird_config: 
    try:
      print("Database Loading: " + config['database'])
      ETLProcess2(FireBirdQueries, TargetConnection, config, 'firebird')
    except Exception as error:
      print("ETL Processes for {} has error".format(config['database']))
      print('With error: {}'.format(error))
	
  TargetConnection.close()
#Well if you dont know what this does then you should not be reasing this
if __name__ == "__main__":
  main()
#Thats all folks, a python pipeline reading from multiple sources into a warehouse