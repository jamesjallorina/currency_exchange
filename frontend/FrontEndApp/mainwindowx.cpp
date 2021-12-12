#include "mainwindowx.h"
#include "ui_mainwindowx.h"

MainWindowx::MainWindowx(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindowx)
{
    ui->setupUi(this);
    const QStringList currencies = {"AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD",
                                    "BIF","BMD","BND","BOB","BRL","BSD","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CLP","CNY",
                                    "COP","CRC","CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD",
                                    "FKP","FOK","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF",
                                    "IDR","ILS","IMP","INR","IQD","IRR","ISK","JMD","JOD","JPY","KES","KGS","KHR","KID","KMF","KRW",
                                    "KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP",
                                    "MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN",
                                    "PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD",
                                    "SHP","SLL","SOS","SRD","SSP","STN","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TVD",
                                    "TWD","TZS","UAH","UGX","USD","UYU","UZS","VES","VND","VUV","WST","XAF","XCD","XDR","XOF","XPF",
                                    "YER","ZAR","ZMW"};

    ui->base_code->addItems(currencies);
    ui->target_code->addItems(currencies);
}

MainWindowx::~MainWindowx()
{
    delete ui;
}

void MainWindowx::on_base_code_activated(const QString &arg1)
{
    qDebug() << arg1;
    base_code = arg1;
}

void MainWindowx::on_target_code_activated(const QString &arg1)
{
    qDebug() << arg1;
    target_code = arg1;
}

void MainWindowx::on_base_amount_textEdited(const QString &arg1)
{
    qDebug() << arg1;
    base_amount = arg1;
}

void MainWindowx::on_pushButton_clicked()
{
    char buffer[100] = {0};
    const QByteArray data = base_amount.toLocal8Bit() + '/' + base_code.toLocal8Bit() + '/' + target_code.toLocal8Bit();
    qDebug() << "Sending bytes to Server: " << data;

    qsocket = new QTcpSocket( this );
    connect( qsocket, SIGNAL(QTcpSocket::readyRead()), SLOT(QTcpSocket::readData()));

    qsocket->connectToHost("127.0.0.1", PORT);
    if( qsocket->waitForConnected() ) {
        qDebug() << "Connected to Server";
        qsocket->write( data );
        while(true)
        {
            if(qsocket->waitForReadyRead()){
                qsocket->read(buffer, 100);
                break;
            }
        }
    }
    qDebug() << "Received response: " << buffer;
    QString converted_amount = QString(buffer);
    ui->lineEdit->setAlignment(Qt::AlignCenter);
    ui->lineEdit->setText(converted_amount);
    qsocket->close();
}
