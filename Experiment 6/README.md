# Hadoop Streaming MapReduce – Weather Data Analysis

## Objective

The objective of this experiment is to perform weather data analysis using Hadoop Streaming with Python. The program finds:

- Hottest Day (Maximum Temperature)
- Coldest Day (Minimum Temperature)

---

## Requirements

- Ubuntu Linux
- Java
- Hadoop (HDFS + YARN)
- Python 3
- Hadoop Streaming JAR

---

## Dataset

File Name:

```
weather_data.txt
```

Format:

```
Date,City,Maximum Temperature,Minimum Temperature
```

Example:

```
2024-01-01,Delhi,12,5
2024-01-02,Delhi,14,6
2024-01-03,Delhi,10,3
...
```

A larger dataset is generated using:

```bash
for i in {1..100}; do cat weather_data.txt; done > weather_large.txt
```

---

## Files Used

| File | Description |
|------|-------------|
| weather_data.txt | Original weather dataset |
| weather_large.txt | Expanded dataset |
| mapper_max_temp.py | Mapper that extracts Date and Maximum Temperature |
| reducer_max_temp.py | Reducer that finds the hottest day |
| reducer_min_temp.py | Reducer that finds the coldest day |

---

## Workflow

### Step 1

Start Hadoop services.

```bash
start-dfs.sh
start-yarn.sh
```

---

### Step 2

Create the weather dataset.

```
weather_data.txt
```

---

### Step 3

Generate a larger dataset.

```bash
for i in {1..100}; do cat weather_data.txt; done > weather_large.txt
```

---

### Step 4

Create the Python Mapper.

```
mapper_max_temp.py
```

The mapper reads each record and outputs:

```
Date    MaximumTemperature
```

Example:

```
2024-01-01    12
```

---

### Step 5

Create Reducer for Maximum Temperature.

```
reducer_max_temp.py
```

This reducer finds the highest temperature and prints the corresponding date.

Example Output:

```
Hottest Day: 2024-01-09 with 33.0°C
```

---

### Step 6

Create Reducer for Minimum Temperature.

```
reducer_min_temp.py
```

This reducer finds the lowest maximum temperature and prints the corresponding date.

Example Output:

```
Coldest Day: 2024-01-03 with 10.0°C
```

---

### Step 7

Upload the dataset to HDFS.

```bash
hdfs dfs -mkdir -p /user/$USER/weather/input
hdfs dfs -put weather_large.txt /user/$USER/weather/input/
```

---

### Step 8

Run the Hadoop Streaming job for the hottest day.

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/$USER/weather/input/weather_large.txt \
-output /user/$USER/weather/output \
-mapper "python3 mapper_max_temp.py" \
-reducer "python3 reducer_max_temp.py" \
-file mapper_max_temp.py \
-file reducer_max_temp.py
```

View the result:

```bash
hdfs dfs -cat /user/$USER/weather/output/part-00000
```

---

### Step 9

Run the Hadoop Streaming job for the coldest day.

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-input /user/$USER/weather/input/weather_large.txt \
-output /user/$USER/weather/output_min \
-mapper "python3 mapper_max_temp.py" \
-reducer "python3 reducer_min_temp.py" \
-file mapper_max_temp.py \
-file reducer_min_temp.py
```

View the result:

```bash
hdfs dfs -cat /user/$USER/weather/output_min/part-00000
```

---

## Expected Output

### Hottest Day

```
Hottest Day: 2024-01-09 with 33.0°C
```

### Coldest Day

```
Coldest Day: 2024-01-03 with 10.0°C
```

---

## Hadoop Streaming Flow

```
Weather Dataset
       |
       v
     Mapper
(Date, Max Temperature)
       |
       v
Shuffle and Sort
       |
       v
    Reducer
       |
       v
Final Result
```

---

## Conclusion

This experiment demonstrates how Hadoop Streaming can execute Python-based MapReduce programs. The mapper extracts the required temperature information, while reducers compute the hottest and coldest days from the weather dataset stored in HDFS.
