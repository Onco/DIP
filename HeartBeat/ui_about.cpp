#include "ui_about.h"
#include "ui_ui_about.h"

ui_About::ui_About(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::ui_About)
{
    ui->setupUi(this);
}

ui_About::~ui_About()
{
    delete ui;
}
