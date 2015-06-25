#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import re;
import sys;
import urllib;
if(len(sys.argv) > 1):
      s =re.compile("<span class=\"eAcep\">(.*?)</span>");
      rm = re.compile("<.*?>(.*?)<.*?>");
      l = urllib.urlopen("http://buscon.rae.es/draeI/SrvltGUIBusUsual?TIPO_BUS=1&LEMA=%s" % sys.argv[1]).read();
      g = s.findall(l)
      if(g):
              print sys.argv[1]
              for i in g:
                       print "->"+ rm.sub(lambda x:x.group(1),i);