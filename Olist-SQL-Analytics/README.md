# Olist E-commerce SQL Analytics

**Status:** In progress

A PostgreSQL portfolio project analysing the Brazilian Olist e-commerce dataset. The goal is to answer business questions about sales, customers, products, sellers, payments, reviews and delivery performance.

## Objectives
- Load and explore a multi-table dataset in PostgreSQL.
- Practise joins, aggregations, CTEs, subqueries and window functions.
- Analyse business performance and communicate actionable insights.
- Build a clean, documented GitHub portfolio project.

## Dataset
Brazilian E-Commerce Public Dataset by Olist. Download the CSV files from the original Kaggle dataset page. Put local files in `data/raw/`. Check the dataset's licence before redistributing any data. Raw data is excluded from Git.

## Repository structure
```text
Olist-SQL-Analytics/
├── data/raw/                 # Local source CSVs (not committed)
├── data/processed/           # Local transformed data (not committed)
├── sql/                      # Ordered SQL scripts
├── docs/                     # Business questions and findings
├── dashboard/                # Dashboard exports/screenshots
├── README.md
└── .gitignore
```

## Planned analysis
1. Monthly orders and payment value
2. Average order value
3. Revenue by product category
4. Customer geography and repeat purchasing
5. Seller performance
6. Late-delivery rate
7. Relationship between delivery performance and review scores
8. Month-over-month trends using window functions

## Tools
PostgreSQL, pgAdmin 4, VS Code, Git and GitHub.

## Setup
1. Create a PostgreSQL database named `olist_analytics`.
2. Download the dataset and place CSV files in `data/raw/`.
3. Confirm the CSV headers and data types.
4. Define tables in `sql/01_schema.sql`.
5. Import the CSV files into PostgreSQL.
6. Execute the SQL scripts in numerical order.

> Schema definitions and query logic will be added after verifying the exact CSV headers. Never commit passwords, connection strings, or private credentials.
