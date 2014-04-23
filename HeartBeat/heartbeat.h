#ifndef HEARTBEAT_H
#define HEARTBEAT_H

#include <QMainWindow>
#include "ui_about.h"

namespace Ui {
class HeartBeat;
}

class HeartBeat : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit HeartBeat(QWidget *parent = 0);
    ~HeartBeat();
    
private:
    Ui::HeartBeat *ui;
    ui_About *dialog;
};

#endif // HEARTBEAT_H
