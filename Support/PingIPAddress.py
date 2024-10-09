# coding=utf-8
import os
import ping, socket

class Ping:
    def __init__(self):
        pass

    def ping(self, hostname):
        try:
            # ping.verbose_ping(hostname, count=1)
            ip_res = ping.do_one(hostname, timeout=2, psize=3)
            if ip_res == None:
                res = 'Printer deconectat'
            else:
                res = 'Conectare printer cu succses'
            return res
        except socket.error, e:
            print "Ping Error:", e
