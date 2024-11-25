#!/usr/bin/python3

def roman_to_int(roman_string):
	num = 0
	prev = ''
	for i in roman_string:
		match i:
			case 'M':
				if 0 < roman_to_int(prev) < 1000:
					num -= value + roman_to_int(prev)
				value = 1000
				num += value
				prev = i
			case 'D':
				if 0 < roman_to_int(prev) < 500:
					num -= value + roman_to_int(prev)
				value = 500
				num += value
				prev = i
			case 'C':
				if 0 < roman_to_int(prev) < 100:
					num -= value + roman_to_int(prev)
				value = 100
				num += value
				prev = i
			case 'L':
				if 0 < roman_to_int(prev) < 50:
					num -= value + roman_to_int(prev)
				value = 50
				num += value
				prev = i
			case 'X':
				if 0 < roman_to_int(prev) < 10:
					num -= value + roman_to_int(prev)
				value = 10
				num += value
				prev = i
			case 'V':
				if 0 < roman_to_int(prev) < 5:
					num -= value + roman_to_int(prev)
				value = 5
				num += value
				prev = i
			case 'I':
				value = 1
				num += value
				prev = i
	return num

def run_tests():
    test_cases = [
        ("I", 1),
        ("V", 5),
        ("X", 10),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("VII", 7),
        ("VIII", 8),
        ("XIV", 14),
        ("XX", 20),
        ("XXX", 30),
        ("XLV", 45),
        ("LXXXVII", 87),
        ("XCIV", 94),
        ("CXXXIV", 134),
        ("CDXCIX", 499),
        ("DCCVII", 707),
        ("MMXXIV", 2024),
        ("MMMCMXCIX", 3999),
        ("II", 2),
        ("III", 3),
    ]
    
    for roman, expected in test_cases:
        result = roman_to_int(roman)
        print(f"Roman: {roman}, Expected: {expected}, Result: {result}")
        
run_tests()
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))