"""Python file including functions that validates input data in monster.py file/app."""


# validate input value, value must be INT type and value > 0
def validate_int_value(int_value):
    """Must be INT type and value > 0"""
    if isinstance(int_value, int) and int_value > 0:
        return int_value
    else:
        if not isinstance(int_value, int):
            raise TypeError("Attribute must be integer type.")
        elif int_value <= 0:
            raise ValueError("Attribute must be greater than 0.")


# validates input of gold sack, value must be INT and value >=0
def validate_int_value_2(int_value):
    """Must be INT and value >=0"""
    if isinstance(int_value, int) and int_value >= 0:
        return int_value
    else:
        if not isinstance(int_value, int):
            raise TypeError("Attribute must be integer type.")
        elif int_value < 0:
            raise ValueError("Attribute must be greater than 0.")


# validates value of weapon damage
def validate_int_weapon_dmg_value(int_value):
    """Must be int and 0 < int_value <= 100"""
    if isinstance(int_value, float) and 0 < int_value <= 100:
        return int_value
    else:
        if not isinstance(int_value, int):
            raise TypeError("Attribute must be integer type.")
        elif 0 < int_value <= 100:
            raise ValueError("Attribute must be greater than 0 and lower or equal of 100.")


# validates float value of weapon attack speed
def validate_float_weapon_dmg_value(float_value):
    """Must be float value and 1.0 < int_value <= 4.0"""
    if isinstance(float_value, float) and 1 < float_value <= 4:
        return float_value
    else:
        if not isinstance(float_value, float):
            raise TypeError("Attribute must be integer type.")
        elif 1 < float_value <= 4:
            raise ValueError("Attribute must be greater than 0 and lower or equal of 100.")


# validate input value, value must be STR type
def validate_str_value(str_value):
    if isinstance(str_value, str):
        return str_value
    else:
        raise TypeError("Attribute must be string type.")
