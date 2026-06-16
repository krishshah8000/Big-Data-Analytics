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
