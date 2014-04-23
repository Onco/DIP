#include "heartbeat.h"
#include "ui_heartbeat.h"

HeartBeat::HeartBeat(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::HeartBeat)
{
    ui->setupUi(this);
    dialog = new ui_About(this);
    connect(ui->actionAbout_HeartBeat, SIGNAL(triggered()), dialog, SLOT(show()));
}

HeartBeat::~HeartBeat()
{
    delete ui;
}
