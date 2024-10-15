Hướng dẫn sử dụng PDF Analyzer
1. Giới thiệu
PDF Analyzer là ứng dụng web sử dụng Streamlit để phân tích nội dung các file PDF. Ứng dụng trích xuất văn bản, phân tích bằng API Google Gemini và hiển thị các từ khóa quan trọng.

2. Cài đặt và chạy ứng dụng
2.1 Cài đặt môi trường
Windows:
Mở Command Prompt.
Tạo môi trường ảo và kích hoạt:
bash
Sao chép mã
python -m venv venv
venv\Scripts\activate
Cài đặt các thư viện:
bash
Sao chép mã
pip install streamlit PyPDF2 google-generativeai python-dotenv pandas plotly
Linux/macOS:
Mở Terminal.
Tạo và kích hoạt môi trường ảo:
bash
Sao chép mã
python3 -m venv venv
source venv/bin/activate
Cài đặt các thư viện:
bash
Sao chép mã
pip install streamlit PyPDF2 google-generativeai python-dotenv pandas plotly
2.2 Thiết lập API key
Tạo file .env trong thư mục dự án và thêm API key:

bash
Sao chép mã
GOOGLE_API_KEY=your_api_key_here
2.3 Chạy ứng dụng
Sử dụng lệnh sau để chạy ứng dụng:

bash
Sao chép mã
streamlit run app.py
3. Cấu trúc ứng dụng
Trích xuất văn bản từ PDF: extract_text_from_pdf().
Gửi văn bản đến API Gemini: call_gemini_api().
Phân tích và trích xuất từ khóa: analyze_research_document(), extract_keywords().
Tạo biểu đồ từ khóa: generate_word_cloud().
Lưu ý: Nếu API gặp lỗi, bạn có thể chọn mô hình khác trong file model.txt.

4. Hướng dẫn sử dụng
Tải file PDF và ứng dụng sẽ tự động phân tích.
Kết quả hiển thị gồm phân tích chi tiết và biểu đồ từ khóa.
Nhấp "Tải báo cáo dạng TEXT" để tải xuống kết quả.
5. Mở rộng và tùy chỉnh
Điều chỉnh prompt trong hàm analyze_research_document() để thay đổi cách phân tích.
Sử dụng thêm các component của Streamlit hoặc thêm tính năng như so sánh nhiều PDF.
