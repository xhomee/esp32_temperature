"""
Micropython (Raspberry Pi Pico)
下面只包含94个字符
"""
textFont={
    0:[0x00, 0x3E, 0x51, 0x49, 0x45, 0x3E, 0x00],
    1:[0x00, 0x00, 0x42, 0x7F, 0x40, 0x00, 0x00],
    2:[0x00, 0x62, 0x51, 0x49, 0x49, 0x46, 0x00],
    3:[0x00, 0x21, 0x41, 0x49, 0x4D, 0x33, 0x00],
    4:[0x00, 0x18, 0x14, 0x12, 0x7F, 0x10, 0x00],
    5:[0x00, 0x27, 0x45, 0x45, 0x45, 0x39, 0x00],
    6:[0x00, 0x3C, 0x4A, 0x49, 0x49, 0x31, 0x00],
    7:[0x00, 0x01, 0x71, 0x09, 0x05, 0x03, 0x00],
    8:[0x00, 0x36, 0x49, 0x49, 0x49, 0x36, 0x00],
    9:[0x00, 0x46, 0x49, 0x49, 0x29, 0x1E, 0x00],
    10:[0x00, 0x24, 0x54, 0x54, 0x38, 0x40, 0x00],
    11:[0x00, 0x7F, 0x28, 0x44, 0x44, 0x38, 0x00],
    12:[0x00, 0x38, 0x44, 0x44, 0x44, 0x08, 0x00],
    13:[0x00, 0x38, 0x44, 0x44, 0x28, 0x7F, 0x00],
    14:[0x00, 0x38, 0x54, 0x54, 0x54, 0x08, 0x00],
    15:[0x00, 0x08, 0x7E, 0x09, 0x09, 0x02, 0x00],
    16:[0x00, 0x98, 0xA4, 0xA4, 0xA4, 0x78, 0x00],
    17:[0x00, 0x7F, 0x08, 0x04, 0x04, 0x78, 0x00],
    18:[0x00, 0x00, 0x00, 0x79, 0x00, 0x00, 0x00],
    19:[0x00, 0x00, 0x80, 0x88, 0x79, 0x00, 0x00],
    20:[0x00, 0x7F, 0x10, 0x28, 0x44, 0x40, 0x00],
    21:[0x00, 0x00, 0x41, 0x7F, 0x40, 0x00, 0x00],
    22:[0x00, 0x78, 0x04, 0x78, 0x04, 0x78, 0x00],
    23:[0x00, 0x04, 0x78, 0x04, 0x04, 0x78, 0x00],
    24:[0x00, 0x38, 0x44, 0x44, 0x44, 0x38, 0x00],
    25:[0x00, 0xFC, 0x24, 0x24, 0x24, 0x18, 0x00],
    26:[0x00, 0x18, 0x24, 0x24, 0x24, 0xFC, 0x00],
    27:[0x00, 0x04, 0x78, 0x04, 0x04, 0x08, 0x00],
    28:[0x00, 0x48, 0x54, 0x54, 0x54, 0x24, 0x00],
    29:[0x00, 0x04, 0x3F, 0x44, 0x44, 0x24, 0x00],
    30:[0x00, 0x3C, 0x40, 0x40, 0x3C, 0x40, 0x00],
    31:[0x00, 0x1C, 0x20, 0x40, 0x20, 0x1C, 0x00],
    32:[0x00, 0x3C, 0x40, 0x3C, 0x40, 0x3C, 0x00],
    33:[0x00, 0x44, 0x28, 0x10, 0x28, 0x44, 0x00],
    34:[0x00, 0x9C, 0xA0, 0xA0, 0x90, 0x7C, 0x00],
    35:[0x00, 0x44, 0x64, 0x54, 0x4C, 0x44, 0x00],
    36:[0x00, 0x7C, 0x12, 0x11, 0x12, 0x7C, 0x00],
    37:[0x00, 0x7F, 0x49, 0x49, 0x49, 0x36, 0x00],
    38:[0x00, 0x3E, 0x41, 0x41, 0x41, 0x22, 0x00],
    39:[0x00, 0x7F, 0x41, 0x41, 0x41, 0x3E, 0x00],
    40:[0x00, 0x7F, 0x49, 0x49, 0x49, 0x41, 0x00],
    41:[0x00, 0x7F, 0x09, 0x09, 0x09, 0x01, 0x00],
    42:[0x00, 0x3E, 0x41, 0x51, 0x51, 0x72, 0x00],
    43:[0x00, 0x7F, 0x08, 0x08, 0x08, 0x7F, 0x00],
    44:[0x00, 0x00, 0x41, 0x7F, 0x41, 0x00, 0x00],
    45:[0x00, 0x20, 0x40, 0x41, 0x3F, 0x01, 0x00],
    46:[0x00, 0x7F, 0x08, 0x14, 0x22, 0x41, 0x00],
    47:[0x00, 0x7F, 0x40, 0x40, 0x40, 0x40, 0x00],
    48:[0x00, 0x7F, 0x02, 0x0C, 0x02, 0x7F, 0x00],
    49:[0x00, 0x7F, 0x04, 0x08, 0x10, 0x7F, 0x00],
    50:[0x00, 0x3E, 0x41, 0x41, 0x41, 0x3E, 0x00],
    51:[0x00, 0x7F, 0x09, 0x09, 0x09, 0x06, 0x00],
    52:[0x00, 0x3E, 0x41, 0x51, 0x21, 0x5E, 0x00],
    53:[0x00, 0x7F, 0x09, 0x19, 0x29, 0x46, 0x00],
    54:[0x00, 0x26, 0x49, 0x49, 0x49, 0x32, 0x00],
    55:[0x00, 0x01, 0x01, 0x7F, 0x01, 0x01, 0x00],
    56:[0x00, 0x3F, 0x40, 0x40, 0x40, 0x3F, 0x00],
    57:[0x00, 0x1F, 0x20, 0x40, 0x20, 0x1F, 0x00],
    58:[0x00, 0x7F, 0x20, 0x18, 0x20, 0x7F, 0x00],
    59:[0x00, 0x63, 0x14, 0x08, 0x14, 0x63, 0x00],
    60:[0x00, 0x03, 0x04, 0x78, 0x04, 0x03, 0x00],
    61:[0x00, 0x61, 0x51, 0x49, 0x45, 0x43, 0x00],
    62:[0x00, 0x00, 0x00, 0x5F, 0x00, 0x00, 0x00],
    63:[0x00, 0x00, 0x07, 0x00, 0x07, 0x00, 0x00],
    64:[0x00, 0x14, 0x7F, 0x14, 0x7F, 0x14, 0x00],
    65:[0x00, 0x24, 0x2E, 0x7B, 0x2A, 0x12, 0x00],
    66:[0x00, 0x23, 0x13, 0x08, 0x64, 0x62, 0x00],
    67:[0x00, 0x36, 0x49, 0x56, 0x20, 0x50, 0x00],
    68:[0x00, 0x00, 0x04, 0x03, 0x01, 0x00, 0x00],
    69:[0x00, 0x00, 0x1C, 0x22, 0x41, 0x00, 0x00],
    70:[0x00, 0x00, 0x41, 0x22, 0x1C, 0x00, 0x00],
    71:[0x00, 0x22, 0x14, 0x7F, 0x14, 0x22, 0x00],
    72:[0x00, 0x08, 0x08, 0x7F, 0x08, 0x08, 0x00],
    73:[0x00, 0x40, 0x30, 0x10, 0x00, 0x00, 0x00],
    74:[0x00, 0x08, 0x08, 0x08, 0x08, 0x08, 0x00],
    75:[0x00, 0x20, 0x10, 0x08, 0x04, 0x02, 0x00],
    76:[0x00, 0x00, 0x36, 0x36, 0x00, 0x00, 0x00],
    77:[0x00, 0x40, 0x36, 0x36, 0x00, 0x00, 0x00],
    78:[0x00, 0x08, 0x14, 0x22, 0x41, 0x00, 0x00],
    79:[0x00, 0x14, 0x14, 0x14, 0x14, 0x14, 0x00],
    80:[0x00, 0x00, 0x41, 0x22, 0x14, 0x08, 0x00],
    81:[0x00, 0x02, 0x01, 0x59, 0x05, 0x02, 0x00],
    82:[0x00, 0x3E, 0x41, 0x5D, 0x55, 0x5E, 0x00],
    83:[0x00, 0x08, 0x36, 0x41, 0x00, 0x00, 0x00],
    84:[0x00, 0x00, 0x00, 0x77, 0x00, 0x00, 0x00],
    85:[0x00, 0x00, 0x00, 0x41, 0x36, 0x08, 0x00],
    86:[0x00, 0x08, 0x04, 0x08, 0x10, 0x08, 0x00],
    87:[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    88:[0x00, 0x00, 0x60, 0x60, 0x00, 0x00, 0x00],
    89:[0x00, 0x04, 0x02, 0x7F, 0x02, 0x04, 0x00],
    90:[0x00, 0x08, 0x1C, 0x2A, 0x08, 0x08, 0x00],
    91:[0x00, 0x00, 0x00, 0x01, 0x02, 0x04, 0x00],
    92:[0x00, 0x7F, 0x7F, 0x41, 0x41, 0x00, 0x00],
    93:[0x00, 0x02, 0x04, 0x08, 0x10, 0x20, 0x00],
    94:[0x00, 0x00, 0x41, 0x41, 0x7F, 0x7F, 0x00],
}
