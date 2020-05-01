from PyQt5.QtWidgets import QApplication
from dialog import Dialog
import sys

app = QApplication(sys.argv)
app.setStyle("fusion")
w = Dialog()
w.show()
sys.exit(app.exec_())