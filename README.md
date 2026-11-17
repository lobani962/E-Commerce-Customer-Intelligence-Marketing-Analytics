# E-Commerce Customer Intelligence & Marketing Analytics

An end-to-end business analytics project using Excel, Power BI, and Python to transform e-commerce sales data into actionable customer and marketing insights.

The project combines interactive dashboards with KMeans customer segmentation to analyze purchasing behavior, identify valuable customers, and support data-driven marketing decisions.

## Project Objectives

- Analyze customer purchasing behavior and sales trends.
- Identify customer segments and high-value customers.
- Evaluate product, category, and regional performance.
- Support targeted marketing strategies with business insights.

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Excel | Data cleaning and transformation |
| Power BI | Interactive dashboards and reporting |
| Python | Customer segmentation and analysis |
| pandas | Data preparation and aggregation |
| scikit-learn | Feature scaling and KMeans clustering |
| Matplotlib | Customer segmentation visualization |

## Dataset

The project uses a cleaned e-commerce dataset containing approximately 50,000 orders.

Main fields include:

- Order ID and order date
- Customer name
- City, state, region, and country
- Product, category, and sub-category
- Quantity and unit price
- Revenue and profit

## Project Workflow

### 1. Data Preparation

Data was cleaned and transformed in Excel to prepare it for analysis.

Tasks included:

- Standardizing column names and checking data types.
- Creating time-related fields for trend analysis.
- Calculating profit margins.
- Adding customer segments and sales levels.
- Creating profit status and product performance indicators.

### 2. Power BI Dashboards

The report includes three main pages:

#### Executive Summary

- Total revenue, profit, orders, and customers.
- Category and regional performance.
- Monthly sales trends.

#### Customer & Marketing Analysis

- Customer segments and revenue contributions.
- Top customers and average order value.
- Regional customer distribution.

#### Product Performance Analysis

- Product and sub-category performance.
- Category profitability.
- Best-selling products by revenue and quantity.

### 3. Customer Segmentation

The Python script aggregates transactions by customer name and calculates six features:

- Total revenue
- Total profit
- Number of unique orders
- Total quantity
- Average order value
- Profit margin

Features are standardized using `StandardScaler`, then grouped into four clusters using `KMeans`.

The script assigns four business labels:

- Low-Value Customers
- Regular Customers
- VIP Customers
- Premium Occasional Customers

These labels are assigned manually and should be checked against the cluster summary when the model is rerun.

## Key Findings

As reported in the project presentation:

| Metric | Value |
|--------|-------|
| Total Revenue | Approximately 35.51 million |
| Total Profit | Approximately 7.85 million |
| Overall Profit Margin | Approximately 22.12% |
| Orders | Approximately 50,000 |
| Customers | Approximately 40,000 |

Additional findings:

- Electronics leads category revenue.
- East generates the highest regional revenue.
- Medium-value customers contribute the highest total revenue.
- Home & Furniture contributes the highest category profit.

## Business Recommendations

- Develop targeted campaigns for different customer segments.
- Use loyalty offers to retain valuable customers.
- Encourage repeat purchases through personalized offers and bundles.
- Prioritize profitable products and best sellers in promotions.
- Use regional performance insights to guide marketing investment.

## Repository Files

| File | Description |
|------|-------------|
| `sampled_product_sales_50000 - AFTER.csv` | Cleaned dataset |
| `busnies project final.pbix` | Interactive Power BI report |
| `code customer_segmentation.py` | Python customer segmentation script |
| `phase4.pptx` | Executive presentation |

## How to Run

### Python Analysis

1. Install the required libraries:

   ```bash
   pip install pandas scikit-learn matplotlib openpyxl
   ```

2. Place the CSV dataset and Python script in the same folder.

3. Replace the hard-coded data loading path in the script with:

   ```python
   file_path = "sampled_product_sales_50000 - AFTER.csv"
   df = pd.read_csv(file_path)
   ```

4. Run the script:

   ```bash
   python "code customer_segmentation.py"
   ```

The script prints cluster summaries, displays a segmentation scatter plot, and exports customer-level results to:

```text
customer_segmentation_results.xlsx
```

### Power BI Report

1. Open `busnies project final.pbix` in Power BI Desktop.
2. Update the data source paths if needed.
3. Explore the dashboard pages and filters.

## Limitations

- Customer names may not uniquely identify individual customers.
- The dataset does not include website activity or campaign interaction history.
- Clustering results depend on the selected features and model settings.
- Cluster numbers require business interpretation before assigning segment labels.
- The analysis supports marketing recommendations but does not measure their actual effectiveness.

## Contributors

- Muntasir Ababneh
- Muntasir Melhem
- Mahmoud Alobani
