import inspect
import logging

import softest


class Utils(softest.TestCase):
    def assert_list_items_text(self, result, stop):
        for value in result:
            self.soft_assert(self.assertEqual, stop.text, value)
        self.assert_all()

    def custom_logger(logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        fh = logging.FileHandler("automation.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
