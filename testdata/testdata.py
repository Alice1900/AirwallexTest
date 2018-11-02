error = {"error": "'payment_method' field required, the value should be either 'LOCAL' or 'SWIFT'"}
pay_method = ["SWIFT", "LOCAL"]
invalid_pay_method = ["", "TEST", None]
bank_country_code = ["US", "AU", "CN"]
invalid_bank_country_code = ["", "test", None]
account_name = ["Alice", "Test", "12Test", "Five  @@*"]
invalid_account_name = ["", "A", "A12345678901234567890", None]
us_account_number =["*1A", "12 abc"]
invalid_us_account_number = ["", None, "12345678901234567890a"]
au_account_number =["abcdef", "abcdefgh0"]
invalid_au_account_number = ["awe", "", None, "12345678901234567890a"]
cn_account_number =["abcdefgh", "1234567890123456789a"]
invalid_cn_account_number = ["awe", "", None, "12345678901234567890ab"]
invalid_swift_code = []
invalid_swift_code_list1 = [
{
        "payment_method": "SWIFT",
        "bank_country_code": "US",
        "account_name": "John Smith",
        "account_number": "123",
        "aba": "11122233A"
}
]
invalid_swift_code_list2 = [
{
        "payment_method": "SWIFT",
        "bank_country_code": "US",
        "account_name": "John Smith",
        "account_number": "123",
        "swift_code": "ICBSSBBJ",
        "aba": "11122233A"
}, {
        "payment_method": "SWIFT",
        "bank_country_code": "CN",
        "account_name": "John Smith",
        "account_number": "12345678",
        "swift_code": "ICBSSBBJ",
        "aba": "11122233A"
}, {
        "payment_method": "SWIFT",
        "bank_country_code": "AU",
        "account_name": "John Smith",
        "account_number": "123456",
        "swift_code": "ICBSBUBJ",
        "bsb": "111222"
}, {
        "payment_method": "SWIFT",
        "bank_country_code": "AU",
        "account_name": "John Smith",
        "account_number": "123456",
        "swift_code": "ICBSBUBJ",
        "bsb": "111222"
}]

invalid_swift_code_list3 = [
{
        "payment_method": "SWIFT",
        "bank_country_code": "US",
        "account_name": "John Smith",
        "account_number": "12348",
        "swift_code": "ICBSBUS",
        "aba": "11122233A"
}, {
        "payment_method": "SWIFT",
        "bank_country_code": "CN",
        "account_name": "John Smith",
        "account_number": "12345678",
        "swift_code": "ICBSSCN",
        "aba": "11122233A"
}, {
        "payment_method": "SWIFT",
        "bank_country_code": "AU",
        "account_name": "John Smith",
        "account_number": "123456",
        "swift_code": "ICBSBAU",
        "bsb": "111222"
}, {
        "payment_method": "SWIFT",
        "bank_country_code": "US",
        "account_name": "John Smith",
        "account_number": "1234567",
        "swift_code": "ICBSBUSAAAAA",
        "aba": "11122233A"
}, {
        "payment_method": "SWIFT",
        "bank_country_code": "CN",
        "account_name": "John Smith",
        "account_number": "12345678",
        "swift_code": "ICBSSCNAAAAA",
        "aba": "11122233A"
}, {
        "payment_method": "SWIFT",
        "bank_country_code": "AU",
        "account_name": "John Smith",
        "account_number": "123456",
        "swift_code": "ICBSBAUAAAAA",
        "bsb": "111222"
} ]

bsb = ["ABCEFD", "      "]
invalid_bsb = ["", "ACD"]
invalid_bsb_list = [
 {
        "payment_method": "SWIFT",
        "bank_country_code": "AU",
        "account_name": "John Smith",
        "account_number": "123456",
        "swift_code": "ICBSAUBJ"
 }
]

aba = ["ABCEFDHIF","123456789"]
invalid_aba = ["ABCE", "123456789A"]
invalid_aba_list = [
    {
        "payment_method": "SWIFT",
        "bank_country_code": "US",
        "account_name": "John Smith",
        "account_number": "1234567",
        "swift_code": "ICBSUSBJ"
    }
]


sample = {
        "payment_method": "SWIFT",
        "bank_country_code": "US",
        "account_name": "John Smith",
        "account_number": "1234567",
        "swift_code": "ICBSUSBJ",
        "aba": "11122233A"
}
us_sample = {
        "payment_method": "SWIFT",
        "bank_country_code": "US",
        "account_name": "John Smith",
        "account_number": "1234567",
        "swift_code": "ICBSUSBJ",
        "aba": "11122233A"
}
cn_sample = {
        "payment_method": "SWIFT",
        "bank_country_code": "CN",
        "account_name": "John Smith",
        "account_number": "12345678",
        "swift_code": "ICBSCNBJ",
        "aba": "11122233A"
}

au_sample = {
        "payment_method": "SWIFT",
        "bank_country_code": "AU",
        "account_name": "John Smith",
        "account_number": "123456",
        "swift_code": "ICBSAUBJ",
        "bsb": "111222"
}
valid_code_list = [us_sample, cn_sample, au_sample]
