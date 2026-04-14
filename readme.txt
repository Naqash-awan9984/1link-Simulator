1link-simulator.service



UAT URL: https://sandboxapi.1link.net.pk/uat-1link/link-certification
SIMULATOR URL: http://localhost:2011/onelink/production


////////////////1link TF

curl -k -X POST "http://localhost:2011/onelink/production/path-1" \
-H "Authorization: Bearer TESTTOKEN123" \
-H "Accept: application/json" \
-H "X-IBM-Client-Id: 60ed8b756e9e10b08c98e4553bcb15d2" \
-H "X-IBM-Client-Secret: 867ce669121dc052df79f0af88b699e0" \
-H "Content-Type: application/json" \
-d '{
"TransactionAmount":"000005000000",
"TransmissionDateAndTime":"0309184012",
"STAN":"012123",
"Time":"184012",
"Date":"0309",
"MerchantType":"0003",
"FromBankIMD":"639357",
"RRN":"009184012123",
"CardAcceptorTerminalId":"00000133",
"CardAcceptorIdCode":"000000000002027",
"PaymentDetail":"0401 Home Remittance",
"CurrencyCodeTransaction":"586",
"AccountNumberTo":"PK12MEZN0036010108930805",
"ToBankIMD":"627873",
"PAN":"0000000000000",
"PosEntMode":"901"
}'



****************1link IBFT




	curl -k -X POST "http://localhost:2011/onelink/production/funds-transfer-rest-service/path-1" \
	-H "Authorization: Bearer TESTTOKEN123" \
	-H "Accept: application/json" \
	-H "X-IBM-Client-Id: 60ed8b756e9e10b08c98e4553bcb15d2" \
	-H "X-IBM-Client-Secret: 867ce669121dc052df79f0af88b699e0" \
	-H "Content-Type: application/json" \
	-d '{
	"TransactionAmount":"000005000000",
	"TransmissionDateAndTime":"0309224515",
	"STAN":"151627",
	"Time":"224515",
	"Date":"0309",
	"MerchantType":"0003",
	"FromBankIMD":"639357",
	"RRN":"092245151627",
	"AuthorizationIdentificationResponse":"672280",
	"CardAcceptorTerminalId":"00000133",
	"CardAcceptorIdCode":"000000000002027",
	"PaymentDetail":"0401",
	"CurrencyCodeTransaction":"586",
	"AccountNumberFrom":"100340191130001",
	"AccountNumberTo":"PK12MEZN0036010108930805",
	"ToBankIMD":"627873",
	"PAN":"0000000000000",
	"PosEntryMode":"901",
	"SenderName":"SAMEER JAN MUHAMMAD KHAN",
	"SenderIBAN":"100340191130001",
	"AccountTitle":"LUQMAN"
	}'
	
	
	
****************1link inquiry
	
	curl -X POST http://10.0.142.4:8005/one-link/mpay/trace/IBFT \
-H "Content-Type: application/json" \
-d '{
"ostan":"023786",
"orrn":"009163023786",
"otxndate":"20260309",
"otxntime":"163021"
}'


****************Fetch API IMD Test Cases (from Book16.xlsx)
For each case, send ToBankIMD and AccountNumberTo. Expected response is exact JSON below.
Note: Some cases intentionally use the same ToBankIMD. Response selection is based on ToBankIMD + AccountNumberTo together.

Case 1
Request:
{
  "ToBankIMD": "589430",
  "AccountNumberTo": "PK89ABPA0010117126020017"
}
Expected Response:
{
  "response": {
    "response_code": "00",
    "response_desc": "PROCESSED OK",
    "title-fetch": {
      "AccountTitleTo": "FATIMA BIBI",
      "BankName": "ALLIED BANK LIMITED",
      "ResponseCode": "00",
      "IBAN_MobileAccountNumber": "PK89ABPA0010117126020017",
      "Amount": "000003709000",
      "STAN": "282021",
      "BranchNameTo": "0082",
      "Time": "180828",
      "TransmissionDateAndTime": "0331180828",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311808282021",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "765347",
      "ResponseDetail": "PROCESSED OK",
      "ToBankIMD": "589430",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK89ABPA0010117126020017"
    }
  }
}

