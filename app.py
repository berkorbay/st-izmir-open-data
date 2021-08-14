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

st.header("Notes & References")

st.markdown("""
- Read the story [here](https://medium.com/berk-orbay/streamlit-a-new-way-to-prototype-interactive-ui-in-python-92815dfd437b).
- This is a simple demo to use [Streamlit Share](https://streamlit.io/sharing)
- Streamlit Share basically takes the app code from a public Github repo ([Click to see source repo](https://github.com/berkorbay/st-izmir-open-data)). You can easily fork it and work on your own project.
- Data is taken with WEB API from [Izmir Municipality Open Data Portal](https://acikveri.bizizmir.com)
""")
