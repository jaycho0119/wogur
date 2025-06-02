import streamlit as st

# 🌈 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 추천기 💼✨",
    page_icon="💡",
    layout="centered"
)

# 🎨 사용자 테마 설정
theme_color = st.color_picker("🎨 테마 색상을 선택하세요!", "#FF69B4")
st.markdown(f"<style>h1, h2, .stSelectbox label, .stSlider label {{ color: {theme_color}; }}</style>", unsafe_allow_html=True)

# 💫 상단 타이틀
st.markdown(f"""
    <div style='text-align: center;'>
        <h1>MBTI 기반 직업 추천 💼🔮</h1>
        <p style='font-size: 20px;'>당신의 성격 유형에 맞는 꿈의 직업을 찾아보세요! ✨</p>
    </div>
""", unsafe_allow_html=True)

# 🌟 배경 이모지
st.markdown("🎈🌟💫✨🎉🎊🎈" * 5)

# 🔤 MBTI 리스트
mbti_types = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
]

# 🧭 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["데이터 과학자 📊", "전략 컨설턴트 🧠", "AI 연구자 🤖", "UX 디자이너 🎨"],
    "INTP": ["이론 물리학자 ⚛️", "프로그래머 💻", "게임 디자이너 🎮", "발명가 🔬"],
    "ENTJ": ["CEO 🏢", "프로젝트 매니저 📈", "변호사 ⚖️", "사업가 📊"],
    "ENTP": ["스타트업 창업가 🚀", "마케팅 전문가 📣", "발명가 🔧", "유튜버 🎥"],
    "INFJ": ["상담사 🧘", "작가 ✍️", "교사 🍎", "사회운동가 ✊"],
    "INFP": ["예술가 🎨", "시인 📜", "사회 운동가 ✊", "기획자 📝"],
    "ENFJ": ["리더십 코치 🧑‍🏫", "홍보 담당자 🗣️", "심리학자 🧠", "사회복지사 ❤️"],
    "ENFP": ["유튜버 📹", "탐험가 🧭", "디자이너 ✏️", "에디터 🖋️"],
    "ISTJ": ["공무원 🏛️", "회계사 🧾", "엔지니어 🛠️", "데이터 분석가 📊"],
    "ISFJ": ["간호사 🏥", "도서관 사서 📚", "초등교사 🍎", "비서 ✉️"],
    "ESTJ": ["경영 관리자 📋", "군 장교 🎖️", "감독관 🛡️", "관리직 🏢"],
    "ESFJ": ["사회복지사 ❤️", "이벤트 플래너 🎊", "호텔 매니저 🏨", "고객 상담사 📞"],
    "ISTP": ["기계공 🛠️", "파일럿 ✈️", "경찰관 🚓", "기술자 🔧"],
    "ISFP": ["사진작가 📷", "플로리스트 🌸", "패션 디자이너 👗", "메이크업 아티스트 💄"],
    "ESTP": ["영업 전문가 💼", "스턴트맨 🏍️", "운동선수 🏋️", "프로게이머 🎮"],
    "ESFP": ["연예인 🎤", "무용가 💃", "MC 🎙️", "방송인 📺"]
}

# 🎯 사용자 입력
selected_mbti = st.selectbox("📌 당신의 MBTI 유형을 선택하세요!", mbti_types)

top3_only = st.checkbox("🔥 TOP 3 직업만 보기", value=True)

num_jobs = st.slider("🔢 추천 직업 개수 선택", min_value=1, max_value=10, value=3)

# 📋 직업 추천 결과
if selected_mbti:
    st.markdown("---")
    st.markdown(f"## 🧭 {selected_mbti} 유형 추천 직업")

    jobs = mbti_jobs.get(selected_mbti, [])
    if top3_only:
        display_jobs = jobs[:3]
    else:
        display_jobs = jobs[:num_jobs]

    for i, job in enumerate(display_jobs, 1):
        st.markdown(f"**{i}.** {job}")

    st.success("💖 당신의 성격에 딱 맞는 직업을 찾아보세요!")
    st.balloons()

# 🚀 바닥글
st.markdown(f"""
<hr>
<div style='text-align: center; color: gray;'>
    Made with ❤️ by 미래진로교육랩 | 2025
</div>
""", unsafe_allow_html=True)