Case 2
Request:
{
  "ToBankIMD": "639390",
  "AccountNumberTo": "03060486668"
}
Expected Response:
{
  "response": {
    "response_code": "01",
    "response_desc": "LIMIT EXCEEDED",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "01",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000000986200",
      "STAN": "208693",
      "BranchNameTo": "",
      "Time": "135120",
      "TransmissionDateAndTime": "0331135120",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311351208693",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "LIMIT EXCEEDED",
      "ToBankIMD": "639390",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "03060486668"
    }
  }
}

Case 3
Request:
{
  "ToBankIMD": "588974",
  "AccountNumberTo": "287160686"
}
Expected Response:
{
  "response": {
    "response_code": "02",
    "response_desc": "INVALID ACCOUNT",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "02",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000010000000",
      "STAN": "492289",
      "BranchNameTo": "",
      "Time": "181049",
      "TransmissionDateAndTime": "0331181049",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311810492289",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "INVALID ACCOUNT",
      "ToBankIMD": "588974",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "287160686"
    }
  }
}

Case 4
Request:
{
  "ToBankIMD": "588974",
  "AccountNumberTo": "PK37UNIL0109000246915175"
}
Expected Response:
{
  "response": {
    "response_code": "03",
    "response_desc": "ACCOUNT INACTIVE",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "03",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000018537800",
      "STAN": "492275",
      "BranchNameTo": "",
      "Time": "181049",
      "TransmissionDateAndTime": "0331181049",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311810492275",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "ACCOUNT INACTIVE",
      "ToBankIMD": "588974",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK37UNIL0109000246915175"
    }
  }
}

Case 5
Request:
{
  "ToBankIMD": "559049",
  "AccountNumberTo": "03197055701"
}
Expected Response:
{
  "response": {
    "response_code": "17",
    "response_desc": "UNKNOWN AUTH MODE",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "17",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000001000000",
      "STAN": "407730",
      "BranchNameTo": "",
      "Time": "183940",
      "TransmissionDateAndTime": "0324183940",
      "Reserved1": "",
      "Date": "0324",
      "Reserved3": "",
      "RRN": "241839407730",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "",
      "ToBankIMD": "559049",
      "DateSettlement": "0325",
      "PAN": "0000000000000",
      "AccountNumberTo": "03197055701"
    }
  }
}

Case 6
Request:
{
  "ToBankIMD": "627197",
  "AccountNumberTo": "PK65BAHL2067004200136801"
}
Expected Response:
{
  "response": {
    "response_code": "21",
    "response_desc": "NO TRANSACTION ON ACCT",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "21",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000001038500",
      "STAN": "108664",
      "BranchNameTo": "",
      "Time": "135110",
      "TransmissionDateAndTime": "0331135110",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311351108664",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "NO TRANSACTION ON ACCT",
      "ToBankIMD": "627197",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK65BAHL2067004200136801"
    }
  }
}

Case 7
Request:
{
  "ToBankIMD": "46168900",
  "AccountNumberTo": "03053377887"
}
Expected Response:
{
  "response": {
    "response_code": "26",
    "response_desc": "INTERNAL ERROR",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "26",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000000001200",
      "STAN": "537095",
      "BranchNameTo": "",
      "Time": "153700",
      "TransmissionDateAndTime": "0302153700",
      "Reserved1": "",
      "Date": "0302",
      "Reserved3": "",
      "RRN": "000021537095",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "INTERNAL ERROR",
      "ToBankIMD": "46168900",
      "DateSettlement": "0303",
      "PAN": "0000000000000",
      "AccountNumberTo": "03053377887"
    }
  }
}

Case 8
Request:
{
  "ToBankIMD": "589430",
  "AccountNumberTo": "ABPA1230010106934840017"
}
Expected Response:
{
  "response": {
    "response_code": "46",
    "response_desc": "UNABLE TO PROCESS",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "46",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000030756900",
      "STAN": "108633",
      "BranchNameTo": "",
      "Time": "135100",
      "TransmissionDateAndTime": "0331135100",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "031135108633",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "TO PROCESS",
      "ToBankIMD": "589430",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "ABPA1230010106934840017"
    }
  }
}

