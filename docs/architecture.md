# Architecture Overview

Raw Data → Azure Blob → ADF Pipeline → Snowflake/Azure SQL  
→ SQL Transformations → Power BI Dashboards → Power Automate Email Alerts

Components:
- Azure Data Factory for automated ingestion
- Snowflake/Azure SQL for storage & modeling
- Power BI for visualization
- Power Automate for reporting automation
