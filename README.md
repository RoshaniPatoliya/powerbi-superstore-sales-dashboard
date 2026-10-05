# 📊 Executive Sales & Performance Dashboard (Power BI)

An end-to-end business intelligence solution built to monitor retail performance, profitability trends, and regional sales distribution using PostgreSQL and Power BI.



## 🚀 Project Overview
This project simulates an executive-level analytics dashboard for a global retail superstore. The goal was to transform raw, transactional database records into a clean, modern, and interactive decision-making tool. 

The dashboard features a top-level KPI row for immediate performance tracking, chronological trend analysis, category-level profitability breakdowns, and dynamic regional filtering.



## 🛠️ Tech Stack & Skills Demonstrated
**Database & Extraction:** PostgreSQL (`public.superstore_sales`)
**Data Transformation:** Power Query (Data cleaning, type casting, regional locale handling for dates)
**Modeling & DAX:** Custom calculated measures (`Total Sales`, `Total Profit`, `Profit Margin`, `Total Orders`)
**Data Visualization:** Power BI Desktop (Executive design principles, custom card formatting, date hierarchies, and slicer UX)



## 📈 Key Features & Dashboard Layout
1. **Executive KPI Row:** High-level summary cards displaying core business metrics (`Total Sales`, `Total Profit`, `Profit Margin`, and `Total Orders`) with a clean, modern aesthetic.
2. **Monthly Sales Trend (Line Chart):** Visualizes revenue over time utilizing Power BI's automatic date hierarchy (Year/Month/Day) to track seasonal patterns.
3. **Profit by Product Category (Bar Chart):** Highlights top-performing and underperforming merchandise categories ranked by profitability.
4. **Interactive Region Slicer:** Enables stakeholders to dynamically filter the entire canvas by geographic region (East, West, Central, South) for granular analysis.


## ⚙️ Engineering Highlights & Challenges Solved
**Robust Date Modeling:** Resolved raw data type constraints from PostgreSQL by transforming text date strings into true `Date` data types using Power Query's *Using Locale* configuration, unlocking seamless chronological analysis.
**Executive UI/UX Design:** Implemented a soft custom canvas background with card containers, strategic whitespace, and clear typographic hierarchy to eliminate visual clutter and emphasize actionable insights.




