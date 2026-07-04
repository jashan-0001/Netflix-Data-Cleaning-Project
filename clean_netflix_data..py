import pandas as pd
from datetime import datetime

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/netflix_movies1.csv")

print("Original Shape:", df.shape)

# -----------------------------
# Standardize Column Names
# -----------------------------
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
)

# -----------------------------
# Remove Duplicate Rows
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# Remove Extra Spaces
# -----------------------------
for col in df.select_dtypes(include="object"):
    df[col] = df[col].astype(str).str.strip()

# -----------------------------
# Replace Missing Values
# -----------------------------
df["director"] = df["director"].replace("nan", "Unknown")
df["cast"] = df["cast"].replace("nan", "Not Available")
df["country"] = df["country"].replace("nan", "Unknown")
df["rating"] = df["rating"].replace("nan", "Not Rated")
df["duration"] = df["duration"].replace("nan", "Unknown")

# Remove rows with missing title
df = df[df["title"] != "nan"]

# -----------------------------
# Format Date
# -----------------------------
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# Create year_added column
df["year_added"] = df["date_added"].dt.year

# Format date
df["date_added"] = df["date_added"].dt.strftime("%Y-%m-%d")
df["date_added"] = df["date_added"].fillna("")

# -----------------------------
# Standardize Text
# -----------------------------
df["type"] = df["type"].str.title()
df["country"] = df["country"].str.title()

# -----------------------------
# Create Content Age
# -----------------------------
current_year = datetime.now().year
df["content_age"] = current_year - df["release_year"]

# -----------------------------
# Rename Columns
# -----------------------------
df.rename(columns={
    "listed_in": "genre"
}, inplace=True)

# -----------------------------
# Arrange Columns
# -----------------------------
columns = [
    "show_id",
    "type",
    "title",
    "director",
    "cast",
    "country",
    "date_added",
    "year_added",
    "release_year",
    "content_age",
    "rating",
    "duration",
    "genre",
    "description"
]

df = df[columns]

# -----------------------------
# Sort Dataset
# -----------------------------
df = df.sort_values(by=["title"])

# -----------------------------
# Save Final Dataset
# -----------------------------
df.to_csv("data/Netflix_Final_Cleaned.csv", index=False)

print("\nCleaning Completed Successfully!")
print("Final Shape:", df.shape)
print("File Saved As: Netflix_Final_Cleaned.csv")