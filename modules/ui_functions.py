from  main import *
from . ui_styles import Style
import numpy as np
import paho.mqtt.client
import os
import psycopg2
from datetime import datetime
import json

temperatureList = ["0"]
humidityList = ["0"]
listTopics = []
enable = ["False"]


with open('info.json') as f:
    data = json.load(f)

class UIFunctions(MainWindow):

    def load(self):
        self.ui.text_publish.setText(data['host_publish'])
        self.ui.text_publish_topic.setText(data['topic_publish'])

        self.ui.text_subscribe.setText(data['host_subscribe'])
        self.ui.text_topic_subscribe.setText(data["topic_subscribe"])

    def postgres(self):
        con = psycopg2.connect(host = data['host'],database = data['database'],user=data['user'],password=data['password'])
        cur = con.cursor()
        SQL = ("INSERT INTO "+data['table']+"("+data['columns']+") VALUES ("+data['values']+")")
        date = str(datetime.now())
        date = date[:-7]

        send = (humidityList[0],temperatureList[0],str(date))
        cur.execute(SQL, send)
        con.commit()
        cur.close()
        con.close()

    def sendVentilate():
            sendMQTT(data['host_sensores'],data['topic_ventilate'],"on_ventilate")

    def sendSpray():
            sendMQTT(data['host_sensores'],data['topic_spray'],"on_spray")


    def send(self):
        host = self.ui.text_publish.toPlainText()
        topic = self.ui.text_publish_topic.toPlainText()
        message = self.ui.text_publish_message.toPlainText()

        data['host_publish'] = host
        data['topic_publish'] = topic

        with open('info.json','w') as f:
            json.dump(data,f, indent = 2)

        if(message == "" or host == "" or topic == ""):
            print("Rellene todos los campos")
        else:
            sendMQTT(host,topic,message)
            print("Enviado")

    def subscribe(self):
        self.ui.toggle.setChecked(True)
        self.ui.toggle_2.setChecked(True)
        host = self.ui.text_subscribe.toPlainText()
        topic = self.ui.text_topic_subscribe.toPlainText()
        listTopics.append(topic)

        data['host_subscribe'] = host
        data['topic_subscribe'] = topic

        with open('info.json','w') as f:
            json.dump(data,f, indent = 2)

        if(host == "" or topic == ""):
            print("Rellene todos los campos")
        else:
            try:
                subscribeMQTT(host,"Ivan")
                self.ui.button_status.setStyleSheet("QPushButton{\n""background-color: rgb(49, 127, 67);\n""border-radius:10px}")
            except:
                self.ui.button_status.setStyleSheet("QPushButton{\n""background-color: rgb(205, 164, 52);\n""border-radius:10px}")

    def unsubscribe(self):
        host = self.ui.text_subscribe.toPlainText()
        unsubscribeMQTT(host,"Ivan-Subs")
        self.ui.button_status.setStyleSheet("QPushButton{\n""background-color: rgb(155, 61, 63);\n""border-radius:10px}")





    def addCheck(self):
        #andadir checkbocs
        self.ui.toggle = PyToggle()
        self.ui.frame_humidity_layout.addWidget(self.ui.toggle,Qt.AlignCenter,Qt.AlignCenter)

        self.ui.toggle_2 = PyToggle()
        self.ui.frame_temperature_layout.addWidget(self.ui.toggle_2,Qt.AlignCenter,Qt.AlignCenter)







    def addCircular(self):
        #agregar progreso circular
        self.ui.progress = CircularProgress()
        self.ui.progress.value = 0
        self.ui.progress.add_shadow(True)
        self.ui.progress.setMinimumSize(self.ui.progress.width,self.ui.progress.height)
        self.ui.frame_humidity_layout.addWidget(self.ui.progress,Qt.AlignCenter,Qt.AlignCenter)

        self.ui.progress_2 = CircularProgress()
        self.ui.progress_2.value = 0
        self.ui.progress_2.add_shadow(True)
        self.ui.progress_2.progress_color = 0xEFB810
        self.ui.progress_2.suffix = "° Grados"
        self.ui.progress_2.setMinimumSize(self.ui.progress.width,self.ui.progress.height)
        self.ui.frame_temperature_layout.addWidget(self.ui.progress_2,Qt.AlignCenter,Qt.AlignCenter)





    def move(event,self):
        #mover ventana
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()





    def buttonsFunctions(self):
        #ocultar barra de windows
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #botones cerrar/minimizar
        self.ui.button_close.clicked.connect(lambda: self.close())
        self.ui.button_minimize.clicked.connect(lambda: self.showMinimized())

        #toggle toggle menu
        self.ui.button_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self,150,True))

        #mqtt
        self.ui.button_subscribe.clicked.connect(lambda: UIFunctions.subscribe(self))
        self.ui.button_unsubscribe.clicked.connect(lambda: UIFunctions.unsubscribe(self))
        self.ui.button_publish.clicked.connect(lambda: UIFunctions.send(self))

        #postgres
        self.ui.button_save.clicked.connect(lambda: UIFunctions.postgres(self))
        self.ui.button_save.clicked.connect(lambda: self.loadData())

        #limpiar
        self.ui.button_clear_publish.clicked.connect(lambda: UIFunctions.clear(self.ui.text_publish_topic))
        self.ui.button_clear_publish.clicked.connect(lambda: UIFunctions.clear(self.ui.text_publish))
        self.ui.button_clear_publish.clicked.connect(lambda: UIFunctions.clear(self.ui.text_publish_message))
        self.ui.button_subscribe_clear.clicked.connect(lambda: UIFunctions.clear(self.ui.text_subscribe))
        self.ui.button_subscribe_clear.clicked.connect(lambda: UIFunctions.clear(self.ui.text_topic_subscribe))

        #botones ventilar y rociar
        self.ui.button_ventilate.clicked.connect(lambda: UIFunctions.sendVentilate())
        self.ui.button_spray.clicked.connect(lambda: UIFunctions.sendSpray())


    def clear(text):
        text.setText("")






    def toggleMenu(self,maxWidth,enable):
        if enable: width = self.ui.frame_left_menu.width(); maxExtend = maxWidth; standard = 70;
        if width == 70: widthExtended = maxExtend
        else: widthExtended = standard

        #animacion
        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    def addMenu(self):
        #agregar botones
        for i in range(0,2):
            font = QFont()
            font.setFamily(u"Segoe UI")
            button = QPushButton("1",self)
            button.setObjectName("button_menu_"+str(i+1))
            sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            sizePolicy3.setHorizontalStretch(0)
            sizePolicy3.setVerticalStretch(0)
            sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
            button.setSizePolicy(sizePolicy3)
            button.setMinimumSize(QSize(0, 50))
            button.setLayoutDirection(Qt.LeftToRight)
            button.setFont(font)
            if i == 0:
                button.setText("Menu")
                button.setStyleSheet(Style.style_button_standard.replace('ICON_REPLACE',"url(:/icons/icons/16x16/cil-home.png)"))
            if i == 1:
                button.setText("MQTT")
                button.setStyleSheet(Style.style_button_standard.replace('ICON_REPLACE',"url(:/icons/icons/16x16/cil-chat-bubble.png)"))
            self.ui.frame_top_menu_layout.addWidget(button)
            button.clicked.connect(self.pages)








    def changePage(self):
        buttonWidget = self.sender()
        if buttonWidget.objectName() == "button_menu_1":
            self.ui.pages_widget.setCurrentWidget(self.ui.page_1)
            UIFunctions.resetStyle(self,"button_menu_1")
            buttonWidget.setStyleSheet(UIFunctions.selectMenu(buttonWidget.styleSheet()))
            self.ui.label_page.setText("PAGE 1")

        if buttonWidget.objectName() == "button_menu_2":
            self.ui.pages_widget.setCurrentWidget(self.ui.page_2)
            UIFunctions.resetStyle(self,"button_menu_2")
            buttonWidget.setStyleSheet(UIFunctions.selectMenu(buttonWidget.styleSheet()))
            self.ui.label_page.setText("PAGE 2")

    def selectMenu(getStyle):
        select = getStyle + ("QPushButton { border-right: 7px solid rgb(45, 45, 45); }")
        return select

    def deselectMenu(getStyle):
        deselect = getStyle.replace("QPushButton { border-right: 7px solid rgb(45, 45, 45); }", "")
        return deselect

    def selectStandardMenu(self):
        self.ui.pages_widget.setCurrentWidget(self.ui.page_1)
        for buttons in self.ui.frame_left_menu.findChildren(QPushButton):
            if buttons.objectName() == "button_menu_1":
                buttons.setStyleSheet(UIFunctions.selectMenu(buttons.styleSheet()))

    def resetStyle(self, widget):
        for buttons in self.ui.frame_left_menu.findChildren(QPushButton):
            if buttons.objectName() != widget:
                buttons.setStyleSheet(UIFunctions.deselectMenu(buttons.styleSheet()))








