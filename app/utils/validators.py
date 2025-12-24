import re

def validate_phone_number(phone: str) -> bool:
    """Validate Indian phone number"""
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, phone))

def validate_aadhaar_number(aadhaar: str) -> bool:
    """Validate Aadhaar number"""
    pattern = r'^\d{12}$'
    return bool(re.match(pattern, aadhaar))

def validate_pincode(pincode: str) -> bool:
    """Validate Indian PIN code"""
    pattern = r'^\d{6}$'
    return bool(re.match(pattern, pincode))