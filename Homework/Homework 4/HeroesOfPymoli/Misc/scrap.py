#aa = pd.cut(age_gender_unique_df["Age"], bins, labels=group_names)

hp_bins = [0, 9, 14, 19, 24, 29, 34, 39, 100]
hp_labels = ["<10", "10-14", "15-19", "20-24","25-29","30-34", "30-35", "40+"]

# Bin the Horsepower column
# cut() returns a Pandas Series containing each of the binned column"s values translated into their corresponding bins

age_gender_unique_df["age ranges"] = pd.cut(purchase_data_unique_SN["Age"], hp_bins, labels=hp_labels)
age_gender_unique_df
grouped_age_gender_unique_df = age_gender_unique_df.groupby("age ranges")
grouped_age_gender_unique_df[["Age"]].count()
first_column_df = pd.DataFrame(grouped_age_gender_unique_df[["Age"]].count())
#create ned df with second column, percentages
calute_percent_df = 100*(first_column_df)/Total_Players

df_merged = first_column_df.merge(calute_percent_df, how="outer", left_index=True, right_index=True)
df_merged

df_merged = df_merged.rename(columns={"Age_x":"Total Count", "Age_y":"Percentage of Players"})

df_merged["Percentage of Players"] = df_merged["Percentage of Players"].apply("{:,.2f}".format)
df_merged