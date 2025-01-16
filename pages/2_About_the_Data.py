import streamlit as st

st.title("About the Data")

st.write("""
The hackathon focuses on integrating and analyzing two complementary datasets:
- **CODEX Imaging Data**: Provides spatially resolved protein expression for ~35 colorectal cancer patients.
- **scRNA-seq Data**: Captures transcriptomic profiles for single cells from the same patients.
""")

st.write("""
### Dataset Details
- **17 patients with Crohn's-like reaction (CLR)**:
  - High amounts of Tertiary Lymphoid Structures (TLSs).
  - Associated with improved overall survival.
- **18 patients with Diffuse Inflammatory Infiltration (DII)**:
  - Lacking TLSs.
  - Less favorable clinical outcomes.
""")

st.markdown("#### Importance of the Data")
st.write("""
These datasets offer a unique opportunity to:
- Study the formation and role of TLSs in the tumor microenvironment.
- Identify key markers driving TLS formation (e.g., CXCL13, CCL19, and CCL21).
- Discover novel insights into immune-tumor interactions.
""")

st.markdown("#### Accessing the Data")
st.write("""
- **CODEX Imaging Files**: Placeholder for links.
- **scRNA-seq Files**: Placeholder for links.
- **Instructions for Download**: Placeholder for a step-by-step guide.
""")
st.download_button("Download CODEX Example Data (Placeholder)", data="Sample data", file_name="codex_sample_data.txt")
st.download_button("Download scRNA-seq Example Data (Placeholder)", data="Sample scRNA-seq data", file_name="scrna_sample_data.txt")

st.markdown("#### Example Use Cases")
st.write("""
Participants can:
1. Preprocess and normalize data for integration using MaxFuse.
2. Investigate the role of TLS-related genes (e.g., CXCL13, CCL19, CCL21).
3. Compare CLR and DII patient datasets to uncover immune-biomarker patterns.
4. Visualize spatial relationships and transcriptomic profiles.
""")
