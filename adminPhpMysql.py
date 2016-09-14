#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#  adminPhpMysql.py
#
#  Copyright 2016 Douglas Fiedler <douglas@dognew.com.br>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#



import pygtk
pygtk.require("2.0") # Define versão requirida
import gtk
from os import path
import commands

class adminPhpMysql(object):
    def __init__(self):
        builder = gtk.Builder()
        gladefile = path.dirname(path.realpath(__file__)) + '/adminPhpMysql.glade'

        builder.add_from_file(gladefile)

        self.window = builder.get_object("telaAdmin")
        self.passRoot = builder.get_object("passRoot")
        self.alerts = builder.get_object("Alerts")
        self.about = builder.get_object("about_dialog")
        self.window.show()

        builder.connect_signals({
            "gtk_main_quit": gtk.main_quit,
            "on_BtStartPhp_clicked": self.BtStartPhp,"on_BtStopPhp_clicked": self.BtStopPhp,
            "on_BtRestartPhp_clicked": self.BtRestartPhp,"on_BtStatusPhp_clicked": self.BtStatusPhp,
            "on_BtStartMysql_clicked": self.BtStartMysql,"on_BtStopMysql_clicked": self.BtStopMysql,
            "on_BtRestartMysql_clicked": self.BtRestartMysql,"on_BtStatusMysql_clicked": self.BtStatusMysql,
            })

    def BtStartPhp(self, widget):
        self.alerts.set_text("")
        senha = self.passRoot.get_text();
        msg = os.system("echo '"+senha+"' | sudo -S /etc/init.d/apache2 start")
        if msg == 0:
            msg = commands.getoutput("/etc/init.d/apache2 status")
        elif msg == 256:
            msg = "Senha incorreta"
        else:
            msg = str(msg)
        self.alerts.set_text(msg)

    def BtStopPhp(self, widget):
        self.alerts.set_text("")
        senha = self.passRoot.get_text();
        msg = os.system("echo '"+senha+"' | sudo -S /etc/init.d/apache2 stop")
        if msg == 0:
            msg = commands.getoutput("/etc/init.d/apache2 status")
        elif msg == 256:
            msg = "Senha incorreta"
        else:
            msg = str(msg)
        self.alerts.set_text(msg)

    def BtStatusPhp(self, widget):
        self.alerts.set_text("")
        senha = self.passRoot.get_text();
        msg = commands.getoutput("echo '"+senha+"' | sudo -S /etc/init.d/apache2 status")
        self.alerts.set_text("")
        self.alerts.set_text(msg)

    def BtRestartPhp(self, widget):
        self.alerts.set_text("")
        senha = self.passRoot.get_text();
        msg = os.system("echo '"+senha+"' | sudo -S /etc/init.d/apache2 restart")
        if msg == 0:
            msg = commands.getoutput("/etc/init.d/apache2 status")
        elif msg == 256:
            msg = "Senha incorreta"
        else:
            msg = str(msg)
        self.alerts.set_text(msg)

    def BtStartMysql(self, widget):
        self.alerts.set_text("")
        senha = self.passRoot.get_text();
        msg = os.system("echo '"+senha+"' | sudo -S /etc/init.d/mysql start")
        if msg == 0:
            msg = commands.getoutput("echo '"+senha+"' | sudo -S /etc/init.d/mysql status")
        elif msg == 256:
            msg = "Senha incorreta"
        else:
            msg = str(msg)
        self.alerts.set_text(msg)

    def BtStopMysql(self, widget):
        self.alerts.set_text("")
        senha = self.passRoot.get_text();
        msg = os.system("echo '"+senha+"' | sudo -S /etc/init.d/mysql stop")
        if msg == 0:
            msg = commands.getoutput("echo '"+senha+"' | sudo -S /etc/init.d/mysql status")
        elif msg == 256:
            msg = "Senha incorreta"
        else:
            msg = str(msg)
        self.alerts.set_text(msg)

    def BtStatusMysql(self, widget):
        self.alerts.set_text("")
        senha = self.passRoot.get_text();
        msg = commands.getoutput("echo '"+senha+"' | sudo -S /etc/init.d/mysql status")
        self.alerts.set_text("")
        self.alerts.set_text(msg)

    def BtRestartMysql(self, widget):
        self.alerts.set_text("")
        senha = self.passRoot.get_text();
        msg = os.system("echo '"+senha+"' | sudo -S /etc/init.d/mysql restart")
        if msg == 0:
            msg = commands.getoutput("echo '"+senha+"' | sudo -S /etc/init.d/mysql status")
        elif msg == 256:
            msg = "Senha incorreta"
        else:
            msg = str(msg)
        self.alerts.set_text(msg)

    def about_window(self, widget):
        self.about.run()
        self.about.hide()

if __name__ == "__main__":
    app = adminPhpMysql()
    gtk.main()
