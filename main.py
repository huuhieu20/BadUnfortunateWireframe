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
        {"id": "NA01", "name": "Naruto", "img": "https://w7.pngwing.com/pngs/516/865/png-transparent-naruto-uzumaki-sasuke-uchiha-sakura-haruno-kakashi-hatake-naruto-cartoon-fictional-character-thumbnail.png"},
        {"id": "NA02", "name": "Sasuke", "img": "https://w7.pngwing.com/pngs/806/774/png-transparent-sasuke-uchiha-naruto-uzumaki-sakura-haruno-kakashi-hatake-sasuke-uchiha-naruto-hand-manga-thumbnail.png"},
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

