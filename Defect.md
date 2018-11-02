# Defects


- Defect 1 
   
   failed case: test_cu_account_number
   
   input :1234567890123456789a
   
   expected result :  the return code is 200
    
   actual result : return code is 400
   
   error msg: 
        
        {"error":"Length of account_number should be between 7 and 11 when bank_country_code is 'US'"}
 
   possible reason: the length check is is invalid when bank_country_code with CN   

   
- Defect 2 
   
  failed case : test_invalid_au_account_number
  input : 'awe'  and '12345678901234567890a'
  expected result : "Length of account_number should be between 6 and 9 when bank_country_code is 'AU'"
  actual result : Length of account_number should be between 7 and 11 when bank_country_code is 'US'
  reason: error message of au

- Defect 3 
   
  failed case : test_invalid_cu_account_number
  input : awe '12345678901234567890ab'
  expected result : Length of account_number should be between 8 and 20 when bank_country_code is 'CN'
  actual result : Length of account_number should be between 7 and 11 when bank_country_code is 'US'
  reason: error message of cu
   
- Defect 4
   
   failed case: test_invalid_aba1
   
   input :
   
      invalid_aba_list = [{
        "payment_method": "SWIFT",
        "bank_country_code": "US",
        "account_name": "John Smith",
        "account_number": "123",
        "swift_code": "ICBSUSBJ"}]
   
   expected result :  the return code is 400
    
   actual result : return code is 200
   
   possible reason: aba is not mandatory when bank country is US

  
   
    