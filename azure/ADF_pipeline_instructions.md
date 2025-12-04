# Azure Data Factory Pipeline Instructions

## Steps:
1. Create Linked Services  
   - Azure Blob Storage  
   - Snowflake / Azure SQL  

2. Build Pipeline:
   - Copy Activity: Blob → SQL table  
   - Script Activity: Run transformations.sql  

3. Schedule with Trigger: Daily at 02:00  

4. Optional:
   - Use Snowpipe for auto-ingestion  
