#ifndef HEARTBEAT_H
#define HEARTBEAT_H

#include <QMainWindow>
#include <QMessageBox>
#include <QFileDialog>

namespace Ui {
class HeartBeat;
}

class HeartBeat : public QMainWindow
{
    Q_OBJECT
    
public:
    explicit HeartBeat(QWidget *parent = 0);
    ~HeartBeat();

public slots:
    void openDir();

private:
    void setupAbout();

private:
    Ui::HeartBeat *ui;
    QMessageBox *aboutbox;
    QString directory;
};

#endif // HEARTBEAT_H
