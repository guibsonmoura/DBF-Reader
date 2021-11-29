
from dbfread import DBF
from PyQt5 import uic, QtWidgets
from tkinter import Tk
from tkinter.filedialog import  askopenfilename
import sys
caminho = ""
def escolherArquivo():
    Tk().withdraw()
    global caminho
    caminho =   askopenfilename()
    listaDbf = []
    try:
        for registros in DBF(caminho):
            print(registros)
            listaDbf.append(registros)
    except UnicodeDecodeError:
        print("alguma coisa deu errado")
    print(len(listaDbf[0]))
    formulario.tableWidget.setColumnCount(len(listaDbf[0]))
    formulario.tableWidget.setRowCount(len(listaDbf)+1)
    
    linhaTable = 0

    for linha in listaDbf:
        print("entrei aqui")
        
        colunaTable = 0 
        for titulo in linha:
            if linhaTable == 0:
                for titulo in linha:
                    formulario.tableWidget.setItem(linhaTable, colunaTable,QtWidgets.QTableWidgetItem(str(titulo)))
                    colunaTable +=1
                colunaTable = 0
                linhaTable += 1
                formulario.tableWidget.setItem(linhaTable, colunaTable,QtWidgets.QTableWidgetItem(str(linha[titulo])))
            else: 
                formulario.tableWidget.setItem(linhaTable, colunaTable,QtWidgets.QTableWidgetItem(str(linha[titulo])))    
               
            colunaTable += 1
        linhaTable += 1
#definindo layout
app=QtWidgets.QApplication(sys.argv)
formulario = uic.loadUi("firstScreen.ui")

#declaraçoes de botoes
formulario.pushButtonEscolher.clicked.connect(escolherArquivo)

#executando 
formulario.show()
sys.exit(app.exec_())