class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        #PROPIEDADES
        self.value = 0
        self.width = 150
        self.height = 150
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x498BD1
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 9
        self.suffix = "% Humedad"
        self.text_color = 0xffffff

        #TAMAÑO SIN CAPA
        self.resize(self.width, self.height)

    def add_shadow(self,enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(15)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0,0,0,120))
            self.setGraphicsEffect(self.shadow)

    def set_value(self, value):
        rango = []
        if(self.value>value):
            x = np.arange(value,self.value,0.3)
            y = x.astype(np.int)
            for n in y:
                rango.append(n)

            for n in reversed(y):
                self.value = n
                self.repaint()
        else:
            x = np.arange(self.value,value+1,0.3)
            y = x.astype(np.int)
            for n in y:
                self.value = n
                self.repaint()

    def paintEvent(self,event):
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 /self.max_value

        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setFont(QFont(self.font_family,self.font_size))

        rect = QRect(0,0,self.width,self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)

        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)

        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)

        paint.setPen(pen)
        paint.drawArc(margin,margin,width,height, -90 * 16, -value * 16)

        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect,Qt.AlignCenter, f"{self.value}{self.suffix}")

        paint.end()

class PyToggle(QCheckBox):
    def __init__(
    self,
    width = 40,
    bg_color = "#9B3D3F",
    circle_color = "#DDD",
    active_color = "#317F43",
    animation_curve = QEasingCurve.OutBounce
    ):
        QCheckBox.__init__(self)

        self.setFixedSize(width,20)
        self.setCursor(Qt.PointingHandCursor)

        self._bg_color = bg_color
        self._circle_color = circle_color
        self._activate_color = active_color

        #CREAR ANIMACION
        self._circle_position = 3
        self.animation = QPropertyAnimation(self,b"circle_position",self)
        self.animation.setEasingCurve(animation_curve)
        self.animation.setDuration(500)

        #CONECTAR CAMBIO DE ESTADO
        self.stateChanged.connect(self.start_transition)


    @Property(float)
    def circle_position(self):
        return self._circle_position

    @circle_position.setter
    def circle_position(self,pos):
        self._circle_position = pos
        self.update()

    def start_transition(self,value):
        self.animation.stop()

        if value:
            self.animation.setEndValue(self.width()-19)
        else:
            self.animation.setEndValue(3)

        # COMENZAR ANIMACION
        self.animation.start()

    def hitButton(self, pos: QPoint):
        return self.contentsRect().contains(pos)

    def paintEvent(self,e):

        paint = QPainter(self)
        paint.setRenderHint(QPainter.Antialiasing)

        paint.setPen(Qt.NoPen)

        rect = QRect(0,0,self.width(),self.height())

        if not self.isChecked():
            #FONDO
            paint.setBrush(QColor(self._bg_color))
            paint.drawRoundedRect(0,0,rect.width(),self.height(),self.height()/2,self.height()/2)

            #CIRCULO
            paint.setBrush(QColor(self._circle_color))
            paint.drawEllipse(self._circle_position,2,16,16)

        else:
            paint.setBrush(QColor(self._activate_color))
            paint.drawRoundedRect(0,0,rect.width(),self.height(),self.height()/2,self.height()/2)

            #CIRCULO
            paint.setBrush(QColor(self._circle_color))
            paint.drawEllipse(self._circle_position,2,16,16)

        #FIN
        paint.end()



