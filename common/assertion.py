import json
from util import log


class Assertion:
    def __init__(self):
        self.log = log.logging

    def assert_code(self, code, expected_code):
        try:
            assert code == expected_code
            return True
        except Exception:
            self.log.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            raise

    def assert_msg(self, body, tag, expected_msg):
        try:
            msg_body = json.loads(body)
            msg = msg_body[tag]
            self.log.info("Response body msg is %s" % msg)
            assert msg == expected_msg
            return True
        except Exception:
            self.log.error("Response body msg is not expected, expected_msg is %s" % (expected_msg))
            raise

    def assert_in_msg(self, body, tag, expected_msg):
        try:
            msg_body = json.loads(body)
            msg = msg_body[tag]
            self.log.info("Response body msg is %s" % msg)
            assert msg in expected_msg
            return True
        except Exception:
            self.log.error("Response body msg is not expected, expected_msg is %s" % (expected_msg))
            raise