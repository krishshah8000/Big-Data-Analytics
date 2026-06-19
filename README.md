# Hadoop Practice – WordCount Example

## Overview
This repository contains my practice work on Apache Hadoop, focusing on setting up the Hadoop environment and executing the classic **WordCount** MapReduce program.

## Work Completed

- Installed and configured Apache Hadoop.
- Started Hadoop services (HDFS and related daemons).
- Verified running Hadoop processes using `jps`.
- Created an input directory in HDFS.
- Uploaded a text file (`data`) into the HDFS input directory.
- Verified the uploaded file using HDFS commands.
- Executed the Hadoop **WordCount** MapReduce example.
- Generated output in the HDFS output directory.
- Displayed the final word frequency results.

## HDFS Commands Used

```bash
# Create input directory
hdfs dfs -mkdir /input

# Upload local file to HDFS
hdfs dfs -put data /input

# List files in HDFS
hdfs dfs -ls /input

# View file contents
hdfs dfs -cat /input/data

# Remove previous output (if it exists)
hdfs dfs -rm -r /output

# Run WordCount
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /input /output

# View output
hdfs dfs -cat /output/part-r-00000
```

## Objective

The objective of this exercise was to understand the basic Hadoop workflow:
1. Store data in HDFS.
2. Execute a MapReduce job.
3. Process text data to count word occurrences.
4. Retrieve and verify the output.

## Learning Outcomes

- Gained hands-on experience with HDFS operations.
- Understood how to upload and access files in Hadoop.
- Learned how to run a MapReduce job using the built-in WordCount example.
- Explored the structure of Hadoop input and output directories.

## Repository Contents

```
Big-Data-Analytics/
├── README.md
├── data                 # Sample input file
└── (WordCount output generated in HDFS)
```

## Next Steps

- Implement a custom WordCount program in Java.
- Explore Mapper and Reducer classes in detail.
- Practice additional MapReduce examples such as Average, Inverted Index, and Log Analysis.


# Hadoop MapReduce – Word Count on Multiple Files

## Objective

Perform a Word Count operation on multiple text files stored in HDFS using the Hadoop MapReduce framework and display the frequency of each word.

## Steps Performed

1. Started Hadoop services.
2. Created an HDFS input directory (`/input2`).
3. Created two sample text files (`file1.txt` and `file2.txt`).
4. Uploaded both files to HDFS using `hdfs dfs -put`.
5. Executed the built-in Hadoop `wordcount` MapReduce program.
6. Stored the results in a new HDFS output directory.
7. Displayed the final word frequencies using `hdfs dfs -cat`.

## Key Commands

* Create HDFS directory: `hdfs dfs -mkdir /input2`
* Upload files: `hdfs dfs -put file1.txt /input2`
* Run WordCount:
  `hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /input2 /output3`
* View output:
  `hdfs dfs -cat /output3/part-r-00000`

## Outcome

The Hadoop MapReduce job successfully processed multiple input files from HDFS and generated the frequency count of each unique word in the output directory.
