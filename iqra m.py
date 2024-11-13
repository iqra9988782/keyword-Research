import streamlit as st
import requests

# Function to simulate keyword analysis (you can integrate real APIs for this)
def keyword_analysis(keyword):
    # Example: Simulating a keyword analysis response
    # Normally you would call an API like Google Keyword Planner, SEMrush, etc. to get real data.
    return {
        "search_volume": 10000,  # Example search volume
        "competition": "Medium",  # Example competition level
        "suggestions": ["SEO tips", "SEO keyword research", "SEO optimization"]
    }

# Streamlit UI layout
def main():
    st.title("SEO Keyword Analyzer")
    st.write("Enter a keyword to analyze its search volume, competition, and related keywords.")
    
    # Keyword input field
    keyword = st.text_input("Enter Keyword:")

    # Clear previous output whenever new keyword is entered
    if 'keyword' in st.session_state:
        st.session_state['keyword'] = keyword
    
    if keyword:
        # Analyze the keyword
        data = keyword_analysis(keyword)

        # Show analysis results
        st.write(f"**Search Volume**: {data['search_volume']}")
        st.write(f"**Competition**: {data['competition']}")
        st.write("**Suggested Keywords**:")
        for suggestion in data["suggestions"]:
            st.write(suggestion)

        # Option to enter next keyword
        if st.button('Analyze Next Keyword'):
            st.session_state['keyword'] = ''
            st.experimental_rerun()

if __name__ == "__main__":
    main()
