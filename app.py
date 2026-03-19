import streamlit as st
from gtts import gTTS
import io

# Giao diện chuẩn giáo án
st.set_page_config(page_title="Hán Ngữ TTS Professional", page_icon="🎙️")
st.title("🎙️ Hệ thống Luyện phát âm Hán Ngữ")
st.markdown("---")

# Ô nhập văn bản
text_to_read = st.text_area("Dán nội dung Hán tự (Bản sạch) vào đây:", height=250, placeholder="Ví dụ: 1. 安。山，爬山。")

# Thanh điều chỉnh tốc độ (Mặc định 0.5 cho bạn)
speed_option = st.select_slider("Tốc độ đọc:", options=[0.25, 0.5, 0.75, 1.0], value=0.5)

if st.button("🚀 BẮT ĐẦU ĐỌC"):
    if text_to_read:
        with st.spinner('Đang tạo giọng đọc chuẩn Bắc Kinh...'):
            # Chuyển đổi tốc độ cho gTTS (True là chậm ~0.5, False là bình thường)
            is_slow = True if speed_option <= 0.5 else False
            
            tts = gTTS(text=text_to_read, lang='zh-cn', slow=is_slow)
            
            # Lưu vào bộ nhớ đệm (không tốn dung lượng máy)
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            
            # Phát âm thanh
            st.audio(mp3_fp, format='audio/mp3')
            
            # Nút tải file
            st.download_button(
                label="📥 TẢI FILE NGHE (.MP3)",
                data=mp3_fp.getvalue(),
                file_name="giao_an_tieng_trung.mp3",
                mime="audio/mp3"
            )
    else:
        st.error("Chưa có nội dung để đọc!")

st.sidebar.info("App này chạy độc lập, không tốn Quota AI Studio, dùng vĩnh viễn.")
