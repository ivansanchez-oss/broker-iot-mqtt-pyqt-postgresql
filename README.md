
# Broker-IOT-MQTT-PYQT-POSTGRESQL
MQTT broker that receives all the messages from a greenhouse and then displays them graphically while sending the data to a PostgreSQL database.


Requirements: Mosquitto, paho-mqtt,PySide6,PyQt5,Psycopg2.

Requirements SQL: have a database in postgres and a table inside the posgres public schema with three columns, names indicated and editable in json, the data table is a timestamp without time zone and it is mandatory that it has the same name and the same type.


![menu](https://user-images.githubusercontent.com/83692003/119083626-e9f86c80-b9c5-11eb-9dc3-949b087cdea9.png)

![MQTT](https://user-images.githubusercontent.com/83692003/119083649-f54b9800-b9c5-11eb-9c4a-8d2092feb248.png)
