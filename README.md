# Operational Efficiency Analytics System
_________________________________
An end-to-end analytics solution designed to simulate manufacturing operational data, transform it using SQL, model KPIs, and visualize actionable insights using Power BI. The system also demonstrates automated data ingestion and reporting workflows using Azure services.

## Overview
______________________
- Manufacturing operations generate large volumes of production, downtime, and energy usage data. This project showcases how raw operational data can be transformed into meaningful KPIs and dashboards to support data-driven decision-making and operational efficiency improvements.
- The solution follows a structured analytics workflow including data generation, SQL-based transformation, dashboarding, and automation.

## Tech Stack
________________________________________
SQL, Power BI, Azure Data Factory (conceptual), Power Automate, Snowflake, Python

## Key Features
______________________
- Simulated manufacturing data for production output, downtime, and energy consumption
- SQL-based data cleaning, transformation, and KPI modeling
- Interactive Power BI dashboards for operational insights
- Azure Data Factory pipeline structure for automated data ingestion
- Power Automate workflow for scheduled KPI email notifications

## Analytics & KPIs
______________________________
- Production efficiency and output trends
- Downtime analysis and root cause indicators
- Energy usage patterns and optimization insights
- Daily and periodic operational performance metrics

## Repository Structure
______________________
- `data/` — Sample datasets and data generation scripts  
- `sql/` — SQL table creation and transformation queries  
- `powerbi/` — Power BI dashboards and DAX measures  
- `azure/` — Azure Data Factory pipeline documentation  
- `powerplatform/` — Power Automate workflow documentation  
- `docs/` — Architecture diagrams and interview reference notes  

## Workflow
____________________________________
1. Generate or ingest operational data  
2. Clean and transform data using SQL  
3. Model KPIs for production, downtime, and energy usage  
4. Visualize insights in Power BI dashboards  
5. Automate data refresh and reporting using Azure services  

## How to Run
_________________________________
1. Clone the repository  
2. Generate sample data:
   ```bash
   python data/generate_data.py --rows 1000

# LIPSA PATTANAIK | ITER, SOA UNIVERSITY