Case 9
Request:
{
  "ToBankIMD": "627544",
  "AccountNumberTo": "PK44SAUD0000462011385047"
}
Expected Response:
{
  "response": {
    "response_code": "55",
    "response_desc": "HOST LINK DOWN",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "55",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000000504500",
      "STAN": "508590",
      "BranchNameTo": "",
      "Time": "135050",
      "TransmissionDateAndTime": "0331135050",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311350508590",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "HOST LINK DOWN",
      "ToBankIMD": "627544",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK44SAUD0000462011385047"
    }
  }
}

Case 10
Request:
{
  "ToBankIMD": "589430",
  "AccountNumberTo": "PK59ABPA0010042984890013"
}
Expected Response:
{
  "response": {
    "response_code": "58",
    "response_desc": "TRANSACTION TIMEDOUT",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "58",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000010125700",
      "STAN": "731245",
      "BranchNameTo": "",
      "Time": "173731",
      "TransmissionDateAndTime": "0331173731",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "031173731245",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "",
      "ResponseDetail": "TRANSACTION TIMEDOUT",
      "ToBankIMD": "589430",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK59ABPA0010042984890013"
    }
  }
}

Case 11
Request:
{
  "ToBankIMD": "623977",
  "AccountNumberTo": "PK58BPUN6640266672700019"
}
Expected Response:
{
  "response": {
    "response_code": "59",
    "response_desc": "HOST REJECT",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "59",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000001476200",
      "STAN": "492293",
      "BranchNameTo": "",
      "Time": "181049",
      "TransmissionDateAndTime": "0331181049",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311810492293",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "HOST REJECT",
      "ToBankIMD": "623977",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK58BPUN6640266672700019"
    }
  }
}

Case 12
Request:
{
  "ToBankIMD": "220552",
  "AccountNumberTo": "PK16MUCB1682335231016132"
}
Expected Response:
{
  "response": {
    "response_code": "63",
    "response_desc": "DESTINATION NOT FOUND",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "MCB BANK LTD",
      "ResponseCode": "63",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000010000000",
      "STAN": "928052",
      "BranchNameTo": "",
      "Time": "135902",
      "TransmissionDateAndTime": "0305135902",
      "Reserved1": "",
      "Date": "0305",
      "Reserved3": "",
      "RRN": "005135928052",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "DESTINATION NOT FOUND",
      "ToBankIMD": "220552",
      "DateSettlement": "0306",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK16MUCB1682335231016132"
    }
  }
}

Case 13
Request:
{
  "ToBankIMD": "600648",
  "AccountNumberTo": "PK42HABB0003597900165303"
}
Expected Response:
{
  "response": {
    "response_code": "65",
    "response_desc": "CASH TRANSACTION NOT ALLOWED",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "65",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000001114100",
      "STAN": "114747",
      "BranchNameTo": "",
      "Time": "195101",
      "TransmissionDateAndTime": "0311195101",
      "Reserved1": "",
      "Date": "0311",
      "Reserved3": "",
      "RRN": "011195114747",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "CASH TRANSACTION NOT ALLOWED",
      "ToBankIMD": "600648",
      "DateSettlement": "0312",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK42HABB0003597900165303"
    }
  }
}

Case 14
Request:
{
  "ToBankIMD": "589430",
  "AccountNumberTo": "PK95ABPA0010089268370010"
}
Expected Response:
{
  "response": {
    "response_code": "66",
    "response_desc": "NO TRANSACTION ALLOWED",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "66",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000004820400",
      "STAN": "492283",
      "BranchNameTo": "",
      "Time": "181049",
      "TransmissionDateAndTime": "0331181049",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311810492283",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "NO TRANSACTION ALLOWED",
      "ToBankIMD": "589430",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK95ABPA0010089268370010"
    }
  }
}

Case 15
Request:
{
  "ToBankIMD": "627271",
  "AccountNumberTo": "00001715277501"
}
Expected Response:
{
  "response": {
    "response_code": "67",
    "response_desc": "INVALID ACCOUNT STATUS",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "67",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000011007600",
      "STAN": "492271",
      "BranchNameTo": "",
      "Time": "181049",
      "TransmissionDateAndTime": "0331181049",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311810492271",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "INVALID ACCOUNT STATUS",
      "ToBankIMD": "627271",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "00001715277501"
    }
  }
}

