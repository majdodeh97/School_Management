import sys
from PyQt6.QtWidgets import (
    QApplication
)
from Database_SQL.Repositories.Student_Repository import StudentRepository
from Database_SQL.Repositories.Class_Repository import ClassRepository
from Database_SQL.Features.Email_Sender import EmailSender
from GUI_pyqt6.UI_Controllers.Main_Window import Window
from Database_SQL.Features.DatabaseManager import DatabaseManager
from Database_SQL.Repositories.Repository_Functions import RepositoryFunctions
from GUI_pyqt6.Configuration.Configuration import load_configuration
from Database_SQL.Repositories.Junction_Table import JunctionTable
from Database_SQL.Repositories.Subjects_Repository import SubjectRepository
from Database_SQL.Repositories.Categories_Repository import CategoriesRepository

if __name__ == "__main__":
    settings = load_configuration("GUI_pyqt6/Configuration/settings.json")
    dm = DatabaseManager(settings.database_path)
    dm.create_database()
    r_func = RepositoryFunctions(dm)
    st_repo = StudentRepository(dm)
    cl_repo = ClassRepository(dm, r_func)
    s_repo = SubjectRepository(dm, r_func)
    cat_repo = CategoriesRepository(dm)
    j_table = JunctionTable(dm, cl_repo, s_repo, cat_repo, r_func)
    emailSender = EmailSender()
    app = QApplication(sys.argv)
    win = Window(cl_repo, st_repo, r_func, emailSender, j_table)
    win.show()
    sys.exit(app.exec())
