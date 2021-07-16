import logging
import os

from flask import g


class LoggingManager:

    def __init__(self):
        self.log = None

    def init_logging(self, app):
        self.log = self.set_local_logging(app)

    def set_request_logging(self, request):
        # example of a request log
        req_log = {
            "severity": logging.INFO,
            "correlation_id": g.get('correlation_id'),
            "request_verb": request.method,
            "request_resource": request.path,
            "ip": request.remote_addr,
            "event_type": 'request'
        }
        self.send_to_kafka(req_log)

    def set_response_logging(self, request, response):
        msg = {}
        if hasattr(response, 'json') and response.json is not None:
            msg = response.json
        # example of a response log
        resp_log = {
            "severity": logging.INFO,
            "correlation_id": g.get('correlation_id'),
            "request_verb": request.method,
            "request_resource": request.path,
            "response_message": msg,
            "ip": request.remote_addr,
            "event_type": 'response'
        }
        self.send_to_kafka(resp_log)

    def set_local_logging(self, app):
        """
        Write logs in a file
        :param app:
        :return:
        """
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        if not os.path.isdir(app.config.get('LOGGING_DIR')):
            os.makedirs(app.config.get('LOGGING_DIR'))
        log_file = os.path.join(app.config.get('LOGGING_DIR'), 'app.log')
        logger = logging.getLogger('mathfunc')
        file_logging = logging.FileHandler(log_file)
        file_logging.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_logging)
        app.log = logger
        return logger

    def send_to_kafka(self, log):
        """
        Handler to send data in kafka, ES etc to monitor q request/response
        requests
        :return:
        """
        # handler to send logs in ES/Kafka
        # we can also write the logs in a file from were fluentd/logstash can read and send data to kafka/es etc
        self.log.info(log)
