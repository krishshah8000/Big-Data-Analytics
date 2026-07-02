# Hadoop Streaming MapReduce – Top Product by City

## Objective

The objective of this experiment is to analyze city-wise product sales using Hadoop Streaming with Python. The program calculates the total sales of each product in every city and identifies the **top-selling product** for each city.

---

## Requirements

- Ubuntu Linux
- Java
- Hadoop (HDFS + YARN)
- Python 3
- Hadoop Streaming JAR

---

## Dataset

**File Name:**

```
sales_products.txt
```

**Format:**

```
ProductID,ProductName,Price,City
```

**Example:**

```
101,Laptop,55000,Mumbai
102,Mobile,25000,Delhi
103,Laptop,60000,Mumbai
104,TV,45000,Delhi
105,Mobile,26000,Mumbai
106,Laptop,58000,Bangalore
107,TV,47000,Bangalore
108,Mobile,24000,Delhi
109,Laptop,62000,Chennai
110,TV,48000,Chennai
```

A larger dataset is generated using:

```bash
for i in {1..100}; do cat sales_products.txt; done > sales_products_large.txt
```

---

## Files Used

| File | Description |
|------|-------------|
| sales_products.txt | Original sales dataset |
| sales_products_large.txt | Expanded dataset |
| mapper_city_products.py | Mapper that extracts city, product, and price |
| reducer_city_products.py | Reducer that calculates total sales and finds the top-selling product for each city |

---

## Workflow

### Step 1

Start Hadoop services (if not already running).

```bash
start-dfs.sh
start-yarn.sh
```

---

### Step 2

Create the sales dataset.

```
sales_products.txt
```

---

### Step 3

Generate a larger dataset.

```bash
for i in {1..100}; do cat sales_products.txt; done > sales_products_large.txt
```

---

### Step 4

Create the Python Mapper.

```
mapper_city_products.py
```

The mapper reads each record and outputs:

```
City_Product    Price
```

Example:

```
Mumbai_Laptop    55000
Delhi_TV         45000
```

---

### Step 5

Create the Python Reducer.

```
reducer_city_products.py
```

The reducer:

- Groups records by city and product.
- Calculates the total sales for each product.
- Compares product sales within each city.
- Displays the highest-selling product for every city.

Example Output:

```
TOP PRODUCT PER CITY:
========================================
Bangalore: Laptop (₹5,800,000.00)
Chennai: Laptop (₹6,200,000.00)
Delhi: TV (₹4,500,000.00)
Mumbai: Laptop (₹11,500,000.00)
```

---

### Step 6

Upload the dataset to HDFS.

```bash
hdfs dfs -mkdir -p /user/$USER/sales_products/input
hdfs dfs -put sales_products_large.txt /user/$USER/sales_products/input/
```

---

### Step 7

Run the Hadoop Streaming job.

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-files mapper_city_products.py,reducer_city_products.py \
-input /user/$USER/sales_products/input/sales_products_large.txt \
-output /user/$USER/sales_products/city_output \
-mapper "python3 mapper_city_products.py" \
-reducer "python3 reducer_city_products.py"
```

---

### Step 8

View the output.

```bash
hdfs dfs -cat /user/$USER/sales_products/city_output/part-00000
```

---

## Expected Output

```
TOP PRODUCT PER CITY:
========================================
Bangalore: Laptop (₹5,800,000.00)
Chennai: Laptop (₹6,200,000.00)
Delhi: TV (₹4,500,000.00)
Mumbai: Laptop (₹11,500,000.00)
```

*(The sales values are higher because the original dataset is repeated 100 times.)*

---

## Hadoop Streaming Flow

```
Sales Dataset
      |
      v
    Mapper
(City_Product, Price)
      |
      v
Shuffle and Sort
      |
      v
    Reducer
      |
      v
Top-Selling Product for Each City
```

---

## Conclusion

This experiment demonstrates the use of Hadoop Streaming with Python to process large-scale sales data. The mapper extracts the city, product, and sales amount from each record, while the reducer aggregates product sales by city and identifies the highest-selling product. The dataset stored in HDFS is processed efficiently using the MapReduce framework.
