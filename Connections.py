#import the Datawarehouse variable initialized in the variables file, it helps a great deal to seperate this things, cleans up the code quiet a bit, try it, and like cerebos, see how it runs.
from variables import DataWarehouse

# Configure the target database, this will be the warehouse and data will be pumped into this from different sources
DataWarehouse = {
  'Trusted_Connection': 'yes',
  'driver': '{SQL Server}',
  'server': 'Motebang_test_NMMU',
  'database': '{}'.format(),
  'user': '',
  'password': '',
  'autocommit': True,
}

# This is the connection configuration for the 1st data source, in this example we will use MSSQL
Mssql_config =
 [
  {
    'Trusted_Connection': 'yes',
    'driver': '{SQL Server}',
    'server': 'motebang_MSsql1',
    'database': 'whatever',
    'user': 'motebang',
    'password': 'wouldnt you want to know',
    'autocommit': True,
  }
  #This will be the seecond MSSQL database, which will serve as the second data source, we ill have two of these coz they are used alot, well atleast in my own opinion
  {
    'Trusted_Connection': 'yes',
    'driver': '{SQL Server}',
    'server': 'motebang_MSsql2',
    'database': 'whatever2',
    'user': 'motebang',
    'password': 'You_are_not_getting_it_from_me',
    'autocommit': True,
   }
]

# this is the connection configuration for the 3rd data source, in this example we will use mysql
Mysql_config = [
  {
    'user': 'motebang',
    'password': 'Again_wouldnt_you_want_to_know',
    'host': 'motebang_mysql1',
    'database': 'whatever',
  },
  #more of what i just said above, but replacing the 3 with a 4
  {
    'user': 'motebang',
    'password': 'Dont_use_the _same_password_over_and_over',
    'host': 'motebang_mysql2',
    'database': 'whatever2',
  },
  #abit more of what said above, but replacing the 4 with a 5. We use 3 mysql data sources because they are usually free and abundantly available, so cheapskate companies use them lol.
   {
    'user': 'motebang',
    'password': 'What_did_i_say_about_using_the_same_password?',
    'host': 'motebang_mysql3',
    'database': 'whatever3',
  },
]

# Here we will use an obscure database system, just for the fun of it, and to accomodate weird applications that do niche things, so we will go with firebird, it is weird enough
Firebird_config = [
  {
    'dsn': "//Server/path/to/firebird.db",
    'user': "motebang",
    'password': "Go_fly_a_Kite",
  }
]