import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Fill missing values
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['duration'].fillna('Unknown', inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].fillna(pd.Timestamp('1900-01-01'))


# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize text format
df.columns = df.columns.str.lower().str.strip()
df['country'] = df['country'].str.title().str.strip()
df['type'] = df['type'].str.capitalize().str.strip()

# Fix data types
df['release_year'] = df['release_year'].astype('Int64')

# Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("✅ Cleaning completed successfully!")
print("Shape after cleaning:", df.shape)
print(df.isnull().sum())
