import streamlit as st

# 🎨 페이지 설정
st.set_page_config(
    page_title="MBTI 직업 추천기 💼✨",
    page_icon="💡",
    layout="centered"
)

# 💫 상단 타이틀
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #FF69B4;'>MBTI 기반 직업 추천 💼🔮</h1>
        <p style='font-size: 20px;'>당신의 성격 유형에 맞는 꿈의 직업을 찾아보세요! ✨</p>
    </div>
""", unsafe_allow_html=True)

# 🎉 이모지 배경 효과 (가짜로 반복 이모지 넣기)
st.markdown("🌟✨💫🌈🎨🎉🎊🪄🦄🌺" * 5)

# 🧠 MBTI 목록
mbti_types = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
]

# 💡 직업 추천 딕셔너리
mbti_jobs = {
    "INTJ": ["데이터 과학자 📊", "전략 컨설턴트 🧠", "AI 연구자 🤖"],
    "INTP": ["이론 물리학자 ⚛️", "프로그래머 💻", "게임 디자이너 🎮"],
    "ENTJ": ["CEO 🏢", "프로젝트 매니저 📈", "변호사 ⚖️"],
    "ENTP": ["스타트업 창업가 🚀", "마케팅 전문가 📣", "발명가 🔧"],
    "INFJ": ["상담사 🧘", "작가 ✍️", "교사 🍎"],
    "INFP": ["예술가 🎨", "시인 📜", "사회 운동가 ✊"],
    "ENFJ": ["리더십 코치 🧑‍🏫", "홍보 담당자 🗣️", "심리학자 🧠"],
    "ENFP": ["유튜버 📹", "탐험가 🧭", "디자이너 ✏️"],
    "ISTJ": ["공무원 🏛️", "회계사 🧾", "엔지니어 🛠️"],
    "ISFJ": ["간호사 🏥", "도서관 사서 📚", "초등교사 🍎"],
    "ESTJ": ["경영 관리자 📋", "군 장교 🎖️", "감독관 🛡️"],
    "ESFJ": ["사회복지사 ❤️", "이벤트 플래너 🎊", "호텔 매니저 🏨"],
    "ISTP": ["기계공 🛠️", "파일럿 ✈️", "경찰관 🚓"],
    "ISFP": ["사진작가 📷", "플로리스트 🌸", "패션 디자이너 👗"],
    "ESTP": ["영업 전문가 💼", "스턴트맨 🏍️", "운동선수 🏋️"],
    "ESFP": ["연예인 🎤", "무용가 💃", "MC 🎙️"]
}

# 🧩 사용자 MBTI 선택
selected_mbti = st.selectbox("📌 당신의 MBTI 유형을 선택하세요!", mbti_types)

# 🎁 추천 결과 출력
if selected_mbti:
    st.markdown("---")
    st.markdown(f"## 🧭 {selected_mbti} 유형에게 추천하는 직업들")
    
    jobs = mbti_jobs.get(selected_mbti, [])
    for job in jobs:
        st.markdown(f"- {job}")

    st.markdown("💖 당신의 성격에 꼭 맞는 직업을 찾아보세요! 💫")
    st.balloons()

# ⛅ 바닥글
st.markdown("""
<hr>
<div style='text-align: center; color: gray;'>
    Made with ❤️ by 미래진로교육랩 | 2025
</div>
""", unsafe_allow_html=True)
