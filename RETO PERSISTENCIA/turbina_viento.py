from influxdb import InfluxDBClient
from datetime import datetime
import pandas as pd
# Configuración de la conexión a la base de datos InfluxDB
host = 'localhost'
port = 8086
user = 'xabitelle'
token = 'Jlx8nb9Vu0uDMPxcLLLPEr0u9Szg7M5a9_QOaTMYqx-IMeF9Mmt8KEQ1STYHGWKsHXKBSVmbtEIFPIRgKx-dBg=='
database = 'viento'

client = InfluxDBClient(host, port, user, token, database)

data = pd.read_csv("T1.csv")

for index, row in data.iterrows():

    timestamp, LV_ActivePower, Wind_Speed, Theoretical_Power_Curve, Wind_Direction = row

    json_payload = []
    data = {
        "measurement": "stocks",
        "tags": {
            "ticker": "turbina"
        },
        "time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "fields": {
            'LV_ActivePower': LV_ActivePower,
            'Wind_Speed': Wind_Speed,
            'Theoretical_Power_Curve':Theoretical_Power_Curve,
            'Wind_Direction': Wind_Direction,
        }
    }
    json_payload.append(data)

    client.write_points(json_payload)

