import pytest
from common import request
from common import assertion
from testdata import testdata
from testdata import commondata
import json


class TestCollectBankInfo:

    req = request.Request(commondata.url)
    test = assertion.Assertion()

    @pytest.mark.parametrize('payment_method', testdata.pay_method)
    def test_payment_method(self, payment_method):
        data = testdata.sample.copy()
        data['payment_method'] = payment_method
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.suc_code)
        assert self.test.assert_msg(response.text, 'success', commondata.success)

    @pytest.mark.parametrize('payment_method', testdata.invalid_pay_method)
    def test_invalid_payment_method(self, payment_method):
        data = testdata.sample.copy()
        data['payment_method'] = payment_method
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_msg(response.text, 'error', commondata.pay_method_error)

    @pytest.mark.parametrize('bank_country_code', testdata.valid_code_list)
    def test_bank_country_code(self, bank_country_code):
        response = self.req.post_request(bank_country_code)
        print(response.text)
        assert self.test.assert_code(response.status_code, commondata.suc_code)
        assert self.test.assert_msg(response.text, 'success', commondata.success)


    @pytest.mark.parametrize('bank_country_code', testdata.invalid_bank_country_code)
    def test_invalid_bank_country_code(self, bank_country_code):
        data = testdata.sample.copy()
        data['bank_country_code'] = bank_country_code
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_msg(response.text, 'error', commondata.bank_country_code_error)


    @pytest.mark.parametrize('account_name', testdata.account_name)
    def test_account_name(self, account_name):
        data = testdata.sample.copy()
        data['account_name'] = account_name
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.suc_code)
        assert self.test.assert_msg(response.text, 'success', commondata.success)

    @pytest.mark.parametrize('account_name', testdata.account_name)
    def test_account_name(self, account_name):
        data = testdata.sample.copy()
        data['account_name'] = account_name
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.suc_code)
        assert self.test.assert_msg(response.text, 'success', commondata.success)

    @pytest.mark.parametrize('account_name', testdata.invalid_account_name)
    def test_empty_account_name(self, account_name):
        data = testdata.sample.copy()
        data['account_name'] = account_name
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_in_msg(response.text, 'error', commondata.account_name_error)

    @pytest.mark.parametrize('account_number', testdata.us_account_number)
    def test_us_account_number(self, account_number):
        data = testdata.us_sample.copy()
        data['account_number'] = account_number
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.suc_code)
        assert self.test.assert_msg(response.text, 'success', commondata.success)

    @pytest.mark.parametrize('account_number', testdata.au_account_number)
    def test_au_account_number(self, account_number):
        data = testdata.au_sample.copy()
        data['account_number'] = account_number
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.suc_code)
        assert self.test.assert_msg(response.text, 'success', commondata.success)

    @pytest.mark.parametrize('account_number', testdata.cn_account_number)
    def test_cu_account_number(self, account_number):
        data = testdata.cn_sample.copy()
        data['account_number'] = account_number
        response = self.req.post_request(data)
        print(data)
        print(response.text)
        assert self.test.assert_code(response.status_code, commondata.suc_code)
        assert self.test.assert_msg(response.text, 'success', commondata.success)

    @pytest.mark.parametrize('account_number', testdata.invalid_us_account_number)
    def test_invalid_us_account_number(self, account_number):
        data = testdata.us_sample.copy()
        data['account_number'] = account_number
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_in_msg(response.text, 'error', commondata.account_us_number_error)

    @pytest.mark.parametrize('account_number', testdata.invalid_au_account_number)
    def test_invalid_au_account_number(self, account_number):
        data = testdata.au_sample.copy()
        data['account_number'] = account_number
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_in_msg(response.text, 'error', commondata.account_au_number_error)

    @pytest.mark.parametrize('account_number', testdata.invalid_cn_account_number)
    def test_invalid_cu_account_number(self, account_number):
        data = testdata.cn_sample.copy()
        data['account_number'] = account_number
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_in_msg(response.text, 'error', commondata.account_cn_number_error)

    @pytest.mark.parametrize('swift_code', testdata.invalid_swift_code_list1)
    def test_invalid_swift_code1(self, swift_code):
        response = self.req.post_request(swift_code)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_in_msg(response.text, 'error', commondata.swift_code_error)

    @pytest.mark.parametrize('swift_code', testdata.invalid_swift_code_list2)
    def test_invalid_swift_code2(self, swift_code):
        response = self.req.post_request(swift_code)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_in_msg(response.text, 'error', commondata.swift_code_error)

    @pytest.mark.parametrize('swift_code', testdata.invalid_swift_code_list3)
    def test_invalid_swift_code3(self, swift_code):
        response = self.req.post_request(swift_code)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_in_msg(response.text, 'error', commondata.swift_code_error)

    @pytest.mark.parametrize('bsb', testdata.invalid_bsb)
    def test_invalid_bsb(self, bsb):
        data = testdata.au_sample.copy()
        data['bsb'] = bsb
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_in_msg(response.text, 'error', commondata.bsb_error)

    @pytest.mark.parametrize('bsb', testdata.invalid_bsb_list)
    def test_invalid_bsb1(self, bsb):
        response = self.req.post_request(bsb)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_in_msg(response.text, 'error', commondata.bsb_error)

    @pytest.mark.parametrize('bsb', testdata.bsb)
    def test_bsb(self, bsb):
        data = testdata.au_sample.copy()
        data['bsb'] = bsb
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.suc_code)
        assert self.test.assert_in_msg(response.text, 'success', commondata.success)

    @pytest.mark.parametrize('aba', testdata.aba)
    def test_aba(self, aba):
        data = testdata.us_sample.copy()
        data['aba'] = aba
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.suc_code)
        assert self.test.assert_in_msg(response.text, 'success', commondata.success)

    @pytest.mark.parametrize('aba', testdata.invalid_aba)
    def test_invalid_aba(self, aba):
        data = testdata.us_sample.copy()
        data['aba'] = aba
        response = self.req.post_request(data)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_in_msg(response.text, 'error', commondata.aba_error)

    @pytest.mark.parametrize('aba', testdata.invalid_aba_list)
    def test_invalid_aba1(self, aba):
        response = self.req.post_request(aba)
        assert self.test.assert_code(response.status_code, commondata.fail_code)
        assert self.test.assert_in_msg(response.text, 'error', commondata.aba_error)
