#ifndef HEARTSPLASHSCREEN_H
#define HEARTSPLASHSCREEN_H

#include <QSplashScreen>
#include <QTimer>

class HeartSplashScreen : public QSplashScreen
{
    Q_OBJECT
public:
    explicit HeartSplashScreen(QWidget* par, const QPixmap & pixmap = QPixmap());
    ~HeartSplashScreen();

    void timer_start(int msec);

signals:
    
public slots:
    void close();
    
private:
    QTimer timer;
    QWidget *parent;
};

#endif // HEARTSPLASHSCREEN_H
