#include <QtGui/QApplication>
#include "heartsplashscreen.h"
#include "heartbeat.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    HeartBeat w;

    QPixmap splashpix(":/img/logo.png");
    HeartSplashScreen splash(&w, splashpix.scaledToWidth(640));

    splash.show();
    app.processEvents();
    splash.timer_start(500);

    w.show();
    //splash.raise();
    
    return app.exec();
}
