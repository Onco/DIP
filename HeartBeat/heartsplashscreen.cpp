#include "heartsplashscreen.h"

HeartSplashScreen::HeartSplashScreen(QWidget *par,const QPixmap & pixmap) :
    QSplashScreen(pixmap,Qt::WindowStaysOnTopHint)
{
    parent = par;
    connect(&timer, SIGNAL(timeout()), this, SLOT(close()));
}

HeartSplashScreen::~HeartSplashScreen()
{
    this->finish(parent);
}

void HeartSplashScreen::timer_start(int msec) {
    timer.start(msec);
}

void HeartSplashScreen::close() {
    this->finish(parent);
}
