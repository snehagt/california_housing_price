import numpy as np
import analysis
import plot

def main():

    """
    Main function to run the program. Provides a menu-driven interface 
    for dataset analysis and visualization.

    Parameters:
    None

    Returns:
    None
    """

    filename = 'data/housing.csv'
    data, column_names = analysis.load_data(filename)

    # if data is not None and column_names is not None:
    #     data = analysis.remove_missing_values(data)

    while True:
        print('\nChoose Your Operation: ')
        print("\nMenu:")
        print("1. Display Dataset - Preview")
        print("2. Show Column Names")
        print("3. Show Basic Information")
        print("4. Show and remove Missing Values or null values")
        print("5. Statistics: for all attributes in our dataset")
        print("6. Generalized Analysis")
        print("7. Visualizations")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            analysis.display_dataset_preview(data, column_names)

        elif choice == '2':
            analysis.show_column_names(filename)

        elif choice == '3':
            analysis.show_basic_info(data)

        elif choice == '4':
            analysis.show_missing_values(data, filename)
            analysis.remove_missing_values(data)
            print('Successfully removed missing values')

        elif choice == '5':
            # Calculate missing value statistics
            column_names = analysis.show_column_names(filename)
            analysis.calculate_statistics(data, column_names)

        elif choice == '6':
            # Generalized Analysis submenu
            while True:
                print('\nChoose Analytical Operation: ')
                print("1. Income Mean")
                print("2. Average Population in Areas with Bedrooms > n")
                print("3. Average House Value in Areas with Bedrooms > n")
                print("4. Average Income in Areas with Bedrooms > n")
                print("5. Average Income of People with More Than 3 Rooms per Household")
                print("6. Average Population in Households with High Density (> 1000)")
                print("7. Average House Value in Households with High Density (> 1000)")
                print("8. Relation between Total Number of Bedrooms by Average Income - GRAPH")
                print("9. Relation between Statistical Operations of All Attributes - GRAPH")
                print("10. Back to Main Menu")

                choice = input("\nEnter your choice (1-10): ")

                if choice == '1':
                    income_mean = analysis.calculate_income_mean(data)
                    print(f"\nIncome Mean: {income_mean}")

                elif choice in ['2', '3', '4']:
                    n = int(input('Enter the number of bedrooms to check: '))
                    if choice == '2':
                        avg_population_bedrooms_gt_n = analysis.calculate_avg_population_bedrooms_gt_n(data, n)
                        print(f"\nAverage Population in Areas with Bedrooms > {n} : \
                              {avg_population_bedrooms_gt_n}")
                    elif choice == '3':
                        avg_house_value_bedrooms_gt_n = analysis.calculate_avg_house_value_bedrooms_gt_n(data, n)
                        print(f"\nAverage House Value in Areas with Bedrooms > {n}: \
                              {avg_house_value_bedrooms_gt_n}")
                    elif choice == '4':
                        avg_income_bedrooms_gt_n = analysis.calculate_avg_income_bedrooms_gt_n(data, n)
                        print(f"""\nAverage Income in Areas with Bedrooms > {n}:
                              {avg_income_bedrooms_gt_n}""")

                elif choice == '5':
                    avg_income_rooms_gt_3 = analysis.calculate_avg_income_rooms_gt_3(data)
                    print(f"\nAverage Income of People with More Than 3 Rooms per Household: \
                          {avg_income_rooms_gt_3}")

                elif choice == '6':
                    avg_population_high_density = analysis.calculate_avg_population_high_density(data)
                    print(f"\nAverage Population in Households with High Density (> 1000): \
                          {avg_population_high_density}")

                elif choice == '7':
                    avg_house_value_high_density = analysis.calculate_avg_house_value_high_density(data)
                    print(f"\nAverage House Value in Households with High Density (> 1000): \
                          {avg_house_value_high_density}")

                elif choice == '8':
                    unique_bedrooms, avg_income_by_bedrooms = analysis.average_income_by_bedrooms(data)
                    plot.plot_income_vs_bedrooms(unique_bedrooms, avg_income_by_bedrooms)

                elif choice == '9':
                    plot.plot_statistics_bar(column_names, data)

                elif choice == '10':
                    break

                else:
                    print("Invalid choice. Please enter a number from 1 to 10.")

        elif choice == '7':
            # Visualization submenu
            while True:
                print('\nChoose Visualization: ')
                print("1. Plot Income Mean")
                print("2. Plot Average Population in Areas with Bedrooms > n")
                print("3. Plot Average House Value in Areas with Bedrooms > n")
                print("4. Plot Income Mean vs Average Population")
                print("5. Plot Frequencies of Data for summary analysis")
                print("6. Plot Relation between Total Number of Bedrooms by Average Income")
                print("7. Plot Relation between Statistical Operations of All Attributes")
                print("8. Plot Income vs Population for Areas with Income > n")
                print("9. Back to Main Menu")

                choice = input("\nEnter your choice (1-8): ")

                if choice == '1':
                    income_mean = analysis.calculate_income_mean(data)
                    plot.plot_income_mean(income_mean)

                elif choice in ['2', '3']:
                    n = int(input('Enter the number of bedrooms to check: '))
                    if choice == '2':
                        plot.plot_avg_population_bedrooms_gt_n(data, n)
                    elif choice == '3':
                        plot.plot_avg_house_value_bedrooms_gt_n(data, n)

                elif choice == '4':
                    income_mean = analysis.calculate_income_mean(data)
                    avg_population_high_density = analysis.calculate_avg_population_high_density(data)
                    labels = ['Income Mean', 'Avg Pop. in High Density Households']
                    values = [income_mean, avg_population_high_density]
                    plot.plot_income_density_bar(labels, values)

                elif choice == '5':
                    plot.plot_frequency(column_names, data)

                elif choice == '6':
                    unique_bedrooms, avg_income_by_bedrooms = analysis.average_income_by_bedrooms(data)
                    plot.plot_income_vs_bedrooms(unique_bedrooms, avg_income_by_bedrooms)

                elif choice == '7':
                    plot.plot_statistics_bar(column_names, data)

                elif choice == '8':
                        column_names = analysis.show_column_names(filename)
                        print('Median Income', data[:5, -3])
                        income_threshold = float(input('Enter the income threshold: '))
                        plot.plot_income_population(data, income_threshold)

                elif choice == '9':
                    break

                else:
                    print("Invalid choice. Please enter a number from 1 to 9.")

        elif choice == '8':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()
