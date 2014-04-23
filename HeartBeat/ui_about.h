#ifndef UI_ABOUT_H
#define UI_ABOUT_H

#include <QDialog>

namespace Ui {
class ui_About;
}

class ui_About : public QDialog
{
    Q_OBJECT
    
public:
    explicit ui_About(QWidget *parent = 0);
    ~ui_About();
    
private:
    Ui::ui_About *ui;
};

#endif // UI_ABOUT_H
