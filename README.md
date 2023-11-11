<br/>
<p align="center">
  <a href="https://github.com//Real-Vs-Nominal-Cash-Flow-Analysis-Multiprocessing">
    <img src="" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Unlocking Financial Clarity: Mastering Real vs. Nominal Cash Flow Analysis</h3>

  <p align="center">
    Transform Your Financial Insights – Dive Deep into the Real Story Behind Your Numbers!
    <br/>
    <br/>
    <a href="https://github.com//Real-Vs-Nominal-Cash-Flow-Analysis-Multiprocessing"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com//Real-Vs-Nominal-Cash-Flow-Analysis-Multiprocessing">View Demo</a>
    .
    <a href="https://github.com//Real-Vs-Nominal-Cash-Flow-Analysis-Multiprocessing/issues">Report Bug</a>
    .
    <a href="https://github.com//Real-Vs-Nominal-Cash-Flow-Analysis-Multiprocessing/issues">Request Feature</a>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Scenario

A financial analysis team at a large corporation is tasked with adjusting a substantial dataset of nominal cash flows for inflation. The dataset is extensive, comprising millions of rows, and needs to be processed efficiently to meet a tight deadline. The team decides to use Python for this task, leveraging its powerful data manipulation libraries and parallel processing capabilities. However, they face a few challenges:

1. **Efficiency in Processing Large Datasets**: The dataset's size demands efficient processing to ensure timely completion. Traditional, single-threaded approaches are too slow.

2. **Accuracy in Inflation Adjustment**: It's crucial to accurately adjust each cash flow value for inflation to ensure the integrity of the financial analysis.

3. **Resource Management**: Effective use of system resources, like CPU cores, is essential to optimize processing time without overloading the system.

4. **Reporting Execution Time**: For performance evaluation and future optimization, the team needs to track and report the time taken for different stages of the data processing task.

### Solution: Using the Provided Script

The team employs the provided Python script, which is designed to efficiently process large datasets and adjust nominal cash flows for inflation. Here's how the script addresses each challenge:

1. **Efficient Parallel Processing**:
   - The script uses the `multiprocessing` library to distribute the dataset across multiple CPU cores, significantly speeding up the computation.
   - It divides the dataset into chunks and processes each chunk in parallel, utilizing the full computational power of the system.

2. **Accurate Inflation Adjustment**:
   - The `adjust_for_inflation` function reliably adjusts each nominal value based on the given inflation rate, ensuring accurate financial calculations.
   - This adjustment is applied consistently across all data chunks, maintaining the integrity of the analysis.

3. **Optimized Resource Utilization**:
   - By dynamically determining the number of processes based on the CPU count (`multiprocessing.cpu_count()`), the script optimally utilizes available system resources.
   - This approach prevents overloading the system while ensuring maximum processing speed.

4. **Performance Tracking and Reporting**:
   - The script includes time tracking for both data loading and processing phases, providing insights into performance bottlenecks.
   - This detailed timing information (loading time, calculation time, and total execution time) helps in evaluating the efficiency of the process and guides future optimizations.

### Execution and Output

- When executed, the script first loads the dataset from a CSV file (`NominalCashFlows.csv`) and then processes it to adjust each cash flow value for a specified inflation rate (e.g., 2%).
- It reports the time taken for loading the data, performing the calculations, and the total execution time.
- The adjusted dataset is then saved to a text file (`InflationAdjustedCashFlows.txt`), ready for further analysis or reporting.

### Conclusion

The script effectively solves the team's challenges by delivering a fast, accurate, and resource-efficient solution for adjusting a large dataset of nominal cash flows for inflation, complete with performance tracking and reporting. This approach not only meets their immediate needs but also sets a precedent for handling similar tasks in the future.

The provided Python script is designed to adjust a dataset of nominal cash flow values for inflation, leveraging parallel processing to improve efficiency. Here's a breakdown of its logic and functionality:

### Import Statements
- `pandas` and `numpy`: Used for data manipulation and handling.
- `multiprocessing`: Enables parallel processing, utilizing multiple CPU cores for faster computation.
- `functools.partial`: Creates a partial function application for easier argument passing.
- `time`: For measuring the time taken by different parts of the script.

### Function Definitions
1. **adjust_for_inflation**
   - **Purpose**: Adjust a nominal value for inflation.
   - **Input**: `nominal_value` (the value to adjust), `inflation_rate` (the rate of inflation).
   - **Output**: Inflation-adjusted value.

2. **process_chunk**
   - **Purpose**: Apply inflation adjustment to a chunk of data.
   - **Input**: `chunk` (a subset of the dataset), `inflation_rate`.
   - **Output**: Chunk of data with inflation-adjusted values.

