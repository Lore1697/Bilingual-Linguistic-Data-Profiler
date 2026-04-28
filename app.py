import streamlit as st
import pandas as pd
import altair as alt
from linguistic_profiler import analyze_text

st.title("Bilingual Linguistic Data Profiler")

st.write("Analyze Italian, English, and mixed-language text using basic NLP metrics.")
st.markdown("### Enter a text to analyze")
user_input = st.text_area("", placeholder="Type or paste your text here...")

if st.button("Analyze"):
    if user_input.strip():
        result = analyze_text(user_input)

        st.subheader("Analysis Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Language", result["language"])
            st.metric("Word Count", result["word_count"])

        with col2:
            st.metric("Unique Words", result["unique_words"])
            st.metric("Lexical Diversity", result["lexical_diversity"])

        st.subheader("Top Words")
        df = pd.DataFrame(result["top_words"], columns=["Word", "Count"])
        df = df.sort_values(by="Count", ascending=False)

        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
               x=alt.X("Word:N", sort="-y", title="Word"),
               y=alt.Y("Count:Q", title="Frequency"),
               tooltip=["Word", "Count"]
            )
            .properties(height=350)
        )
        st.altair_chart(chart, use_container_width=True)
        st.dataframe(df, use_container_width=True, hide_index=True)

    else:
        st.warning("Please enter some text.")