Case 16
Request:
{
  "ToBankIMD": "627408",
  "AccountNumberTo": "9930177140101693"
}
Expected Response:
{
  "response": {
    "response_code": "68",
    "response_desc": "INVALID TO ACCOUNT",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "68",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000056248400",
      "STAN": "308756",
      "BranchNameTo": "",
      "Time": "135130",
      "TransmissionDateAndTime": "0331135130",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311351308756",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "",
      "ResponseDetail": "INVALID TO ACCOUNT",
      "ToBankIMD": "627408",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "9930177140101693"
    }
  }
}

Case 17
Request:
{
  "ToBankIMD": "627271",
  "AccountNumberTo": "PK86SCBL0000001180414202"
}
Expected Response:
{
  "response": {
    "response_code": "77",
    "response_desc": "REFER TO ISSUER",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "77",
      "IBAN_MobileAccountNumber": "PK86SCBL0000001180414202",
      "Amount": "000037090500",
      "STAN": "492277",
      "BranchNameTo": "",
      "Time": "181049",
      "TransmissionDateAndTime": "0331181049",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311810492277",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "REFER TO ISSUER",
      "ToBankIMD": "627271",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK86SCBL0000001180414202"
    }
  }
}

Case 18
Request:
{
  "ToBankIMD": "62910400",
  "AccountNumberTo": "PK87MPBL0668027140103149"
}
Expected Response:
{
  "response": {
    "response_code": "80",
    "response_desc": "MESSAGE FORMAT ERROR",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "80",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000008000000",
      "STAN": "518034",
      "BranchNameTo": "",
      "Time": "135851",
      "TransmissionDateAndTime": "0305135851",
      "Reserved1": "",
      "Date": "0305",
      "Reserved3": "",
      "RRN": "051358518034",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "",
      "ResponseDetail": "MESSAGE FORMAT ERROR",
      "ToBankIMD": "62910400",
      "DateSettlement": "0306",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK87MPBL0668027140103149"
    }
  }
}

Case 19
Request:
{
  "ToBankIMD": "639390",
  "AccountNumberTo": "03004787587"
}
Expected Response:
{
  "response": {
    "response_code": "90",
    "response_desc": "CUSTOMER NOT FOUND",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "90",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000000037700",
      "STAN": "492285",
      "BranchNameTo": "",
      "Time": "181049",
      "TransmissionDateAndTime": "0331181049",
      "Reserved1": "",
      "Date": "0331",
      "Reserved3": "",
      "RRN": "311810492285",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "CUSTOMER NOT FOUND",
      "ToBankIMD": "639390",
      "DateSettlement": "0401",
      "PAN": "0000000000000",
      "AccountNumberTo": "03004787587"
    }
  }
}

Case 20
Request:
{
  "ToBankIMD": "589388",
  "AccountNumberTo": "PK09MUCB1624880371002474"
}
Expected Response:
{
  "response": {
    "response_code": "94",
    "response_desc": "PERMISSION DENIED",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "MCB BANK LIMITED",
      "ResponseCode": "94",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000000742500",
      "STAN": "919682",
      "BranchNameTo": "0000",
      "Time": "204919",
      "TransmissionDateAndTime": "0325204919",
      "Reserved1": "",
      "Date": "0325",
      "Reserved3": "",
      "RRN": "025204919682",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "PERMISSION DENIED",
      "ToBankIMD": "589388",
      "DateSettlement": "0326",
      "PAN": "0000000000000",
      "AccountNumberTo": "PK09MUCB1624880371002474"
    }
  }
}

Case 21
Request:
{
  "ToBankIMD": "220556",
  "AccountNumberTo": "11600106799684"
}
Expected Response:
{
  "response": {
    "response_code": "95",
    "response_desc": "TRANSACTION REJECTED",
    "title-fetch": {
      "AccountTitleTo": "",
      "BankName": "",
      "ResponseCode": "95",
      "IBAN_MobileAccountNumber": "",
      "Amount": "000000001100",
      "STAN": "104867",
      "BranchNameTo": "",
      "Time": "140100",
      "TransmissionDateAndTime": "0302140100",
      "Reserved1": "",
      "Date": "0302",
      "Reserved3": "",
      "RRN": "002140104867",
      "Reserved2": "",
      "AuthorizationIdentificationResponse": "000000",
      "ResponseDetail": "TRANSACTION REJECTED",
      "ToBankIMD": "220556",
      "DateSettlement": "0303",
      "PAN": "0000000000000",
      "AccountNumberTo": "11600106799684"
    }
  }
}