3. **calculate_real_values**
   - **Purpose**: Calculate real values for the entire dataset using parallel processing.
   - **Steps**:
     - Determine the number of processes based on CPU count.
     - Divide the dataset into chunks.
     - Create a pool of processes and distribute chunks among them.
     - Measure and print the time taken for this computation.
   - **Output**: DataFrame with inflation-adjusted values.

### Main Function
- **Purpose**: Execute the overall process.
- **Steps**:
  1. **Initialization**: Start timing the entire process.
  2. **Data Loading**:
     - Load the dataset from a CSV file.
     - Measure and print the time taken for loading.
  3. **Adjustment Calculation**:
     - Extract nominal values.
     - Calculate real values using the `calculate_real_values` function.
  4. **Data Output**:
     - Add real values to the original DataFrame.
     - Save the adjusted data to a text file in a formatted manner.
  5. **Finalization**: Measure and print the total execution time.

### Usage Example
- At the end of the script, there is a conditional (`if __name__ == "__main__":`) which allows the script to be run as a standalone program.
- It calls the `main` function with a sample CSV file ('NominalCashFlows.csv') and an example inflation rate (2%).

### Parallel Processing
- A key aspect of this script is its use of the `multiprocessing` module, enabling it to process large datasets more efficiently by dividing the workload among multiple CPU cores.
- This is particularly useful for compute-intensive tasks and large datasets.

### File I/O
- The script reads data from a CSV file and outputs the results to a text file, demonstrating data input/output operations in Python.

### Overall
The script is a practical example of handling, processing, and analyzing financial data in Python, showcasing techniques like parallel processing, data manipulation with Pandas, and performance measurement.

The output results from the script provide insights into the performance and efficiency of the data processing task. Here's a detailed explanation of each component:

### Loading Time: 0.05607461929321289 seconds
- **What It Means**: This is the time taken to load the dataset from the CSV file into a Pandas DataFrame.
- **Interpretation**:
  - A relatively short time, indicating efficient data loading.
  - The actual time can vary depending on the size of the CSV file and the performance of the I/O subsystem of the machine where the script is running.

### Calculation Time: 0.03148698806762695 seconds
- **What It Means**: This is the time taken to adjust the nominal values for inflation across the entire dataset.
- **Interpretation**:
  - Significantly quick, highlighting the efficiency of parallel processing in handling the computational task.
  - This duration is the aggregated time for processing all chunks of data in parallel. It is notably short due to the distribution of work across multiple CPU cores.
  - It demonstrates the advantage of using multiprocessing for compute-intensive tasks, especially on systems with multiple cores.

### Total Execution Time: 6.296285390853882 seconds
- **What It Means**: This is the overall time taken from the start to the end of the script's execution, including data loading, processing, and any other overhead.
- **Interpretation**:
  - This duration is considerably longer than the sum of the loading and calculation times. This discrepancy suggests that there are other significant overheads in the script.
  - These overheads could include:
    - The initialization of the multiprocessing pool.
    - Overhead due to dividing the dataset into chunks and combining the results.
    - Time taken to write the adjusted data to a file.
    - Any additional processing or data manipulation not explicitly timed in the output.
  - It's important to note that while parallel processing accelerates the calculation, it also introduces overhead, especially when initializing and terminating processes.

### Process finished with exit code 0
- **What It Means**: This indicates that the script completed successfully without any errors.
- **Interpretation**:
  - An exit code of 0 is standard in programming to signify successful completion.
  - It means that all functions and processes in the script executed as expected and there were no unhandled exceptions or errors that caused an abnormal termination.

### Overall Interpretation
- The output reflects an efficient data processing operation, especially in terms of data loading and parallel computation.
- The significant difference between the total execution time and the sum of loading and calculation times underscores the impact of various overheads associated with multiprocessing and other non-timed operations in the script.
- Successful completion without errors indicates good script health and robust error handling.

## Built With

This project is built using a combination of powerful Python libraries and techniques, each chosen for its specific capabilities in handling, processing, and analyzing large datasets. Below is a detailed overview of each component used in this project:

#### 1. Python
- **Language**: Python 3.x
- **Reason for Choice**: Python's simplicity and vast ecosystem of libraries make it ideal for data processing and analysis tasks.

#### 2. Pandas
- **Library**: `pandas`
- **Purpose**: Data Manipulation and Analysis
- **Features Used**:
  - `read_csv()`: For loading data from CSV files into DataFrame structures.
  - DataFrame Operations: For manipulating and preparing data for analysis.
  - `to_string()`: To convert DataFrames into string format for saving.
- **Why Pandas**: Offers fast, flexible, and expressive data structures designed to make working with structured (tabular, multidimensional, potentially heterogeneous) and time series data both easy and intuitive.

