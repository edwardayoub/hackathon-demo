import streamlit as st

st.title("Tools & Pipelines")

st.subheader("MaxFuse Integration")
st.write("""
**maxfuse** is a computational framework designed to integrate multiplexed imaging data 
with single-cell transcriptomic data. It enables cross-modality alignment and identification 
of shared cell phenotypes.
""")

# Example tools table
st.markdown("### Available Tools")
st.write("""
| Tool      | Input Data    | Output        | Approx. Duration | Link/Docs          |
|-----------|---------------|---------------|------------------|--------------------|
| maxfuse   | CODEX & scRNA | Integrated dataset, matched cell types | ~2-3h | [Docs](#) |
| Tool A    | CODEX only    | Cell phenotypes, spatial maps          | ~1h   | [Docs](#) |
| Tool B    | scRNA only    | Cluster annotations, gene markers      | ~30m  | [Docs](#) |
""")
