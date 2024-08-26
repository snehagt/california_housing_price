import matplotlib.pyplot as plt
import numpy as np

def plot_income_mean(income_mean):

    """
    Plot the income mean.

    Args:
    - income_mean (float): Mean income value.
    """

    plt.figure(figsize=(8, 6))
    plt.bar(['Income Mean'], [income_mean], color='skyblue')
    plt.title('Income Mean')
    plt.ylabel('Income')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_income_population(data, income_threshold):

    """
    Plots income per household and population in areas where income is 
    greater than the specified threshold.

    Parameters:
    data (numpy.ndarray): The numpy array containing the dataset.
    income_threshold (float): The income value to filter the dataset.

    Returns:
    None
    """

    income_column_index = -3
    population_column_index = -6
    # Filter the dataset
    filtered_data = data[data[:, income_column_index] > income_threshold]

    # Extract income and population
    income = filtered_data[:, income_column_index]
    population = filtered_data[:, population_column_index]

    plt.figure(figsize=(10, 6))
    plt.scatter(income, population, alpha=0.5, c='blue', edgecolors='w', s=50)
    plt.title(f'Income vs Population for Areas with Income > {income_threshold}')
    plt.xlabel('Income per Household')
    plt.ylabel('Population')
    plt.grid(True)
    plt.show()

def plot_avg_population_bedrooms_gt_n(data, n):

    """
    Plot the average population in areas with bedrooms greater than n.

    Args:
    - data (numpy.ndarray): Input data.
    - n (int): Number of bedrooms threshold.
    """

    bedrooms_gt_n = data[data[:, 4] > n]
    avg_population_bedrooms_gt_n = np.mean(bedrooms_gt_n[:, 5])

    plt.figure(figsize=(8, 6))
    plt.bar([f'Avg Pop. in Bedrooms > {n}'], [avg_population_bedrooms_gt_n], 
            color='lightgreen')
    plt.title(f'Average Population in Areas with Bedrooms > {n}')
    plt.ylabel('Population')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_income_density_bar(labels, values):

    """
    Plot income mean vs average population in high density households.

    Args:
    - labels (list): List of labels for the bars.
    - values (list): Corresponding values for the bars.
    """

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.bar(labels, values, color=['skyblue', 'lightgreen'])
    plt.title('Income Mean and Avg Pop. in High Density Households')
    plt.ylabel('Values')
    plt.tight_layout()
    plt.show()

def plot_avg_house_value_bedrooms_gt_n(data, n):

    """
    Plot the average house value in areas with bedrooms greater than n.

    Args:
    - data (numpy.ndarray): Input data.
    - n (int): Number of bedrooms threshold.
    """

    bedrooms_gt_n = data[data[:, 4] > n]
    avg_house_value_bedrooms_gt_n = np.mean(bedrooms_gt_n[:, 8])

    plt.figure(figsize=(8, 6))
    plt.bar([f'Avg House Value in Bedrooms > {n}'], [avg_house_value_bedrooms_gt_n], 
            color='orange')
    plt.title(f'Average House Value in Areas with Bedrooms > {n}')
    plt.ylabel('Avg House Value')
    plt.xticks(rotation=45)
    plt.ylim(0, max(avg_house_value_bedrooms_gt_n * 1.2, 400000))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_income_vs_bedrooms(unique_bedrooms, avg_income_by_bedrooms):

    """
    Plot average income vs total bedrooms.

    Args:
    - unique_bedrooms (numpy.ndarray): Unique values of total bedrooms.
    - avg_income_by_bedrooms (numpy.ndarray): Average income corresponding
      to each unique total bedrooms value.
    """

    plt.figure(figsize=(10, 6))
    plt.scatter(unique_bedrooms, avg_income_by_bedrooms, marker='o', color='blue', 
                alpha=0.7)
    plt.title('Average Income vs. Total Bedrooms')
    plt.xlabel('Total Bedrooms')
    plt.ylabel('Average Income')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_frequency(column_names, data):

    """
    Plot frequency vs attribute relation for every attribute

    Args:
    - column_names (list): List of column names.
    - data (numpy.ndarray): Input data.
    """

    plt.figure(figsize=(15, 20))

    for i, column in enumerate(column_names):
        plt.subplot(len(column_names) // 3 + 1, 3, i + 1)
        plt.hist(data[:, i], bins=30, edgecolor='black')
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.grid(True)

    plt.tight_layout()
    plt.show()

def plot_statistics_bar(column_names, data):

    """
    Plot bar charts for statistical operations (min, max, median, mean) 
    of selected attributes.

    Args:
    - column_names (list): List of column names.
    - data (numpy.ndarray): Input data.
    """

    selected_data = data[:, [3,5,6,7]]
    stats_min = np.min(selected_data, axis=0)
    stats_max = np.max(data[:, [3,4,5,6]], axis=0)
    stats_median = np.median(data[:, :-2], axis=0)
    stats_mean = np.mean(data[:, :-2], axis=0)

    fig, axs = plt.subplots(4, 1, figsize=(10, 20))

    axs[0].bar(['Total rooms per area', 'Population', 'household', 'median income'],
                stats_min, color='blue', alpha=0.7)
    axs[0].set_title('Minimum Values')
    axs[0].set_ylabel('Value')

    axs[1].bar(['Total rooms per area', 'Population', 'household', 'median income'], 
               stats_max, color='green', alpha=0.7)
    axs[1].set_title('Maximum Values')
    axs[1].set_ylabel('Value')

    axs[2].bar(column_names[:-2], stats_median, color='orange', alpha=0.7)
    axs[2].set_title('Median Values')
    axs[2].set_ylabel('Value')

    axs[3].bar(column_names[:-2], stats_mean, color='red', alpha=0.7)
    axs[3].set_title('Mean Values')
    axs[3].set_ylabel('Value')

    plt.tight_layout()
    plt.show()


