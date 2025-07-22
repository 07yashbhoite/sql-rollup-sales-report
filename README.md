# Sales Report Generation Using SQL ROLLUP

This project demonstrates how to generate summarized sales reports using the SQL `ROLLUP` operator. The report includes total sales grouped by region, product, and time.

## Technologies Used
- MySQL / SQL Server
- Python (optional for automation)
- SQL ROLLUP operator
- Git

## How It Works
1. Sample sales dataset is stored in a SQL table.
2. ROLLUP is used to create subtotals and grand totals.
3. Data is optionally exported into PDF or DOCX reports.
4. Charts can be generated for visual reporting.

## Example Query
```sql
SELECT region, product, SUM(amount) AS total_sales
FROM sales
GROUP BY ROLLUP(region, product);
