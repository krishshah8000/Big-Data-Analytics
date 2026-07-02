Hadoop MapReduce – Word Count on Multiple Files
Objective
Perform a Word Count operation on multiple text files stored in HDFS using the Hadoop MapReduce framework and display the frequency of each word.

Steps Performed
Started Hadoop services.
Created an HDFS input directory (/input2).
Created two sample text files (file1.txt and file2.txt).
Uploaded both files to HDFS using hdfs dfs -put.
Executed the built-in Hadoop wordcount MapReduce program.
Stored the results in a new HDFS output directory.
Displayed the final word frequencies using hdfs dfs -cat.
Key Commands
Create HDFS directory: hdfs dfs -mkdir /input2
Upload files: hdfs dfs -put file1.txt /input2
Run WordCount: hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /input2 /output3
View output: hdfs dfs -cat /output3/part-r-00000
Outcome
The Hadoop MapReduce job successfully processed multiple input files from HDFS and generated the frequency count of each unique word in the output directory.
