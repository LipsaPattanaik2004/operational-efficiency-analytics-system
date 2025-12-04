# Operational Efficiency Analytics System using SQL, Power BI, Azure & Snowflake
__________________________________________________________________________________
This project demonstrates an end-to-end analytics workflow designed to simulate manufacturing operational data, clean and transform it using SQL, model KPIs, visualize insights in Power BI, and automate reporting using Azure & Power Automate.

# LIPSA PATTANAIK | ITER SOA UNIVERSITY

## Features
________________________________________________________________________________________________
- Data simulation for production, downtime, and energy usage
- SQL-based modeling and KPI transformation
- Power BI dashboards for production, downtime, and energy insights
- Azure Data Factory pipeline structure for automated ingestion
- Power Automate workflow for daily KPI email alerts

## Repository Structure
_____________________________________________________________________
- `data/` — sample datasets + generator script  
- `sql/` — table creation + transformation queries  
- `powerbi/` — DAX measures + dashboard layout  
- `azure/` — ADF pipeline instructions  
- `powerplatform/` — Power Automate flow description  
- `docs/` — architecture + interview notes  

## Quick Start
_______________________________________________
```bash
python data/generate_data.py --rows 1000

