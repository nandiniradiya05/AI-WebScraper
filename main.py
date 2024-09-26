import streamlit as st
from scrape import main, split_dom_content ,extract_html, clean_body_content
from parse import parse_with_ollama

st.title('AI WebScrapper')

website = st.text_input('Enter a website URL')

if st.button('Scrape'):
    st.write('Scraping...')
    result = main(website)
    body = extract_html(result)
    clean_content = clean_body_content(body)
    
    st.session_state.dom_content = clean_content
    
    with st.expander('View DOM Content'):
        st.text_area('DOM Content', clean_content, height=300)
    
    
if 'dom_content' in st.session_state:
    st.write('You can now parse the content')
    parse_description = st.text_area('Describe what you want to parse')
    
    if st.button('Parse'):
        print('Parsing the content...')
        dom_chunks = split_dom_content(st.session_state.dom_content)
        result = parse_with_ollama(dom_chunks, parse_description)
        st.write(result)