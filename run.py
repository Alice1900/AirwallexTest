import pytest


from util import log

test_log = log.logging


if __name__ == "__main__":
    test_log.info("start to run test cases")
    pytest.main(['-q', 'testcase/test_collect_bank_info_api.py'])




