#!/usr/bin/env python
"""An SMTP sink."""

import argparse
import asyncore
import json
import os
import re
import smtpd
import threading
import time

class SmtpSinkServer(smtpd.SMTPServer):
  """SMTP Sink class."""

  __lock = threading.Lock()

  def __init__(self, host, port, sink_dir='/tmp/smtpsink', msg_ct=50, **kwargs):
    print 'SMTPSink ready for service.'
    smtpd.SMTPServer.__init__(self, (host, port), None, **kwargs)
    self._sink_dir = sink_dir
    if not os.path.exists(self._sink_dir):
      os.makedirs(self._sink_dir)
    self._msg_ct = msg_ct

  def process_message(self, peer, mailfrom, rcptto, data):
    """Save the received message into a log."""
    __lock.acquire()
    pat = re.compile('\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d.\d+$')
    msgs = [f for f in sorted(os.listdir(self._sink_dir)) if pat.match(f)]
    if len(msgs) > self._msg_ct:
      for doomed in msgs[:-self._msg_ct]:
        os.unlink(os.path.join(self._sink_dir, doomed))
    fn = time.strftime('%Y-%m-%d %H:%M:%S.', time.localtime())
    i = 0
    while os.path.exists(os.path.join(self._sink_dir, fn + str(i))):
      i += 1
    fn = fn + str(i)
    f = open(os.path.join(self._sink_dir, fn), 'w')
    f.write(json.dumps({
      'peer': peer,
      'mailfrom': mailfrom,
      'rcpttos': rcpttos,
      'data': data,
      }))
    f.close()
    __lock.release()


if __name__ == '__main__':
  parser = argparse.ArgumentParser(prog='smtpsinkd',
    usage='%(prog)s [options]', description='SMTP Sink server')
  parser.add_argument('host', nargs='?', default='localhost')
  parser.add_argument('port', nargs='?', type=int, default=25)
  parser.add_argument('--sink-dir', default='log')
  parser.add_argument('-v', '--version', action='version',
      version='%(prog)s 0.0.1')
  args = parser.parse_args()
  smtpsink = SmtpSinkServer(args.host, args.port, sink_dir=args.sink_dir)
  try:
    asyncore.loop()
  except KeyboardInterrupt:
    smtpsink.close()
