from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions

def productmaster_parseInput(line):
    fields = line.split('|')
    return Row(Company_code = str(fields[0]), Category_Desc = str(fields[1]), Sub_Desc = str(fields[2]), Brand_Desc = str(fields[3]), Basepack_Desc = str(fields[4]) , Barcode = str(fields[5]) )
	
	
def BUSY_parseInput(line):
    fields = line.split('|')
    return Row( POS_Application_Name = str(fields[0]), STOREID = str(fields[1]), BILLNO = str(fields[2]), BARCODE = str(fields[3]), GUID = str(fields[4]) , CREATED_STAMP = int(fields[5]) , UPDATED_STAMP = int(fields[6]) )
	
	
def EASYSOL_parseInput(line):
    fields = line.split('|')
    return Row( POS_Application_Name = str(fields[0]), STOREID = str(fields[1]), BILLNO = str(fields[2]), BARCODE = str(fields[3]), GUID = str(fields[4]) , CREATED_STAMP = int(fields[5]) , UPDATED_STAMP = int(fields[6]) )
	
	
def MARG_parseInput(line):
    fields = line.split('|')
    return Row( POS_Application_Name = str(fields[0]), STOREID = str(fields[1]), BILLNO = str(fields[2]), BARCODE = str(fields[3]), GUID = str(fields[4]) , CREATED_STAMP = int(fields[5]) , UPDATED_STAMP = int(fields[6]) )


def RETAIL_EXPER_parseInput(line):
    fields = line.split('|')
    return Row( POS_Application_Name = str(fields[0]), STOREID = str(fields[1]), BILLNO = str(fields[2]), BARCODE = str(fields[3]), GUID = str(fields[4]) , CREATED_STAMP = int(fields[5]) , UPDATED_STAMP = int(fields[6]) )
	
def SOFT_GEN_parseInput(line):
    fields = line.split('|')
    return Row( POS_Application_Name = str(fields[0]), STOREID = str(fields[1]), BILLNO = str(fields[2]), BARCODE = str(fields[3]), GUID = str(fields[4]) , CREATED_STAMP = int(fields[5]) , UPDATED_STAMP = int(fields[6]) )
	
	
	
	if __name__ == "__main__":
    # Create a SparkSession
    spark = SparkSession.builder.appName("CassandraIntegration").config("spark.cassandra.connection.host", "127.0.0.1").getOrCreate()

    # Get the raw data
    lines = spark.sparkContext.textFile("hdfs:///user/maria_dev/MUZE/ProductMaster")
    
	# Convert it to a RDD of Row objects with (Company_code, Category_Desc, Sub_Desc , Brand_Desc, Basepack_Desc , Barcode )
    users = lines.map(productmaster_parseInput)
    
	# Convert that to a DataFrame
    usersDataset = spark.createDataFrame(users)
	
	# Write it into Cassandra
    usersDataset.write\
        .format("org.apache.spark.sql.cassandra")\
        .mode('append')\
        .options(table="ProductMaster", keyspace="HUL")\
        .save()
	''' -------------------------------------------------------------------------------------------------------------------'''	
		
	# Get the raw data
    lines = spark.sparkContext.textFile("hdfs:///user/maria_dev/MUZE/BUSY")
    
	# Convert it to a RDD of Row objects with (POS_Application_Name, STOREID, BILLNO , BARCODE, GUID , CREATED_STAMP  , UPDATED_STAMP)
    users = lines.map(BUSY_parseInput)
    
	# Convert that to a DataFrame
    usersDataset = spark.createDataFrame(users)
	
	# Write it into Cassandra
    usersDataset.write\
        .format("org.apache.spark.sql.cassandra")\
        .mode('append')\
        .options(table="BUSY", keyspace="HUL")\
        .save()
		
	''' -------------------------------------------------------------------------------------------------------------------'''		

	# Get the raw data
    lines = spark.sparkContext.textFile("hdfs:///user/maria_dev/MUZE/EASYSOL")
    
	# Convert it to a RDD of Row objects with (POS_Application_Name, STOREID, BILLNO , BARCODE, GUID , CREATED_STAMP , UPDATED_STAMP)
    users = lines.map(EASYSOL_parseInput)
    
	# Convert that to a DataFrame
    usersDataset = spark.createDataFrame(users)
	
	# Write it into Cassandra
    usersDataset.write\
        .format("org.apache.spark.sql.cassandra")\
        .mode('append')\
        .options(table="EASYSOL", keyspace="HUL")\
        .save()
	
	''' -------------------------------------------------------------------------------------------------------------------'''	
	
		# Get the raw data
    lines = spark.sparkContext.textFile("hdfs:///user/maria_dev/MUZE/MARG")
    
	# Convert it to a RDD of Row objects with (POS_Application_Name, STOREID, BILLNO , BARCODE, GUID , CREATED_STAMP )
    users = lines.map(MARG_parseInput)
    
	# Convert that to a DataFrame
    usersDataset = spark.createDataFrame(users)
	
	# Write it into Cassandra
    usersDataset.write\
        .format("org.apache.spark.sql.cassandra")\
        .mode('append')\
        .options(table="MARG", keyspace="HUL")\
        .save()
	
	''' -------------------------------------------------------------------------------------------------------------------'''	
	
	
			# Get the raw data
    lines = spark.sparkContext.textFile("hdfs:///user/maria_dev/MUZE/RETAIL_EXPER")
    
	# Convert it to a RDD of Row objects with (POS_Application_Name, STOREID, BILLNO , BARCODE, GUID , CREATED_STAMP )
    users = lines.map(RETAIL_EXPER_parseInput)
    
	# Convert that to a DataFrame
    usersDataset = spark.createDataFrame(users)
	
	# Write it into Cassandra
    usersDataset.write\
        .format("org.apache.spark.sql.cassandra")\
        .mode('append')\
        .options(table="RETAIL_EXPER", keyspace="HUL")\
        .save()
	
	''' -------------------------------------------------------------------------------------------------------------------'''	
	
				# Get the raw data
    lines = spark.sparkContext.textFile("hdfs:///user/maria_dev/MUZE/SOFT_GEN")
    
	# Convert it to a RDD of Row objects with (POS_Application_Name, STOREID, BILLNO , BARCODE, GUID , CREATED_STAMP )
    users = lines.map(SOFT_GEN_parseInput)
    
	# Convert that to a DataFrame
    usersDataset = spark.createDataFrame(users)
	
	# Write it into Cassandra
    usersDataset.write\
        .format("org.apache.spark.sql.cassandra")\
        .mode('append')\
        .options(table="SOFT_GEN", keyspace="HUL")\
        .save()
	
	''' -------------------------------------------------------------------------------------------------------------------'''	
	
	
	
	
	
	
	
	    # Read it back from Cassandra into a new Dataframe
    readUsers = spark.read\
    .format("org.apache.spark.sql.cassandra")\
    .options(table="ProductMaster", keyspace="movielens")\
    .load()

    readUsers.createOrReplaceTempView("ProductMaster")

    sqlDF = spark.sql("SELECT * FROM ProductMaster LIMIT 20")
    sqlDF.show()

	
	
	
    # Stop the session
    spark.stop()

	
	
	
	
	