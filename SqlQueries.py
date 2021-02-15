# So, here is the thing right, since all these sources use different syntax, they will run run seperately, see below for the magc
#So we will start by creating the queries that will be used to extract the data from the source and load into the destination database, which is our data warehouse

MSsqlExtract1 = ('''
  SELECT MSsql_column_1, MSsql_column_2, MSsql_column_3
  FROM MsSQLTable1
''')

MSsqlInsert1 = ('''
  INSERT INTO table (column_1, column_2, column_3)
  VALUES (?, ?, ?)  
''')

MSsqlExtract2 = ('''
  SELECT MSsql_column_1, MSsql_column_2, MSsql_column_3
  FROM MsSqlTable2
''')

MSsqlInsert2 = ('''
  INSERT INTO table (column_1, column_2, column_3)
  VALUES (?, ?, ?)  
''')

MySqlExctract1 = ('''
  SELECT mysql_column_1, mysql_column_2, mysql_column_3
  FROM mysql_table
''')

MySqlInsert1 = ('''
  INSERT INTO table (column_1, column_2, column_3)
  VALUES (?, ?, ?)  
''')

MySqlExctract2 = ('''
  SELECT mysql_column_1, mysql_column_2, mysql_column_3
  FROM mysql_table
''')

MySqlInsert2 = ('''
  INSERT INTO table (column_1, column_2, column_3)
  VALUES (?, ?, ?)  
''')

MySqlExtract3 = ('''
  SELECT mysql_column_1, mysql_column_2, mysql_column_3
  FROM mysql_table
''')

MySqlInsert3 = ('''
  INSERT INTO table (column_1, column_2, column_3)
  VALUES (?, ?, ?)  
''')

FireBirdExtract1 = ('''
  SELECT fb_column_1, fb_column_2, fb_column_3
  FROM FireBirdTable1;
''')

FireBirdInsert1 = ('''
  INSERT INTO table (column_1, column_2, column_3)
  VALUES (?, ?, ?)  
''')

FirebirdExtract2 = ('''
  SELECT fb_column_1, fb_column_2, fb_column_3
  FROM FireBirdTable2;
''')

FirebirdInsert2 = ('''
  INSERT INTO table_2 (column_1, column_2, column_3)
  VALUES (?, ?, ?)  
''')

# So we will export the above queries into a python class, just to make everything fancy. so that it can be automated, or atleast run at a press of a button whenever n
#essesary 
class SqlQueries:
  def __init__(self, ExtractionQuery, LoadingQuery):
    self.ExtractionQuery = ExtractionQuery
    self.LoadingQuery = LoadingQuery
    
# create instances for the SqlQueries class, these will be the instances that would be fired up when the class runs.

MSsqlQuery1 = SqlQueries(MSsqlExtract1, MSsqlInsert1)
MSsqlQuery2 = SqlQueries(MSsqlExtract2, MSsqlInsert2)
MySqlQuery1 = SqlQueries(MySqlExctract1, MySqlInsert1)
MySQlQuery2 = SqlQueries(MySqlExctract2, MySqlInsert2)
MySqlQuery3 = SqlQueries(MySqlExctract3, MySqlInsert3)
FireBirdQuery1 = SqlQueries(FirebirdExtract1, FireBirdInsert1)
FireBirdQuery2 = SqlQueries(FirebirdExtract2, FirebirdInsert2)

# The above instances will be stored in a list(array) for iteration, and no im not going to explain iteration, please figure it out. Just know that iteration is important 
# for making thing easier to work with.

MSsqlQueries = [MSsqlQuery1, MSsqlQuery2]
MySqlQueries = [MySqlQuery1, MySqlQuery2, MySqlQuery3]
FireBirdQueries = [FireBirdQuery1, FireBirdQuery2]