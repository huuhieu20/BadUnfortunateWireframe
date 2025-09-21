import streamlit as st

# --- Sidebar ---
st.sidebar.title("Cửa hàng mô hình Anime")
st.sidebar.info(
    """
    📍 Địa chỉ: 123 Đường ABC, Hà Nội  
    📞 SĐT: 0987 654 321  
    📧 Email: shop@anime.vn
    """
)

# --- Tiêu đề chính ---
st.title("🛒 Chương trình quản lý cửa hàng đồ chơi")

# --- Các chủ đề ---
st.subheader("Chọn chủ đề mô hình:")
option = st.radio("Chủ đề", ["Dragon Ball", "Naruto", "One Piece"])

# --- Dữ liệu mô hình ---
models = {
    "Dragon Ball": [
        {"id": "DB01", "name": "Goku", "img": "https://w7.pngwing.com/pngs/46/38/png-transparent-goku-thumbnail.png"},
        {"id": "DB02", "name": "Vegeta", "img": "https://w7.pngwing.com/pngs/92/90/png-transparent-dragon-ball-z-vegeta-goku-gohan-dragon-ball-z-goku-child-gohan-thumbnail.png"},
        {"id": "DB03", "name": "Gohan", "img": "https://w7.pngwing.com/pngs/302/315/png-transparent-gohan-goku-vegeta-dragon-ball-dragon-ball-cartoon-thumbnail.png"}
    ],
    "Naruto": [
        {"id": "NA01", "name": "Naruto", "img": "https://www.google.com/imgres?q=m%C3%B4%20h%C3%ACnh%20naruto&imgurl=https%3A%2F%2Fdinotoystore.vn%2Fwp-content%2Fuploads%2F2023%2F05%2F350636998_264683536102104_7120706964712928931_n.jpg&imgrefurl=https%3A%2F%2Fdinotoystore.vn%2Fsan-pham%2Fmo-hinh-naruto-hien-nhan-thuat-evil-studio%2F&docid=KzkM625TxjqOuM&tbnid=sA9rtVh5rBAu0M&vet=12ahUKEwiT4_H3-OiPAxXni68BHXsjEnMQM3oECBsQAA..i&w=790&h=526&hcb=2&ved=2ahUKEwiT4_H3-OiPAxXni68BHXsjEnMQM3oECBsQAA"},
        {"id": "NA02", "name": "Sasuke", "img": "https://www.google.com/imgres?q=m%C3%B4%20h%C3%ACnh%20naruto&imgurl=https%3A%2F%2Fsneakerdaily.vn%2Fwp-content%2Fuploads%2F2024%2F03%2FMo-Hinh-Do-Choi-POP-MART-Naruto-Ninkai-Taisen-6941848247599-10.jpg&imgrefurl=https%3A%2F%2Fsneakerdaily.vn%2Fsan-pham%2Fmo-hinh-do-choi-pop-mart-naruto-ninkai-taisen-6941848247599%2F&docid=xiHLiMzoHaDd4M&tbnid=8ht3Y-L_SbAvNM&vet=12ahUKEwiT4_H3-OiPAxXni68BHXsjEnMQM3oECBwQAA..i&w=1200&h=1200&hcb=2&ved=2ahUKEwiT4_H3-OiPAxXni68BHXsjEnMQM3oECBwQAA"},
        {"id": "NA03", "name": "Kakashi", "img": "https://w7.pngwing.com/pngs/620/978/png-transparent-kakashi-hatake-naruto-uzumaki-sasuke-uchiha-sakura-haruno-naruto-cartoon-comic-book-fictional-character-thumbnail.png"}
    ],
    "One Piece": [
        {"id": "OP01", "name": "Luffy", "img": "https://w7.pngwing.com/pngs/101/513/png-transparent-monkey-d-luffy-nami-roronoa-zoro-one-piece-pirate-warriors-3-luffy-png-material-computer-wallpaper-cartoon-thumbnail.png"},
        {"id": "OP02", "name": "Zoro", "img": "https://w7.pngwing.com/pngs/731/431/png-transparent-roronoa-zoro-monkey-d-luffy-one-piece-world-seeker-one-piece-treasure-cruise-zoro-pirate-fictional-character-thumbnail.png"},
        {"id": "OP03", "name": "Nami", "img": "https://w7.pngwing.com/pngs/644/518/png-transparent-nami-monkey-d-luffy-roronoa-zoro-one-piece-grand-battle-anime-fictional-character-cartoon-thumbnail.png"}
    ]
}

# --- Hiển thị danh sách mô hình ---
st.subheader(f"Danh sách mô hình: {option}")
cols = st.columns(3)
for i, model in enumerate(models[option]):
    with cols[i % 3]:
        st.image(model["img"], caption=f"{model['name']} (Mã: {model['id']})", use_container_width=True)

# --- Form đặt hàng ---
st.subheader("📝 Đặt hàng")
with st.form("order_form"):
    model_id = st.text_input("Nhập mã mô hình")
    quantity = st.number_input("Số lượng", min_value=1, value=1)
    name = st.text_input("Họ và tên")
    phone = st.text_input("Số điện thoại")
    address = st.text_area("Địa chỉ giao hàng")
    submit = st.form_submit_button("Xác nhận đặt hàng")

if submit:
    if model_id and name and phone and address:
        st.success("✅ Đặt hàng thành công!")
        st.write("### Hóa đơn")
        st.write(f"- Mã mô hình: {model_id}")
        st.write(f"- Số lượng: {quantity}")
        st.write(f"- Khách hàng: {name}")
        st.write(f"- SĐT: {phone}")
        st.write(f"- Địa chỉ: {address}")
        st.write("Cảm ơn bạn đã mua hàng 🛍️")
    else:
        st.error("⚠️ Vui lòng nhập đầy đủ thông tin trước khi xác nhận.")

