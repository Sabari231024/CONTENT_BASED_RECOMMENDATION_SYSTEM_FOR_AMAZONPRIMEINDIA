import pandas as pd
import time

# Function to save DataFrame to CSV with retry mechanism
def save_csv_with_retry(df, filepath, max_attempts=5, retry_delay=1):
    for attempt in range(max_attempts):
        try:
            df.to_csv(filepath, index=False)
            print("CSV file saved successfully.")
            return True
        except PermissionError:
            print(f"Permission denied. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
    print("Failed to save CSV file.")
    return False

# Load the CSV data file
df = pd.read_csv(r'D:\ML\updated_dataset.csv')

# Initial grouping columns containing all categories
grouping_columns = ['genre', 'directors', 'type', 'season', 'release_year', 'moods', 'starring']

# Iterate through grouping columns
for col_to_remove in grouping_columns:
    # Copy original DataFrame
    grouped_df = df.copy()
    # Remove one column
    grouping_columns_without_col = [col for col in grouping_columns if col != col_to_remove]
    # Group by combinations of grouping columns and calculate average IMDb rating
    grouped_ratings = grouped_df.groupby(grouping_columns_without_col)['imdb_rating'].mean().reset_index()

    # Iterate through rows with missing IMDb ratings
    for index, row in grouped_df[grouped_df['imdb_rating'].isnull()].iterrows():
        # Find corresponding group in grouped_ratings
        group = grouped_ratings
        for col in grouping_columns_without_col:
            group = group[group[col] == row[col]]
        # If group exists and has non-null rating, fill missing value
        if not group.empty and not pd.isnull(group['imdb_rating'].iloc[0]):
            df.at[index, 'imdb_rating'] = group['imdb_rating'].iloc[0]

# Save the updated DataFrame back to CSV with retry mechanism
save_csv_with_retry(df, 'AMZRECOMM_dataset.csv')
