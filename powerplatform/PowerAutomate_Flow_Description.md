# Power Automate: Daily KPI Email Flow

## Steps:
1. Trigger: Recurrence — Daily 8 AM  
2. Action: Get rows from SQL view vw_daily_production  
3. Compose HTML summarizing KPIs  
4. Send Email:
   Subject: "Daily Operational KPIs"  
   Body: KPI summary + Power BI link  
