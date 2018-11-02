url = 'http://preview.airwallex.com:30001/bank'
suc_code = 200
fail_code = 400
success = "Bank details saved"
pay_method_error = "'payment_method' field required, the value should be either 'LOCAL' or 'SWIFT'"

bank_country_code_error = "'bank_country_code' is required, and should be one of 'US', 'AU', or 'CN'"
account_name_empty_error =  "'account_name' is required"
account_name_length_error = "Length of account_name should be between 2 and 10"
account_name_error = [account_name_empty_error, account_name_length_error]

account_number_empty_error = "'account_number' is required"
account_us_number_length_error = "Length of account_number should be between 7 and 11 when bank_country_code is 'US'"
account_us_number_error = [account_number_empty_error, account_us_number_length_error]

account_au_number_length_error = "Length of account_number should be between 6 and 9 when bank_country_code is 'AU'"
account_au_number_error = [account_number_empty_error, account_au_number_length_error]

account_cn_number_length_error = "Length of account_number should be between 8 and 20 when bank_country_code is 'CN'"
account_cn_number_error = [account_number_empty_error, account_cn_number_length_error]
swift_code_length_error = "Length of 'swift_code' should be either 8 or 11"
swift_code_error = ["'swift_code' is required when payment method is 'SWIFT'",
                    "The swift code is not valid for the given bank country code: US",
                    "The swift code is not valid for the given bank country code: AU",
                     "The swift code is not valid for the given bank country code: CN",
                    swift_code_length_error
                    ]

bsb_error =["'bsb' is required when bank country code is 'AU'", "Length of 'bsb' should be 6"]
aba_error = ["'aba' is required when bank country code is 'US'","Length of 'aba' should be 9"]




