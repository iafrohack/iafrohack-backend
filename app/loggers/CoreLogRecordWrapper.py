from logging import LogRecord

class CoreLogRecordWrapper(LogRecord):

    def getMessage(self):
        """
        :return: msg - the log's message
        """
        msg = str(self.msg)

        if self.args is None:
            return msg

        if isinstance(self.args, dict):
            return msg.format(**self.args)

        return msg.format(*self.args)
