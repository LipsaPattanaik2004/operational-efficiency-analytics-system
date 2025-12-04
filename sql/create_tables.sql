CREATE TABLE machine_logs (
  timestamp TIMESTAMP,
  machine_id VARCHAR(50),
  downtime_minutes INT,
  reason VARCHAR(100)
);

CREATE TABLE production_records (
  timestamp TIMESTAMP,
  shift VARCHAR(5),
  machine_id VARCHAR(50),
  units_produced INT,
  defects INT
);

CREATE TABLE energy_readings (
  timestamp TIMESTAMP,
  meter_id VARCHAR(50),
  kwh FLOAT
);
