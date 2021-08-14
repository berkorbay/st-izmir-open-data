import streamlit as st
import requests
import json
import os
import pandas as pd
from datetime import datetime, timedelta
from funs import get_prices

st.title("Fruit & Vegetable Prices at Izmir Wholesale Market")

st.session_state['cur_date'] = st.date_input("Choose Date",value=datetime.today() - timedelta(days=1),max_value=datetime.today() - timedelta(days=1))

price_df = get_prices(str(st.session_state['cur_date']))

st.table(price_df)
