#ifndef WINDOW_H
#define WINDOW_H

#include <QWidget>

class QPushButton;

class window : public QWidget
{
Q_OBJECT
public:
	explicit window(QWidget *parent = 0);

private:
	QPushButton *m_button;
};

#endif

