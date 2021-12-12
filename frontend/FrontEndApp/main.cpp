#include "mainwindowx.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    app.setApplicationName("CurrencyConverter");
    app.setOrganizationName("CurrencyConverter");
    MainWindowx window;
    window.setWindowTitle(QApplication::translate("toplevel", "CurrencyConverter"));
    window.show();
    return app.exec();
}
