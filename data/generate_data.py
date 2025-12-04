import argparse, random, csv, json, datetime
from pathlib import Path

def gen_machine_logs(n):
    rows = []
    base = datetime.datetime.now() - datetime.timedelta(days=30)
    machines = [f'MACH_{i:03d}' for i in range(1,11)]
    reasons = ['Maintenance','Operator Error','Power Failure','Mechanical','Unknown']
    for i in range(n):
        t = base + datetime.timedelta(minutes=15*i)
        rows.append({
            'timestamp': t.strftime('%Y-%m-%d %H:%M:%S'),
            'machine_id': random.choice(machines),
            'downtime_minutes': random.choice([0,0,0,5,10,15,30,60]),
            'reason': random.choice(reasons)
        })
    return rows

def gen_production_records(n):
    rows = []
    base = datetime.datetime.now() - datetime.timedelta(days=30)
    shifts = ['A','B','C']
    for i in range(n):
        t = base + datetime.timedelta(minutes=30*i)
        rows.append({
            'timestamp': t.strftime('%Y-%m-%d %H:%M:%S'),
            'shift': random.choice(shifts),
            'machine_id': f'MACH_{random.randint(1,10):03d}',
            'units_produced': random.randint(0,50),
            'defects': random.randint(0,5)
        })
    return rows

def gen_energy_readings(n):
    rows = []
    base = datetime.datetime.now() - datetime.timedelta(days=30)
    for i in range(n):
        t = base + datetime.timedelta(minutes=60*i)
        rows.append({
            'timestamp': t.strftime('%Y-%m-%d %H:%M:%S'),
            'meter_id': f'MTR_{random.randint(1,5):03d}',
            'kwh': round(random.uniform(0.5, 20.0),2)
        })
    return rows

def main(rows):
    data_dir = Path(__file__).parent
    ml = gen_machine_logs(rows)
    pr = gen_production_records(rows//2)
    er = gen_energy_readings(rows//4)

    # save files
    with open(data_dir / 'machine_logs.csv','w',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=ml[0].keys())
        writer.writeheader()
        writer.writerows(ml)

    with open(data_dir / 'production_records.csv','w',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=pr[0].keys())
        writer.writeheader()
        writer.writerows(pr)

    with open(data_dir / 'energy_readings.json','w') as f:
        json.dump(er, f, indent=2)

    print("Generated datasets successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--rows', type=int, default=1000)
    args = parser.parse_args()
    main(args.rows)
