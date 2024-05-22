#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 13:14:37 2023

@author: mayk
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime


from entsoe import EntsoeRawClient
from entsoe import EntsoePandasClient

client = EntsoePandasClient(api_key="4a2ed80d-d974-47ef-8d11-778e05f67850")

start = pd.Timestamp('20230101', tz='Europe/Brussels')
end = pd.Timestamp('20230102', tz='Europe/Brussels') # '20230101T23'
country_code = 'NL'  # Netherlands
#country_code_from = 'FR'  # France
#country_code_to = 'DE_LU' # Germany-Luxembourg
type_marketagreement_type = 'A01'
contract_marketagreement_type = "A01"


DA = client.query_day_ahead_prices(country_code, start=start, end=end)
#DA = pd.DataFrame(DA, columns=['date','price'])
DA.to_csv('outfile_DA.csv', header=['DA_price'])

imb = client.query_imbalance_prices(country_code, start=start,end=end, psr_type=None)
imb = imb.drop('Short', axis=1)
imb.to_csv('outfile_imb.csv', header=['imb_price'])

