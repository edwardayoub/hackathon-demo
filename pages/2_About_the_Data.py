import streamlit as st

st.title("About the Data")
st.write("""
The primary dataset includes CODEX imaging data from 35 advanced-stage colorectal cancer patients:
- **17 patients with Crohn's-like reaction (CLR)**: High amounts of tertiary lymphoid structures (TLS)
- **18 patients with diffuse inflammatory infiltration (DII)**: No TLS
""")

st.write("""
These samples were selected from an initial cohort of 715 CRC patients, matched for age, sex, 
and tumor characteristics. Notably, CLR patients exhibited better overall survival.
""")

st.markdown("#### Accessing the Data")
st.write("""
- CODEX imaging files (placeholder links)
- scRNA dataset files (placeholder links)
- Instructions for downloading (placeholder)
""")
st.download_button("Download CODEX Example Data (Placeholder)", data="Sample data", file_name="codex_sample_data.txt")