def postgresMQTT():
    con = psycopg2.connect(host = "localhost",database = "IOT",user="postgres",password="2001")
    cur = con.cursor()
    SQL = ("INSERT INTO measurements (temperature, humidity, date) VALUES (%s,%s,%s)")
    data = (humidityList[0],temperatureList[0],str(date.today()))
    cur.execute(SQL, data)
    con.commit()
    cur.close()
    con.close()


def on_disconnect(client, userdata,rc=0):
    client.loop_stop()

def on_connect(client, userdata,flags,rc):
    print(enable[0])
    if(enable[0] == "False"):
        client.subscribe(topic = listTopics.pop(),qos = 2)
    print('Connected: (%s)' % client._client_id)

def on_message(client, userdata, message):
    message_received = str(format(message.payload.decode("utf-8")))
    temperature = ""
    humidity = ""
    next = False

    for words in message_received:
        if(words != "x" and next == False):
            temperature = temperature + str(words)
        else:
            next = True

        if(next == True):
            humidity = humidity + str(words)

    temperatureList.pop()
    humidityList.pop()
    temperatureList.append(temperature)
    humidityList.append(humidity[1:])
    print("Message Received: "+str("Temperatura:")+str(temperatureList[0])+str(" ")+str("Humidity:")+str(humidityList[0]))

def sendMQTT(server,topico,mensaje):
    client = paho.mqtt.client.Client(client_id = 'Ivan-subs', clean_session = False )
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host = server, port = 1883)
    client.publish(topico,mensaje)

def subscribeMQTT(server,user):
    print(enable[0])
    client = paho.mqtt.client.Client(client_id = user , clean_session = False )
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.loop_start()
    if(enable[0] == "True"):
        client.loop_stop()
    client.connect(host = server, port = 1883)



def unsubscribeMQTT(server,user):
    client = paho.mqtt.client.Client(client_id = user , clean_session = False )
    client.on_disconnect = on_disconnect
    client.loop_stop()
