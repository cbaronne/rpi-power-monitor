#!/usr/bin/python
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBServerError

# InfluxDB connection settings
client = InfluxDBClient(host='localhost', port=8086, username='root', password='password', database='power_monitor')

client.drop_database("power_monitor")
client.close()
