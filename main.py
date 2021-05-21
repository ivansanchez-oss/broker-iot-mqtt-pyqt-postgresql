import sys
import json
from modules import *


class MainWindow(QMainWindow):
    def __init__(self):

        #parametros basicos
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(QSize(500,550))

        #cargar datos guardados
        UIFunctions.load(self)

        #funciones UI
        UIFunctions.addMenu(self)
        UIFunctions.selectStandardMenu(self)
        UIFunctions.addCircular(self)
        UIFunctions.addCheck(self)
        UIFunctions.buttonsFunctions(self)
        self.loadData()

        #CircularProgress
        def timeout():
            self.changeValue(int(humidityList[0]),int(temperatureList[0]))

        timer = QTimer(self)
        timer.timeout.connect(timeout)
        timer.start(1000)

        #mover ventana
        def moveWindow(event):
            UIFunctions.move(event,self)
        self.ui.frame_title.mouseMoveEvent = moveWindow

        #mostrar
        self.show()

    def loadData(self):
        con = psycopg2.connect(host =data['host'],database = data['database'],user=data['user'],password=data['password'])
        cur = con.cursor()
        cur.execute('select '+data['columns']+" from "+ data['table']+ " ORDER BY date DESC;")
        rows = cur.fetchall()
        tableRow = 1
        for r in rows:
            #print(f"temperature: {r[0]} humidity: {r[1]} date: {r[2]}")
            self.ui.table_sql.setItem(tableRow,0,QTableWidgetItem(str(r[0])))
            self.ui.table_sql.setItem(tableRow,1,QTableWidgetItem(str(r[1])))
            self.ui.table_sql.setItem(tableRow,2,QTableWidgetItem(str(r[2])))
            tableRow = tableRow + 1
        cur.close()
        con.close()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def pages(self):
        #cambiar paginas
        UIFunctions.changePage(self)

    def changeValue(self,value_1,value_2):
        #cambiar valor progres circular
        if(self.ui.toggle.isChecked()):
            self.ui.progress.set_value(value_1)
        else:
            self.ui.progress.set_value(0)

        if(self.ui.toggle_2.isChecked()):
            self.ui.progress_2.set_value(value_2)
        else:
            self.ui.progress_2.set_value(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
