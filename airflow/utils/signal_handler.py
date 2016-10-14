from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import signal


class SignalHandler:
    sigint_received = False
    sigterm_received = False
    sigquit_received = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.handle_sigint)
        signal.signal(signal.SIGTERM, self.handle_sigterm)
        signal.signal(signal.SIGQUIT, self.handle_sigquit)

    def handle_sigint(self, signum, frame):
        logging.info('SignalHandler detected SIGINT signal...')
        self.sigint_received = True

    def handle_sigterm(self, signum, frame):
        logging.info('SignalHandler detected SIGTERM signal...')
        self.sigterm_received = True

    def handle_sigquit(self, signum, frame):
        logging.info('SignalHandler detected SIGQUIT signal...')
        self.sigquit_received = True
