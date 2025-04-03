import streamlit as st
import csv

st.set_page_config(page_title="LLM Bioinformatics Interpreter", layout="centered")
st.title("🧬 LLM Bioinformatics Interpreter (Lite)")

uploaded_file = st.file_uploader("Upload your microarray CSV file", type="csv")

if uploaded_file:
    data = list(csv.reader(uploaded_file.read().decode("utf-8").splitlines()))
    headers = data[0]
    rows = data[1:]

    st.subheader("📊 Gene Expression Table")
    st.write(f"**{headers[0]:<10} | {headers[1]:<12} | {headers[2]:<12}**")
    for row in rows:
        st.text(f"{row[0]:<10} | {row[1]:<12} | {row[2]:<12}")

    prompt = f"""
You are a molecular biology LLM assistant. Analyze the following gene expression data:

{chr(10).join([", ".join(row) for row in data])}

Instructions:
- Identify significantly up- or downregulated genes.
- Suggest molecular roles.
- Propose a hypothesis for further investigation.
"""
    st.subheader("🧠 LLM Prompt")
    st.code(prompt)

    mock_response = """
- TP53 is downregulated in Condition B, indicating potential loss of tumor suppression.
- BRCA1 is upregulated, suggesting DNA repair activation.
- VEGF is highly upregulated, implying angiogenesis.
- EGFR is upregulated, indicating increased proliferation.

**Hypothesis:**  
Condition B reflects oncogenic transformation or hypoxic response triggering DNA repair and vascular pathways.
"""
    st.subheader("🔬 Simulated AI Response")
    st.write(mock_response)
else:
    st.info("Please upload a valid `.csv` file to begin.")
