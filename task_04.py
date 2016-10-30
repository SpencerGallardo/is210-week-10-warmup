#!/usr/bin/env pythong
# -*- coding: utf-8 -*-
"""Task 04 Week 10"""

import data

NEW_BAND = {
    'Buckingham Nicks': {
        'Lindsey Buckingham': ['guitar', 'vocals'],
        'Stevie Nicks': ['vocals', 'tambourine']
        }
    }

data.BANDS.update(NEW_BAND)

data.BANDS['Fleetwood Mac'].update({'Lindsey Buckingham': ['guitar', 'vocals'],
                                    'Stevie Nicks': ['vocals', 'tambourine']})
