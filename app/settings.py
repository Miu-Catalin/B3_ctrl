def dacX_vol(dac_no):
    return {
                'name': f'DAC{dac_no}_vol',
                'register': dac_no,
                'position': 0,
                'length': 8,
                'definition': f'Volume of DAC{dac_no}, dB = -REG_VAL/2',
                'default_value': 0,  # max
                'acceptable_values': list(range(0, 255)),
                'constrains': None
            }

automute_lev_source = {
    'name': 'automute_lev_source',
    'register': 8,
    'position': 0,
    'length': 1,
    'definition': 'source for automute lev. I2S or DSD = 0 ; SPDIF = 1',
    'default_value': 0,  # I2S or DSD
    'acceptable_values': [0, 1],
    'constrains': None
}

automute_lev_dB = {
    'name': 'automute_lev_dB',
    'register': 8,
    'position': 1,
    'length': 7,
    'definition': 'automute level, trigger point. dB = -REG_VAL',
    'default_value': 0,  # 104
    'acceptable_values': list(range(0, 127)),
    'constrains': None
}

automute_time = {
    'name': 'automute_time',
    'register': 9,
    'position': 0,
    'length': 8,
    'definition': 'automute time, time in seconds = 2096896/(REG_VAL * DATA_CLK)',
    'default_value': 4,  # 101
    'acceptable_values': list(range(0, 255)),
    'constrains': None
}

serial_data_mode_bit = {
    'name': 'serial_data_mode_bit',
    'register': 10,
    'position': 0,
    'length': 2,
    'definition': '24/20/16/32 Bit for Serial Data Modes. b00 - 24bit, b01 - 20bit, b10 - 16bit, b11 - 32bit. Default: 32Bit',
    'default_value': 3,  # 11 -> 32 Bit
    'acceptable_values': list(range(0, 3)),
    'constrains': None
}

serial_data_mode_type = {
    'name': 'serial_data_mode_type',
    'register': 10,
    'position': 2,
    'length': 2,
    'definition': 'Serial Data Modes LJ/I2S/RJ. b00 - I2S, b01 - LJ, b10 - RJ, b11 - I2S. Default: I2S (b00)',
    'default_value': 0,  # 0 -> I2S
    'acceptable_values': list(range(0, 3)),
    'constrains': None
}

jitter_reduction_enable = {
    'name': 'jitter_reduction_enable',
    'register': 10,
    'position': 5,
    'length': 1,
    'definition': 'Jitter reduction. b0 - bypass and stop, *b1 - use .Default: Use jitter reduction',
    'default_value': 1,  # 1 -> use jitter reduction
    'acceptable_values': [0, 1],
    'constrains': None
}

bypass_deemphasis_filter = {
    'name': 'bypass_deemphasis_filter',
    'register': 10,
    'position': 6,
    'length': 1,
    'definition': 'Bypass deephasis filter. b0 - use de-emphasize, *b1 - do not use. Default: Use jitter reduction',
    'default_value': 1,  # 1 -> bypass
    'acceptable_values': [0, 1],
    'constrains': None
}

mute_all_dacs = {
    'name': 'mute_all_dacs',
    'register': 10,
    'position': 7,
    'length': 1,
    'definition': 'Mute all dacs. *b0 - unmute all DACs, b1 - mute. Default: unmute',
    'default_value': 0,  # 0 -> unmute
    'acceptable_values': [0, 1],
    'constrains': None
}

dpll_bandwidth = {
    'name': 'dpll_bandwidth',
    'register': 11,
    'position': 3,
    'length': 3,
    'definition': 'Dpll bandwidth. *b000 - no bandwith, *b001 - lowest bandwidth ... *111 - highest bandwidth. Default: b001 - lowest bandwith',
    'default_value': 1,  # b001 -> lowest bandwidth
    'acceptable_values': list(range(0, 7)),
    'constrains': None # de revazut
}



