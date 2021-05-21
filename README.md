# Broker-IOT-MQTT-PYQT-POSTGRESQL
MQTT broker that receives all the messages from a greenhouse and then displays them graphically while sending the data to a PostgreSQL database.


Requirements: Mosquitto, paho-mqtt,PySide6,PyQt5,Psycopg2.

Requirements SQL: have a database in postgres and a table inside the posgres public schema with three columns, names indicated and editable in json, the data table is a timestamp without time zone and it is mandatory that it has the same name and the same type


