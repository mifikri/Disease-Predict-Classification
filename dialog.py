from PyQt5.QtCore import pyqtSignal, pyqtSlot, Q_CLASSINFO
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.QtDBus import (QDBusAbstractAdaptor, QDBusAbstractInterface, QDBusConnection, QDBusMessage)
import sys
from PyQt5 import uic
import autocomplete
from collections import OrderedDict
import model
import fielddata as fd

Ui_ChatMainWindow, QtBaseClass = uic.loadUiType("chatmainwindow.ui")
Ui_NicknameDialog, QtBaseClass = uic.loadUiType("chatsetnickname.ui")

class ChatAdaptor(QDBusAbstractAdaptor):

    Q_CLASSINFO("D-Bus Interface", 'org.example.chat')

    Q_CLASSINFO("D-Bus Introspection", ''
        '  <interface name="org.example.chat">\n'
        '    <signal name="message">\n'
        '      <arg direction="out" type="s" name="nickname"/>\n'
        '      <arg direction="out" type="s" name="text"/>\n'
        '    </signal>\n'
        '    <signal name="action">\n'
        '      <arg direction="out" type="s" name="nickname"/>\n'
        '      <arg direction="out" type="s" name="text"/>\n'
        '    </signal>\n'
        '  </interface>\n'
        '')

    action = pyqtSignal(str, str)
    message = pyqtSignal(str, str)

    def __init__(self, parent):
        super(ChatAdaptor, self).__init__(parent)
        self.setAutoRelaySignals(True)


class ChatInterface(QDBusAbstractInterface):
    action = pyqtSignal(str, str)
    message = pyqtSignal(str, str)

    def __init__(self, service, path, connection, parent=None):
        super(ChatInterface, self).__init__(service, path, 'org.example.chat',
                connection, parent)

class ChatMainWindow(QMainWindow, Ui_ChatMainWindow):

    action = pyqtSignal(str, str)

    message = pyqtSignal(str, str)

    def __init__(self):
        super(ChatMainWindow, self).__init__()

        self.m_nickname = "nickname"
        self.m_messages = []
        self.symptomRaw = []
        self.symptomClean = []
        self.inputTest = []

        self.setupUi(self)
        self.sendButton.setEnabled(False)

        self.messageLineEdit.textChanged.connect(self.textChangedSlot)
        self.messageLineEdit = autocomplete.auto(self.messageLineEdit)
        self.sendButton.clicked.connect(self.sendClickedSlot)
        self.unSendButton.clicked.connect(self.unsendMessage)
        self.clearButton.clicked.connect(self.clearMessage)
        QApplication.instance().lastWindowClosed.connect(self.exiting)

        self.predictButton.clicked.connect(self.retrieveChat)

        # Add our D-Bus interface and connect to D-Bus.
        ChatAdaptor(self)
        QDBusConnection.sessionBus().registerObject('/', self)

        iface = ChatInterface('', '', QDBusConnection.sessionBus(), self)
        QDBusConnection.sessionBus().connect('', '', 'org.example.chat',
                'message', self.messageSlot)
        iface.action.connect(self.actionSlot)

        dialog = NicknameDialog()
        dialog.cancelButton.setVisible(False)
        dialog.exec_()
        self.m_nickname = dialog.nickname.text().strip()
        self.action.emit(self.m_nickname, "joins the chat")

    def rebuildHistory(self):
        history = '\n'.join(self.m_messages)
        self.chatHistory.setPlainText(history)


    @pyqtSlot()
    def retrieveChat(self):
        for i in range (len(self.symptomRaw)):
            try:
                symtompIndex = fd.l1.index(str(self.symptomRaw[i]))
                self.symptomClean.append(fd.lowerl1[int(symtompIndex)])
            except:
                pass

        self.symptomClean = list(OrderedDict.fromkeys(self.symptomClean))

        sympInput = fd.symtompsInput()

        for k in range(0,len(fd.lowerl1)):
            for z in self.symptomClean:
                if z==fd.lowerl1[k]:
                    sympInput[k]=1
        
        self.inputTest = [sympInput]
        ypred = model.predict(self.inputTest)
        disease = fd.disease[int(ypred)]

        self.diseaseHistory.setPlainText(disease)

    @pyqtSlot(str, str)
    def messageSlot(self, nickname, text):
        self.m_messages.append("<%s> %s" % (nickname, text))

        if len(self.m_messages) > 100:
            self.m_messages.pop(0)

        self.rebuildHistory()
        self.symptomRaw.append(str(text))

    @pyqtSlot()
    def unsendMessage(self):
        if len(self.m_messages) > 1:
            del self.m_messages[-1]
        self.rebuildHistory()
        del self.symptomRaw[:]
        del self.symptomClean[:]


    @pyqtSlot()
    def clearMessage(self):
        #self.m_messages.append("* %s %s" % (nickname, text))
        del self.m_messages[1:]
        self.diseaseHistory.clear()
        self.rebuildHistory()
        del self.symptomRaw[:]
        del self.symptomClean[:]

    @pyqtSlot(str, str)
    def actionSlot(self, nickname, text):
        self.m_messages.append("* %s %s" % (nickname, text))

        if len(self.m_messages) > 100:
            self.m_messages.pop(0)

        self.rebuildHistory()

    @pyqtSlot(str)
    def textChangedSlot(self, newText):
        self.sendButton.setEnabled(newText != '')

    @pyqtSlot()
    def sendClickedSlot(self):
        msg = QDBusMessage.createSignal('/', 'org.example.chat', 'message')
        msg << self.m_nickname << self.messageLineEdit.text()
        QDBusConnection.sessionBus().send(msg)
        self.messageLineEdit.setText('')

    @pyqtSlot()
    def exiting(self):
        self.action.emit(self.m_nickname, "leaves the chat")


class NicknameDialog(QDialog, Ui_NicknameDialog):

    def __init__(self, parent=None):
        super(NicknameDialog, self).__init__(parent)

        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    chat = ChatMainWindow()
    chat.show()
    sys.exit(app.exec_())