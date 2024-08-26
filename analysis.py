import numpy as np

# Load Data Part
def load_data(filename):

    """
    Load data from a CSV file.

    Args:
    - filename (str): Path to the CSV file.

    Returns:
    - data (numpy.ndarray): Loaded data as a numpy array.
    - column_names (list): List of column names extracted from the file.
    """

    try:
        data = np.genfromtxt(filename, delimiter=',', dtype=float, skip_header=1)
        with open(filename, 'r') as f:
            column_names = f.readline().strip().split(',')
        return data, column_names
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None, None
    
def display_dataset_preview(data, column_names):

    """
    Displays a preview of the dataset, showing column names and the 
    first 10 rows of data.

    Parameters:
    data (numpy.ndarray): The numpy array containing the dataset.
    column_names (list): List of column names corresponding to the dataset.

    Returns:
    None
    """

    print("\nDisplaying Dataset Preview:")
    num_rows_to_display = min(10, data.shape[0])  # Display up to 10 rows
    print("\nColumn Names:")
    print(column_names)
    print("\nFirst {} rows of the dataset:".format(num_rows_to_display))
    print(data[:num_rows_to_display])

def show_column_names(filename):

    """
    Displays the column names read from the header row of a CSV file.

    Parameters:
    filename (str): The path to the CSV file.

    Returns:
    None
    """

    with open(filename, 'r') as f:
        column_names = f.readline().strip().split(',')
    print("\nColumn Names:")
    print(column_names)

    return column_names

def show_basic_info(data):

    """
    Displays basic information about a numpy array.

    Parameters:
    data (numpy.ndarray): The numpy array containing the dataset.

    Returns:
    None
    """

    print("\nBasic information about numpy array:")
    print("Shape:", data.shape)
    print("Size:", data.size)
    print("Number of dimensions:", data.ndim)
    print("Item size:", data.itemsize)
    print("Data type:", data.dtype)
    print("\nPreview of the first 5 rows:")
    print(data[:5])

def show_missing_values(data, filename):

    """
    Prints the number of missing (NaN) values in each column of a numpy array.

    Parameters:
    data (numpy.ndarray): The numpy array containing the dataset.

    Returns: None
    """

    missing_counts = np.sum(np.isnan(data), axis=0)
    print("\nMissing value counts per column:")
    column_names = show_column_names(filename)
    print(column_names)
    for i, col in enumerate(column_names):
        print(f"Column '{col}': {missing_counts[i]} missing values")

# Remove missing values
def remove_missing_values(data):

    """
    Replace missing values (NaN) in the data with 0.

    Args:
    - data (numpy.ndarray): Input data with potential missing values.

    Returns:
    - data (numpy.ndarray): Data with missing values replaced by 0.
    """
    
    data[np.isnan(data)] = 0
    return data

# Finding mean, max, median values
def calculate_statistics(data, column_names):

    """
    Calculate mean, max, median, and mode values for each column of the data.

    Args:
    - data (numpy.ndarray): Input data.

    Returns:
    - mean_values (numpy.ndarray): Mean values for each column.
    - max_values (numpy.ndarray): Maximum values for each column.
    - median_values (numpy.ndarray): Median values for each column.
    - mode_values (numpy.ndarray): Mode values for each column.
    """

    mean_values = np.mean(data, axis=0)
    max_values = np.max(data, axis=0)
    median_values = np.median(data, axis=0)
    mode_values = np.zeros(data.shape[1], dtype=float)

    for i in range(data.shape[1]):
        col_data = data[:, i]

        if np.any(col_data < 0):
            mode_values[i] = np.nan
            continue

        col_data = col_data.astype(int)
        mode_values[i] = np.argmax(np.bincount(col_data))
    print("\nStatistical summary:")
    for i, col in enumerate(column_names):
        print(f"Column '{col}': Mean={mean_values[i]}, Max={max_values[i]}, \
              Median={median_values[i]}, Mode={mode_values[i]}")

    return mean_values, max_values, median_values, mode_values

# Income mean calculation
def calculate_income_mean(data):

    """
    Calculate the mean income from the data.

    Args:
    - data (numpy.ndarray): Input data.

    Returns:
    - income_mean (float): Mean income.
    """

    return np.mean(data[:, 7])

# Analysis Part

def calculate_avg_population_bedrooms_gt_n(data, n):

    """
    Calculate the average population in areas with bedrooms greater than n.

    Args:
    - data (numpy.ndarray): Input data.
    - n (int): Number of bedrooms threshold.

    Returns:
    - avg_population (float): Average population in areas with bedrooms > n.
    """

    bedrooms_gt_n = data[data[:, 4] > n]
    return np.mean(bedrooms_gt_n[:, 5])

def calculate_avg_house_value_bedrooms_gt_n(data, n):

    """
    Calculate the average house value in areas with bedrooms greater than n.

    Args:
    - data (numpy.ndarray): Input data.
    - n (int): Number of bedrooms threshold.

    Returns:
    - avg_house_value (float): Average house value in areas with bedrooms > n.
    """

    bedrooms_gt_n = data[data[:, 4] > n]
    return np.mean(bedrooms_gt_n[:, 8])

def calculate_avg_income_bedrooms_gt_n(data, n):

    """
    Calculate the average income in areas with bedrooms greater than n.

    Args:
    - data (numpy.ndarray): Input data.
    - n (int): Number of bedrooms threshold.

    Returns:
    - avg_income (float): Average income in areas with bedrooms > n.
    """

    bedrooms_gt_n = data[data[:, 4] > n]
    return np.mean(bedrooms_gt_n[:, 7])

def calculate_avg_income_rooms_gt_3(data):

    """
    Calculate the average income of people with more than 3 rooms per household.

    Args:
    - data (numpy.ndarray): Input data.

    Returns:
    - avg_income (float): Average income of people with more than 3 rooms per household.
    """

    rooms_per_household_gt_3 = data[data[:, 4] > 3]
    return np.mean(rooms_per_household_gt_3[:, 7])

def calculate_avg_population_high_density(data):

    """
    Calculate the average population in households with high density (> 1000).

    Args:
    - data (numpy.ndarray): Input data.

    Returns:
    - avg_population (float): Average population in households with high density (> 1000).
    """

    high_density_households = data[data[:, 5] > 1000]
    return np.mean(high_density_households[:, 5])

def calculate_avg_house_value_high_density(data):

    """
    Calculate the average house value in households with high density (> 1000).

    Args:
    - data (numpy.ndarray): Input data.

    Returns:
    - avg_house_value (float): Average house value in households with high density (> 1000).
    """

    high_density_households = data[data[:, 5] > 1000]
    return np.mean(high_density_households[:, 8])

def average_income_by_bedrooms(data):

    """
    Calculate the average income by total number of bedrooms.

    Args:
    - data (numpy.ndarray): Input data.

    Returns:
    - unique_bedrooms (numpy.ndarray): Unique values of total bedrooms.
    - avg_income_by_bedrooms (numpy.ndarray): Average income corresponding to
      each unique total bedrooms value.
    """

    total_bedrooms = data[:, 4]
    median_income = data[:, 7]

    unique_bedrooms, counts = np.unique(total_bedrooms, return_counts=True)
    avg_income_by_bedrooms = np.zeros_like(unique_bedrooms, dtype=float)

    for i, bedrooms in enumerate(unique_bedrooms):
        avg_income_by_bedrooms[i] = np.mean(median_income[total_bedrooms == bedrooms])

    return unique_bedrooms, avg_income_by_bedrooms

