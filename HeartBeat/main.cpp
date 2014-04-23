#include <QtGui/QApplication>
#include "heartbeat.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    HeartBeat w;
    w.show();
    
    return a.exec();
}
