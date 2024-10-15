import streamlit as st
import PyPDF2
import google.generativeai as genai
import os
import re
from dotenv import load_dotenv
from google.api_core import exceptions as google_exceptions
import pandas as pd
import plotly.express as px
import time

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def call_gemini_api(prompt, max_retries=5, delay=2):
    for attempt in range(max_retries):
        try:
            model = genai.GenerativeModel('gemini-1.5-pro')
            response = model.generate_content(prompt)
            return response.text
        except google_exceptions.ResourceExhausted:
            if attempt < max_retries - 1:
                st.warning(f"Đã vượt quá giới hạn API. Đang thử lại (lần {attempt + 1}/{max_retries})...")
                time.sleep(delay)
            else:
                st.error("Không thể kết nối với API sau nhiều lần thử. Vui lòng thử lại sau.")
                return None
        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {str(e)}")
            return None
    return None

def analyze_research_document(text):
    prompt = f"""Phân tích tài liệu nghiên cứu sau và cung cấp thông tin về các mục sau:
    
    1. Tóm tắt những điểm nổi bật của tài liệu trong khoảng 300 từ.
    2. Những vấn đề nổi bật mà nghiên cứu đạt được và hạn chế của nghiên cứu.
    3. Các lý thuyết nghiên cứu được sử dụng trong tài liệu.
    4. Phương pháp nghiên cứu, đối tượng nghiên cứu và giả thuyết nghiên cứu.
    5. Đề xuất 3-5 hướng nghiên cứu tiếp theo dựa trên kết quả của nghiên cứu này.
    
    Tài liệu:
    {text}
    
    Hãy trình bày kết quả theo cấu trúc được đánh số như trên, với mỗi mục được trình bày rõ ràng và ngắn gọn."""
    return call_gemini_api(prompt)

def extract_keywords(text):
    prompt = f"""Từ văn bản sau, hãy trích xuất 10 từ khóa quan trọng nhất liên quan đến chủ đề nghiên cứu. 
    Chỉ liệt kê các từ khóa, mỗi từ khóa trên một dòng.

    Văn bản:
    {text}"""
    response = call_gemini_api(prompt)
    if response:
        return [keyword.strip() for keyword in response.split('\n') if keyword.strip()]
    return []

def generate_word_cloud(keywords):
    if not keywords:
        return None
    df = pd.DataFrame({'keyword': keywords, 'count': range(len(keywords), 0, -1)})
    fig = px.treemap(df, path=['keyword'], values='count', 
                     color='count', color_continuous_scale='Viridis',
                     title='Từ khóa quan trọng')
    return fig

def main():
    st.set_page_config(page_title="PDF Visualizer - Phân tích Nghiên cứu", layout="wide")
    
    st.title("PDF Visualizer - Phân tích Nghiên cứu")
    
    uploaded_file = st.file_uploader("Chọn một file PDF", type="pdf")
    
    if uploaded_file is not None:
        with st.spinner("Đang xử lý PDF..."):
            text = extract_text_from_pdf(uploaded_file)
            
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Phân tích Nghiên cứu")
            analysis = analyze_research_document(text)
            
            if analysis:
                # Định nghĩa các tiêu đề cho từng phần
                section_titles = [
                    "Tóm tắt những điểm nổi bật",
                    "Vấn đề nổi bật và hạn chế",
                    "Lý thuyết nghiên cứu",
                    "Phương pháp, đối tượng và giả thuyết nghiên cứu",
                    "Đề xuất hướng nghiên cứu tiếp theo"
                ]
                
                # Tách nội dung phân tích thành các phần
                sections = re.split(r'\n\d+\.', analysis)
                
                # Hiển thị từng phần với tiêu đề tương ứng
                for i, (title, content) in enumerate(zip(section_titles, sections[1:]), 1):
                    with st.expander(f"{i}. {title}", expanded=True):
                        st.write(content.strip())
            else:
                st.error("Không thể phân tích tài liệu. Vui lòng thử lại sau.")
        
        with col2:
            st.subheader("Từ khóa quan trọng")
            keywords = extract_keywords(text)
            if keywords:
                fig = generate_word_cloud(keywords)
                if fig:
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Không thể tạo biểu đồ từ khóa.")
            else:
                st.warning("Không thể trích xuất từ khóa. Vui lòng thử lại sau.")
        
        if analysis and keywords:
            st.subheader("Tải về báo cáo")
            report = f"""# Báo cáo Phân tích Nghiên cứu

    {analysis}

    ## Từ khóa quan trọng
    {', '.join(keywords)}
            """
            st.download_button(
                label="Tải báo cáo dạng TEXT",
                data=report,
                file_name="bao_cao_phan_tich.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()