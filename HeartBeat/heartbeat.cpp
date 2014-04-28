#include "heartbeat.h"
#include "ui_heartbeat.h"

HeartBeat::HeartBeat(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::HeartBeat)
{
    ui->setupUi(this);
    aboutbox = new QMessageBox();
    setupAbout();

    connect(ui->actionAbout_HeartBeat, SIGNAL(triggered()), aboutbox, SLOT(exec()));

    connect(ui->actionOpen, SIGNAL(triggered()), this, SLOT(openDir()));
}

HeartBeat::~HeartBeat()
{
    delete ui;
    delete aboutbox;
}

void HeartBeat::setupAbout() {
    aboutbox->setText("HeartBeat is a simple program used to detect heart chambers in an echocardiographic image. It is built on vosm library for face detection with modification to allow detection of heart in ultrasound scans.");
    aboutbox->setInformativeText("Version: 1.0\nReleased: 2014; Qt version: 4.8\nAuthor: Ondrej Vavro");
    aboutbox->setStandardButtons(QMessageBox::Ok);
    aboutbox->setDefaultButton(QMessageBox::Ok);
    aboutbox->setIconPixmap(QPixmap(":/img/logo.png").scaledToWidth(240));
    aboutbox->setWindowTitle("About HeartBeat");
}

void HeartBeat::openDir() {
    directory = QFileDialog::getExistingDirectory(this, tr("Open Directory"));
}