#### 3. NumPy
- **Library**: `numpy`
- **Purpose**: Numerical Processing
- **Features Used**:
  - `ceil()`: Used in calculating the size of each chunk for data processing.
- **Why NumPy**: A fundamental package for scientific computing with Python, providing powerful data structures for efficient computation of multi-dimensional arrays and matrices.

#### 4. Multiprocessing
- **Library**: `multiprocessing`
- **Purpose**: Parallel Processing
- **Features Used**:
  - `cpu_count()`: To determine the number of available CPU cores for parallel processing.
  - `Pool`: To create a pool of worker processes for distributing the computation tasks.
- **Why Multiprocessing**: Enables the use of multiple processors on a machine, significantly improving the script's performance by parallelizing data processing, especially beneficial for large datasets.

#### 5. functools
- **Module**: `functools`
- **Purpose**: Higher-order Functions and Operations on Callable Objects
- **Features Used**:
  - `partial()`: To create partial functions, enabling us to freeze a portion of a function's arguments and keywords resulting in a new object.
- **Why functools**: Essential for simplifying the function calls when working with the multiprocessing pool, allowing for more flexible code.

#### 6. Time
- **Module**: `time`
- **Purpose**: Time Tracking
- **Features Used**:
  - `time()`: To measure the duration of data loading and processing stages.
- **Why Time**: Critical for performance measurement, helping in understanding and optimizing the time complexity of data processing tasks.

#### Development and Execution Environment
- **Platform**: This script is platform-independent but ideally run in an environment with multiple CPU cores for optimal performance.
- **Requirements**: Python 3.x with Pandas, NumPy, and Multiprocessing libraries installed. Suitable for execution in various environments, including local machines, cloud-based computing platforms, or dedicated data servers.

#### Version Control
- **System**: Git
- **Repository Hosting Service**: GitHub
- **Reason**: Git, in conjunction with GitHub, provides robust version control, allowing for efficient collaboration, code tracking, and documentation.

#### Conclusion
This project leverages a blend of Python's computational libraries and parallel processing capabilities, making it highly efficient for large-scale data analysis tasks such as adjusting financial datasets for inflation. The chosen technologies not only facilitate quick and accurate computations but also allow for scalability and easy maintenance.Here are a few examples.

## Getting Started

This section guides you through setting up and running the Inflation Adjustment Script on your local machine for development and testing purposes. Follow these instructions to get a copy of the project up and running.

#### Prerequisites

Before you begin, ensure you have the following installed:
1. **Python**: The script is written in Python 3.x. You can download Python from [python.org](https://www.python.org/downloads/).
2. **Pandas Library**: Used for data manipulation. Install it using pip:
   ```
   pip install pandas
   ```
3. **NumPy Library**: Required for numerical computations. Install it using pip:
   ```
   pip install numpy
   ```

#### Installation

1. **Clone the Repository**
   - Use Git or checkout with SVN using the following URL: `https://github.com/your_username_/Project-Name.git`.

2. **Navigate to the Project Directory**
   - Open a terminal and navigate to the directory where you cloned the repo.

#### Running the Script

1. **Prepare Your Data File**
   - Ensure you have a CSV file with the necessary data. The script expects a column named 'NominalCashFlow' in this file.
   - Example CSV format:
     ```
     NominalCashFlow
     10000
     15000
     20000
     ...
     ```

2. **Set the Inflation Rate**
   - Determine the inflation rate you wish to apply. This is a decimal value (e.g., 0.02 for 2%).

3. **Run the Script**
   - Execute the script by running:
     ```
     python main.py 'path/to/your/NominalCashFlows.csv' 0.02
     ```
   - Replace `'path/to/your/NominalCashFlows.csv'` with the path to your CSV file and `0.02` with your desired inflation rate.

4. **View the Output**
   - The script will adjust the nominal values for inflation and save the output in a file named 'InflationAdjustedCashFlows.txt'.
   - It will also print the loading time, calculation time, and total execution time in the console.

#### Troubleshooting

- If you encounter any errors related to missing libraries, ensure that all the required packages (`pandas`, `numpy`) are installed.
- Ensure that the CSV file is correctly formatted and accessible at the specified path.

#### Contributing

We welcome contributions to this project. Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

#### Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your_username_/Project-Name/tags).


This guide should help you get started with the Inflation Adjustment Script. For more details, refer to the `README.md` file in the project repository.

## Roadmap

See the [open issues](https://github.com//Real-Vs-Nominal-Cash-Flow-Analysis-Multiprocessing/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com//Real-Vs-Nominal-Cash-Flow-Analysis-Multiprocessing/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com//Real-Vs-Nominal-Cash-Flow-Analysis-Multiprocessing/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com//Real-Vs-Nominal-Cash-Flow-Analysis-Multiprocessing/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion) - **

## Acknowledgements

* []()
* []()
* []()
