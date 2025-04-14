import streamlit as st
import time

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(1000):
    latest_iteration.text(f'Iteration {i + 1}')
    
    # Progresso proporcional ao total (escala de 0 a 100)
    progress = int((i + 1) / 1000 * 100)
    bar.progress(progress)
    
    time.sleep(0.01)  # pode diminuir o tempo pra não demorar tanto
