import pandas as pd
import numpy as np
import multiprocessing
from functools import partial
import time

def adjust_for_inflation(nominal_value, inflation_rate):
    return nominal_value / (1 + inflation_rate)

def process_chunk(chunk, inflation_rate):
    return chunk.apply(adjust_for_inflation, args=(inflation_rate,))

def calculate_real_values(df, inflation_rate):
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    chunk_size = int(np.ceil(len(df) / num_processes))
    chunks = [df[i:i + chunk_size] for i in range(0, len(df), chunk_size)]
    func = partial(process_chunk, inflation_rate=inflation_rate)

    start_time = time.time()  # Start timing the calculation
    real_values = pd.concat(pool.map(func, chunks))
    end_time = time.time()  # End timing the calculation

    pool.close()
    pool.join()

    print(f"Calculation Time: {end_time - start_time} seconds")  # Print calculation time
    return real_values

def main(csv_file, inflation_rate):
    start_time = time.time()  # Start timing the entire process

    # Load the dataset and time this process
    load_start_time = time.time()
    df = pd.read_csv(csv_file)
    load_end_time = time.time()
    print(f"Loading Time: {load_end_time - load_start_time} seconds")  # Print loading time

    # Assuming the CSV has a column 'NominalCashFlow'
    nominal_values = df['NominalCashFlow']

    # Calculate real values
    real_values = calculate_real_values(nominal_values, inflation_rate)

    # Add real values to dataframe
    df['RealCashFlow'] = real_values

    # Professionally format and save output
    with open('InflationAdjustedCashFlows.txt', 'w') as file:
        df_string = df.to_string(index=False)  # Convert the DataFrame to a string
        file.write(df_string)  # Write the string to a file
        # print(df_string)  # Print the formatted DataFrame

    end_time = time.time()  # End timing the entire process
    print(f"Total Execution Time: {end_time - start_time} seconds")  # Print total execution time

# Example usage
if __name__ == "__main__":
    main('NominalCashFlows.csv', 0.02)  # Example inflation rate of 2%
