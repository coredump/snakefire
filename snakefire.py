﻿#!/usr/bin/env python

import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

import snakefire

if snakefire.KDE_ENABLED:
    from PyKDE4 import kdecore
    from PyKDE4 import kdeui

if __name__ == "__main__":
    QtCore.QCoreApplication.setOrganizationName(snakefire.Snakefire.NAME);
    QtCore.QCoreApplication.setOrganizationDomain(snakefire.Snakefire.DOMAIN);
    QtCore.QCoreApplication.setApplicationName(snakefire.Snakefire.NAME);

    if snakefire.KDE_ENABLED:
        appName     = snakefire.Snakefire.NAME
        catalog     = ""
        programName = kdecore.ki18n(snakefire.Snakefire.NAME)
        version     = snakefire.Snakefire.VERSION
        description = kdecore.ki18n("A KDE Campfire client")
        license     = kdecore.KAboutData.License_Custom
        copyright   = kdecore.ki18n("(c) 2010 Mariano Iglesias")
        text        = kdecore.ki18n("none")
        homePage    = snakefire.Snakefire.DOMAIN

        about = kdecore.KAboutData(appName, catalog, programName, version, description,
                                    license, copyright, text, homePage)

        kdecore.KCmdLineArgs.init(sys.argv, about)

        app = kdeui.KApplication()
    else:
        app = QtGui.QApplication(sys.argv)

    sf = snakefire.Snakefire()

    if snakefire.KDE_ENABLED:
        app.setTopWidget(sf)
    
    sf.show()
    app.exec_()
