import streamlit as st
import numpy as np 
import pandas as pd

st.title(" UM TESTE SIMPLES")
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=("col %d" % i for i in range(20)))

st.dataframe(dataframe)
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
