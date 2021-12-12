#ifndef MAINWINDOWX_H
#define MAINWINDOWX_H

#include <QMainWindow>
#include <QString>
#include <QStringList>
#include <QDebug>
#include <QTcpSocket>


QT_BEGIN_NAMESPACE
namespace Ui { class MainWindowx; }
QT_END_NAMESPACE

const int PORT = 8888;

class MainWindowx : public QMainWindow
{
    Q_OBJECT

public:
    MainWindowx(QWidget *parent = nullptr);
    ~MainWindowx();

private slots:
    void on_target_code_activated(const QString &arg1);

    void on_base_code_activated(const QString &arg1);

    void on_base_amount_textEdited(const QString &arg1);

    void on_pushButton_clicked();

private:
    Ui::MainWindowx *ui;
    QString base_amount = "1";
    QString base_code = "PHP";
    QString target_code = "USD";

private:
    QTcpSocket* qsocket;
};
#endif // MAINWINDOWX_H
