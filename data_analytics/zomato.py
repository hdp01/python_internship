import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_dataset(file_path):
    print("Loading dataset...")
    dataframe = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
    return dataframe

# Handle 'rate' column
def handle_rate_column(dataframe):
    print("Handling 'rate' column...")
    dataframe['rate'] = dataframe['rate'].apply(lambda x: float(str(x).split('/')[0]))
    print("Handled 'rate' column successfully!")
    return dataframe

# Display dataset information
def display_dataset_info(dataframe):
    print("Dataset Information:")
    print(dataframe.info())
    print("--------------------------------------------------")

# Plot countplot for 'listed_in(type)'
def plot_type_count(dataframe):
    print("Plotting countplot for 'listed_in(type)'...")
    plt.figure(figsize=(8, 6))
    sns.countplot(x=dataframe['listed_in(type)'])
    plt.xlabel("Type of Restaurant", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.title("Count of Restaurants by Type", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("Plot displayed successfully!")
    print("--------------------------------------------------")

# Plot grouped bar plot for 'votes' by 'listed_in(type)'
def plot_votes_by_type(dataframe):
    print("Plotting grouped bar plot for 'votes' by 'listed_in(type)'...")
    grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='listed_in(type)', y='votes', data=grouped_data, palette='muted')
    plt.xlabel("Type of Restaurant", fontsize=12)
    plt.ylabel("Total Votes", fontsize=12)
    plt.title("Total Votes by Type of Restaurant", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("Plot displayed successfully!")
    print("--------------------------------------------------")

# Find restaurant(s) with maximum votes
def find_max_votes_restaurant(dataframe):
    print("Finding restaurant(s) with maximum votes...")
    max_votes = dataframe['votes'].max()
    restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
    print("Restaurant(s) with the maximum votes:")
    print(restaurant_with_max_votes)
    print("--------------------------------------------------")

# Plot countplot for 'online_order'
def plot_online_order_count(dataframe):
    print("Plotting countplot for 'online_order'...")
    plt.figure(figsize=(6, 4))
    sns.countplot(x=dataframe['online_order'], palette='Set2')
    plt.xlabel("Online Order Availability", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.title("Count of Restaurants by Online Order Availability", fontsize=14)
    plt.tight_layout()
    plt.show()
    print("Plot displayed successfully!")
    print("--------------------------------------------------")

# Plot histogram for 'rate'
def plot_rate_histogram(dataframe):
    print("Plotting histogram for 'rate'...")
    plt.figure(figsize=(8, 6))
    plt.hist(dataframe['rate'], bins=10, color='skyblue', edgecolor='black')
    plt.xlabel("Rating", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.title("Distribution of Ratings", fontsize=14)
    plt.tight_layout()
    plt.show()
    print("Plot displayed successfully!")
    print("--------------------------------------------------")

# Plot countplot for 'approx_cost(for two people)'
def plot_approx_cost_count(dataframe):
    print("Plotting countplot for 'approx_cost(for two people)'...")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='approx_cost(for two people)', data=dataframe, palette='pastel')
    plt.xlabel("Approx Cost (for Two People)", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.title("Count of Restaurants by Approx Cost (for Two People)", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    print("Plot displayed successfully!")
    print("--------------------------------------------------")

# Plot boxplot for 'rate' by 'online_order'
def plot_rate_boxplot(dataframe):
    print("Plotting boxplot for 'rate' by 'online_order'...")
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='online_order', y='rate', data=dataframe, palette='Set3')
    plt.xlabel("Online Order Availability", fontsize=12)
    plt.ylabel("Rating", fontsize=12)
    plt.title("Distribution of Ratings by Online Order Availability", fontsize=14)
    plt.tight_layout()
    plt.show()
    print("Plot displayed successfully!")
    print("--------------------------------------------------")

def main():
    file_path = r"C:\Users\LENOVO\Downloads\Zomato data .csv"
    dataframe = load_dataset(file_path)
    dataframe = handle_rate_column(dataframe)
    display_dataset_info(dataframe)
    plot_type_count(dataframe)
    plot_votes_by_type(dataframe)
    find_max_votes_restaurant(dataframe)
    plot_online_order_count(dataframe)
    plot_rate_histogram(dataframe)
    plot_approx_cost_count(dataframe)
    plot_rate_boxplot(dataframe)

if __name__ == "__main__":
    main()