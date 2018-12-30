class Setting:

    from app.helpers import read_reg
    
    def __init__(self, reg_name):
        self.name = reg_name
        self.register = 'setting_register'
        self.position = 'setting_position'
        self.definition = 'something'
        self.default_value = 'setting_default_value'
        self.acceptable_values = ['value1', 'value2', 'value3']
        self.constrains = [
            {
                'setting_name': 'setting_ooo',
                'acceptable_values': ['value1', 'value2']
            },
            {
                'setting_name': 'setting_ooo',
                'acceptable_values': ['value1', 'value2']
            },
        ]
    
    def write_value(self, value):
        check_if_value_is_acceptable = True
        check_if_contrains_are_acceptable = True
        if check_if_value_is_acceptable and check_if_contrains_are_acceptable:
            original_reg = read_reg('name')
            modified_reg = 'something'
            bus.write_byte_data(bufallo, self.register, modified_reg)
            return 0
        return 1