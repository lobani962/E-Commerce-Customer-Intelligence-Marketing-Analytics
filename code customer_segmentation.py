import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 1. Load the cleaned Excel file
file_path = "sampled_product_sales_50000 - AFTER.csv"
df = pd.read_csv(r"C:\GOOD STUFF\UNIVERSITY\YEAR 3\SCOND TERM\BUSINESS ANALYTICS\business analytics project\sampled_product_sales_50000 - AFTER.csv")

# 2. Clean column names just in case
df.columns = df.columns.str.strip()

# 3. Create customer-level data
customer_df = df.groupby("Customer_Name").agg({
    "Revenue": "sum",
    "Profit": "sum",
    "Order_ID": "nunique",
    "Quantity": "sum"
}).reset_index()

# 4. Rename columns
customer_df.rename(columns={
    "Revenue": "Total_Revenue",
    "Profit": "Total_Profit",
    "Order_ID": "Number_of_Orders",
    "Quantity": "Total_Quantity"
}, inplace=True)

# 5. Add extra customer metrics
customer_df["Average_Order_Value"] = customer_df["Total_Revenue"] / customer_df["Number_of_Orders"]
customer_df["Profit_Margin"] = customer_df["Total_Profit"] / customer_df["Total_Revenue"]

# 6. Select features for clustering
features = [
    "Total_Revenue",
    "Total_Profit",
    "Number_of_Orders",
    "Total_Quantity",
    "Average_Order_Value",
    "Profit_Margin"
]

X = customer_df[features]

# 7. Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 8. Apply KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
customer_df["Cluster"] = kmeans.fit_predict(X_scaled)

# 9. Give business names to clusters
cluster_summary = customer_df.groupby("Cluster")[features].mean()
print("Cluster Summary:")
print(cluster_summary)

# Optional: manually name clusters after checking summary
customer_df["Customer_ML_Segment"] = customer_df["Cluster"].map({
    0: "Low-Value Customers",
    1: "Regular Customers",
    2: "VIP Customers",
    3: "Premium Occasional Customers"
})

# 10. Save result to Excel
customer_df.to_excel("customer_segmentation_results.xlsx", index=False)

print("Done! File saved as customer_segmentation_results.xlsx")

# 11. Simple chart
plt.figure(figsize=(8, 5))
plt.scatter(customer_df["Total_Revenue"], customer_df["Total_Profit"], c=customer_df["Cluster"])
plt.xlabel("Total Revenue")
plt.ylabel("Total Profit")
plt.title("Customer Segmentation using KMeans")
plt.show()