CREATE OR REPLACE VIEW vw_daily_production AS
SELECT
  CAST(timestamp AS DATE) AS day,
  shift,
  machine_id,
  SUM(units_produced) AS total_units,
  SUM(defects) AS total_defects
FROM production_records
GROUP BY day, shift, machine_id;

CREATE OR REPLACE VIEW vw_downtime AS
SELECT
  CAST(timestamp AS DATE) AS day,
  machine_id,
  SUM(downtime_minutes) AS downtime_minutes
FROM machine_logs
GROUP BY day, machine_id;

CREATE OR REPLACE VIEW vw_energy AS
SELECT
  CAST(timestamp AS DATE) AS day,
  meter_id,
  SUM(kwh) AS total_kwh
FROM energy_readings
GROUP BY day, meter_id;
