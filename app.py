import streamlit as st
import random

# Cấu hình trang
st.set_page_config(
    page_title="Món Quà Valentine Cho Minh Thùy",
    page_icon="💝",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS và Animation
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;700&family=Pacifico&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #ffeef8 0%, #ffe0f0 50%, #ffd4e8 100%);
        background-attachment: fixed;
    }
    
    /* ===== GIFT BOX ===== */
    .gift-box {
        text-align: center;
        padding: 3rem;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 30px;
        box-shadow: 0 12px 48px rgba(233, 30, 99, 0.3);
        border: 4px solid #f8bbd0;
        transition: transform 0.3s ease;
        animation: slideUp 0.8s ease-out;
    }
    
    .gift-box:hover {
        transform: scale(1.05);
    }
    
    .gift-emoji {
        font-size: 5rem;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* ===== BUTTON EFFECTS ===== */
    .stButton>button {
        background: linear-gradient(135deg, #f06292 0%, #e91e63 100%);
        color: white;
        border: none;
        padding: 1rem 3rem;
        border-radius: 50px;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(233, 30, 99, 0.4);
        transition: all 0.3s ease;
        font-family: 'Dancing Script', cursive;
        animation: buttonPulse 2s ease-in-out infinite;
    }
    
    @keyframes buttonPulse {
        0%, 100% { box-shadow: 0 4px 15px rgba(233, 30, 99, 0.4); }
        50% { box-shadow: 0 4px 25px rgba(233, 30, 99, 0.8); }
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 6px 30px rgba(233, 30, 99, 0.9);
    }
    
    .stButton>button:active {
        transform: scale(0.95);
    }
    
    /* ===== EXPLOSION ANIMATION (CHẠY 1 LẦN) ===== */
    .explosion-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        background: rgba(0, 0, 0, 0.9);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        animation: overlayFadeOut 0.5s ease 2.5s forwards;
    }
    
    @keyframes overlayFadeOut {
        to { 
            opacity: 0; 
            visibility: hidden; 
            pointer-events: none; 
        }
    }
    
    .explosion-heart {
        font-size: 10rem;
        animation: heartExplosion 2s ease-out forwards;
        filter: drop-shadow(0 0 50px rgba(233, 30, 99, 1));
    }
    
    @keyframes heartExplosion {
        0% {
            transform: scale(0.5);
            opacity: 0;
        }
        30% {
            transform: scale(1.2);
            opacity: 1;
        }
        50% {
            transform: scale(1) rotate(10deg);
        }
        70% {
            transform: scale(1) rotate(-10deg);
        }
        100% {
            transform: scale(1) rotate(0deg);
            opacity: 1;
        }
    }
    
    /* Fireworks - CHẠY 1 LẦN */
    .firework {
        position: fixed;
        font-size: 2rem;
        animation: fireworkBurst 1.5s ease-out forwards;
    }
    
    @keyframes fireworkBurst {
        0% {
            opacity: 1;
            transform: translate(0, 0) scale(0);
        }
        50% {
            opacity: 1;
        }
        100% {
            opacity: 0;
            transform: translate(var(--tx), var(--ty)) scale(1);
        }
    }
    
    /* Love text - CHẠY 1 LẦN */
    .love-text {
        font-family: 'Pacifico', cursive;
        font-size: 5rem;
        color: #ff1744;
        text-shadow: 0 0 30px rgba(255, 23, 68, 0.8);
        animation: loveAppear 2s ease-out forwards;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    
    @keyframes loveAppear {
        0% {
            opacity: 0;
            transform: translate(-50%, -50%) scale(0) rotate(-180deg);
        }
        60% {
            opacity: 1;
            transform: translate(-50%, -50%) scale(1.2) rotate(10deg);
        }
        100% {
            opacity: 1;
            transform: translate(-50%, -50%) scale(1) rotate(0deg);
        }
    }
    
    /* ===== MEGA EXPLOSION (2 LẦN) ===== */
    .mega-explosion {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        background: rgba(0, 0, 0, 0.95);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 10000;
        animation: megaOverlayFadeOut 0.5s ease 4s forwards;
    }
    
    @keyframes megaOverlayFadeOut {
        to { 
            opacity: 0; 
            visibility: hidden; 
            pointer-events: none; 
        }
    }
    
    .mega-heart {
        font-size: 15rem;
        animation: megaHeartExplosion 2s ease-out forwards;
        filter: drop-shadow(0 0 80px rgba(233, 30, 99, 1));
    }
    
    @keyframes megaHeartExplosion {
        0% {
            transform: scale(0);
            opacity: 0;
        }
        20% {
            transform: scale(2);
            opacity: 1;
        }
        40% {
            transform: scale(1.5) rotate(15deg);
        }
        60% {
            transform: scale(1.5) rotate(-15deg);
        }
        80% {
            transform: scale(1.5) rotate(5deg);
        }
        100% {
            transform: scale(1.5) rotate(0deg);
            opacity: 1;
        }
    }
    
    .fool-text {
        font-family: 'Pacifico', cursive;
        font-size: 6rem;
        color: #ff1744;
        text-shadow: 0 0 50px rgba(255, 23, 68, 1);
        animation: foolAppear 1.5s ease-out 2s both;
        margin-top: 2rem;
    }
    
    @keyframes foolAppear {
        0% {
            opacity: 0;
            transform: scale(0) rotate(-360deg);
        }
        70% {
            opacity: 1;
            transform: scale(1.3) rotate(10deg);
        }
        100% {
            opacity: 1;
            transform: scale(1) rotate(0deg);
        }
    }
    
    /* Mega fireworks - CHẠY 1 LẦN */
    .mega-firework {
        position: fixed;
        font-size: 3rem;
        animation: megaFireworkBurst 2s ease-out forwards;
    }
    
    @keyframes megaFireworkBurst {
        0% {
            opacity: 1;
            transform: translate(0, 0) scale(0) rotate(0deg);
        }
        50% {
            opacity: 1;
        }
        100% {
            opacity: 0;
            transform: translate(var(--tx), var(--ty)) scale(1.5) rotate(360deg);
        }
    }
    
    /* ===== FLYING HEARTS ===== */
    .flying-heart {
        position: fixed;
        font-size: 3rem;
        pointer-events: none;
        z-index: 9998;
        animation: flyAway 2s ease-out forwards;
    }
    
    @keyframes flyAway {
        0% {
            opacity: 1;
            transform: translate(0, 0) scale(1) rotate(0deg);
        }
        100% {
            opacity: 0;
            transform: translate(var(--fx), var(--fy)) scale(0.3) rotate(var(--fr));
        }
    }
    
    /* ===== MESSAGE DISPLAY ===== */
    .romantic-text {
        font-family: 'Dancing Script', cursive;
        color: #d81b60;
        font-size: 1.5rem;
        line-height: 1.8;
        text-align: center;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(233, 30, 99, 0.2);
        border: 3px solid #f48fb1;
        margin: 2rem 0;
        animation: messageReveal 1s ease-out;
    }
    
    @keyframes messageReveal {
        0% {
            opacity: 0;
            transform: scale(0.8) translateY(20px);
        }
        100% {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }
    
    /* Floating hearts */
    .floating-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    }
    
    .floating-heart {
        position: absolute;
        font-size: 2rem;
        opacity: 0.3;
        animation: floatHearts 10s infinite ease-in-out;
    }
    
    @keyframes floatHearts {
        0%, 100% {
            transform: translateY(0) translateX(0) rotate(0deg);
        }
        25% {
            transform: translateY(-20px) translateX(10px) rotate(5deg);
        }
        50% {
            transform: translateY(-40px) translateX(-10px) rotate(-5deg);
        }
        75% {
            transform: translateY(-20px) translateX(5px) rotate(3deg);
        }
    }
    
    .love-message {
        font-family: 'Dancing Script', cursive;
        color: #c2185b;
        font-size: 1.8rem;
        text-align: center;
        margin: 1rem 0;
    }
    
    .footer-text {
        font-family: 'Dancing Script', cursive;
        color: #ec407a;
        text-align: center;
        font-size: 0.9rem;
        margin-top: 2rem;
        opacity: 0.7;
    }
    
    /* ===== HIDE STREAMLIT ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .main-title {
        font-family: 'Pacifico', cursive;
        color: #e91e63;
        text-align: center;
        font-size: 3rem;
        text-shadow: 2px 2px 4px rgba(233, 30, 99, 0.3);
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
</style>
""", unsafe_allow_html=True)

# Danh sách lời yêu thương
love_messages = [
    """ Bé minhthuy ơi! 
    Anh muốn nói với em rằng: anh cảm ơn bé vì món quà hôm nay bé tặng anh,
    anh nhớ bé và iu bé càng ngày càng nhiều rồi 
    Yêu em nhiều lắm! 💖""",
    
    """Bé iu của anh! 
    Anh biết anh không giỏi cũng như xấu nhưng anh sẽ cố gắng đẹp hơn.
    (tuy là lời hứa nhất thời nhưng sẽ thành hiện thực ở ngày không xa ^v^) 
    Cảm ơn em đã đến bên anh. Forever yours! ❤️""",
    
    """Người yêu của anh, 
    Valentine này anh chẳng biết nói gì cho hoa mỹ,
    chỉ biết là từ khi có em,cuộc sống bớt nhạt, 
    bớt buồn,và thêm rất nhiều tiếng cười. 
    Anh hứa sẽ luôn yêu thương và chăm sóc em thật tốt. 🌹""",
    
    """Bé iu  , 
    Valentine chỉ là một ngày trong năm, nhưng anh mong rằng từ hôm nay đến những ngày rất rất lâu sau này,
    em vẫn luôn là người luôn làm phiền anh bởi những câu chuyện em muốn kể, 
    và nằm với nhau cùng ôm nhau ngủ. 
    Mãi yêu em! 💕""",
    
    """nhóc Minhthuy của anh ơi! 
    Anh chỉ muốn nói một điều thật đơn giản: 
    Em là tất cả những gì anh cần, là niềm hạnh phúc của anh. 
    Yêu nhóc , Minhthuy ngốc ! 😘""",
    
    """Bé Minhthuy xinh đẹp của anh, 
    Cảm ơn em đã luôn ở bên anh, động viên anh mỗi khi anh mệt mỏi. 
    Em là nguồn động lực lớn nhất của anh. 
    Anh yêu em vô cùng! 💝""",
    
    """Minhthuy thân yêu, 
    Anh làm cái này tuy có sài AI, Chat GPT nhưng thật sự anh cũng rất nhọc công để làm 
    và tìm hiểu nó chỉ mong em vui mãi. hè hè  
    Anh sẽ luôn iu bé moa moa 💗""",
    
    """Em yêu ơi, 
    Anh biết Valentine chỉ là một ngày trong năm, 
    nhưng với anh, mỗi ngày bên em đều là ngày hạnh phúc nhất. 
    Yêu em nhiều lắm, Minhthuy của anh! 🥰"""
]

# Session state
if 'screen' not in st.session_state:
    st.session_state.screen = 'gift'
if 'love_message' not in st.session_state:
    st.session_state.love_message = ""
if 'love_count' not in st.session_state:
    st.session_state.love_count = 0
if 'show_explosion' not in st.session_state:
    st.session_state.show_explosion = False
if 'show_fool' not in st.session_state:
    st.session_state.show_fool = False

def generate_love_message() -> str:
    return random.choice(love_messages)

# ===== GIFT SCREEN =====
def show_gift():
    st.markdown("""
    <div class="floating-hearts">
        <div class="floating-heart" style="top: 10%; left: 10%; animation-delay: 0s;">❤️</div>
        <div class="floating-heart" style="top: 20%; right: 15%; animation-delay: 2s;">💕</div>
        <div class="floating-heart" style="bottom: 20%; left: 20%; animation-delay: 4s;">💖</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h1 class='main-title'>💝</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='gift-box'>
        <div class='gift-emoji'>🎁</div>
        <h2 style='color: #e91e63; font-family: "Pacifico", cursive; margin: 1rem 0;'>
            Bé Iu Minh Thùy ơi!
        </h2>
        <p style='color: #666; font-size: 1.2rem; margin: 1rem 0;'>
            Anh có một món quà bí mật dành cho em...
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎁 Mở quà ngay 💖", use_container_width=True):
            st.session_state.show_explosion = True
            st.session_state.love_message = generate_love_message()
            st.session_state.screen = 'message'
            st.rerun()

# ===== MESSAGE WITH EXPLOSION =====
def show_message():
    # Mega explosion (2 LẦN - ĐÃ ĐỔI TỪ 10 LẦN)
    if st.session_state.show_fool:
        st.markdown("""
        <div class="mega-explosion">
            <div class="mega-heart">💖</div>
            <div class="fool-text">Đồ Ngốc! 😝 Biết minhthuy iu anh rùi</div>
        </div>
        """, unsafe_allow_html=True)
        
        fireworks_html = ""
        for i in range(40):
            x = random.randint(-400, 400)
            y = random.randint(-400, 400)
            delay = random.uniform(0, 2)
            emoji = random.choice(['❤️', '💕', '💖', '💗', '💝', '💘', '😝', '🥰', '😍'])
            fireworks_html += f"""
            <div class="mega-firework" style="
                left: 50%; 
                top: 50%; 
                --tx: {x}px; 
                --ty: {y}px;
                animation-delay: {delay}s;
            ">{emoji}</div>
            """
        st.markdown(fireworks_html, unsafe_allow_html=True)
    
    # Normal explosion - CHỈ HIỆN 1 LẦN KHI VỪA MỞ QUÀ
    elif st.session_state.show_explosion:
        st.markdown("""
        <div class="explosion-overlay">
            <div class="explosion-heart">💖</div>
            <div class="love-text">For You ❤️</div>
        </div>
        """, unsafe_allow_html=True)
        
        fireworks_html = ""
        for i in range(20):
            x = random.randint(-300, 300)
            y = random.randint(-300, 300)
            delay = random.uniform(0, 1)
            emoji = random.choice(['❤️', '💕', '💖', '💗', '💝', '💘'])
            fireworks_html += f"""
            <div class="firework" style="
                left: 50%; 
                top: 50%; 
                --tx: {x}px; 
                --ty: {y}px;
                animation-delay: {delay}s;
            ">{emoji}</div>
            """
        st.markdown(fireworks_html, unsafe_allow_html=True)
    
    # Background hearts
    st.markdown("""
    <div class="floating-hearts">
        <div class="floating-heart" style="top: 10%; left: 10%; animation-delay: 0s;">❤️</div>
        <div class="floating-heart" style="top: 20%; right: 15%; animation-delay: 2s;">💕</div>
        <div class="floating-heart" style="bottom: 20%; left: 20%; animation-delay: 4s;">💖</div>
        <div class="floating-heart" style="top: 60%; right: 10%; animation-delay: 1s;">💗</div>
        <div class="floating-heart" style="bottom: 40%; right: 30%; animation-delay: 3s;">💝</div>
    </div>
    """, unsafe_allow_html=True)
    
    hearts_container = st.empty()
    
    st.markdown("<h1 class='main-title'>Happy Valentine's Day! 💕</h1>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='romantic-text'>
        {st.session_state.love_message}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p class='love-message'>Yêu bé MinhThuy nhiều lắm 🥰</p>", unsafe_allow_html=True)
    
    # Buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("💌 Gửi lại", use_container_width=True):
            st.session_state.screen = 'gift'
            st.session_state.love_message = ""
            st.session_state.love_count = 0
            st.session_state.show_explosion = False
            st.session_state.show_fool = False
            st.rerun()
    
    with col3:
        if st.button(f"❤️ Thương ({st.session_state.love_count})", use_container_width=True):
            st.session_state.love_count += 1
            # TẮT EXPLOSION SAU LẦN ĐẦU
            st.session_state.show_explosion = False
            
            # Flying hearts
            hearts_html = ""
            for i in range(5):
                x = random.randint(-200, 200)
                y = random.randint(-300, -100)
                rotation = random.randint(-180, 180)
                emoji = random.choice(['❤️', '💕', '💖', '💗', '💝'])
                
                hearts_html += f"""
                <div class="flying-heart" style="
                    left: 50%; 
                    top: 70%; 
                    --fx: {x}px; 
                    --fy: {y}px;
                    --fr: {rotation}deg;
                ">{emoji}</div>
                """
            
            hearts_container.markdown(hearts_html, unsafe_allow_html=True)
            
            # ĐỔI TỪ 10 → 2 LẦN
            if st.session_state.love_count >= 2:
                st.session_state.show_fool = True
                st.session_state.love_count = 0
            
            st.rerun()
    
    st.markdown("""
    <p class='footer-text'>
        Chúc em một ngày Valentine thật hạnh phúc! 🌸❤️
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align: center; margin-top: 2rem; color: #f06292; font-family: "Dancing Script", cursive;'>
        <p>#MinhThuy #Valentine2025 💖</p>
    </div>
    """, unsafe_allow_html=True)

# ===== MAIN =====
def main():
    if st.session_state.screen == 'gift':
        show_gift()
    elif st.session_state.screen == 'message':
        show_message()

if __name__ == "__main__":
    main()
