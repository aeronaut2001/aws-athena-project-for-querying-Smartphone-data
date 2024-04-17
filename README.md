# aws-athena-project-for-Smartphone-data

learning :  
query run time reduced for parquet format than csv
then if we use bucketing and partition then also scan reduce and help save cost
data repartition support on athena
but data  rebucketing  is not after bucketing or create the table 


take care of query performance and cost reduction using 
compression of differnet file formats
and algorithm utilize for compresion and decompression
like Gzip,bzip2,lzo,snappy check official documantation to read more about it


order by optimization 
use limit

in joins always right big data table on left side and small data table on 
right side it reduce the run time

group by 
always write high cardanality (unique) value first and then lowest last


distinct 
in distinct give accurate number of distinct count 
but if you go with approse distinct it give related number but faster result 2.3% in original result
we utilize it for where we need to take random count like count million row




