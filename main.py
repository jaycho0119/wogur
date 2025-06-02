import streamlit as st

# 🎨 페이지 설정
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

# 🎉 배경 이모지 효과
st.markdown("🎈🌟💫✨🎉🎊🎈" * 5)

# 🧠 MBTI 유형
mbti_types = [
    'INTJ', 'INTP', 'ENTJ', 'ENTP',
    'INFJ', 'INFP', 'ENFJ', 'ENFP',
    'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ',
    'ISTP', 'ISFP', 'ESTP', 'ESFP'
]

# 📚 직업 데이터 구조: {직업: (설명, 평균연봉)}
job_info = {
    "데이터 과학자 📊": ("데이터를 분석하여 인사이트를 도출하고 의사결정에 도움을 주는 직업", 6000),
    "전략 컨설턴트 🧠": ("기업의 전략을 수립하고 개선 방향을 제시하는 전문가", 8000),
    "AI 연구자 🤖": ("인공지능 알고리즘과 모델을 개발 및 연구하는 직업", 7500),
    "UX 디자이너 🎨": ("사용자의 경험을 최우선으로 생각하는 디지털 제품 디자이너", 5500),
    "이론 물리학자 ⚛️": ("우주의 원리를 수학과 논리를 통해 탐구하는 과학자", 5000),
    "프로그래머 💻": ("코드를 작성하여 앱, 웹, 소프트웨어를 만드는 직업", 5500),
    "게임 디자이너 🎮": ("게임의 세계관과 콘텐츠를 설계하고 개발하는 직업", 5200),
    "CEO 🏢": ("기업을 총괄하며 전략을 수립하고 조직을 이끄는 최고 책임자", 15000),
    "상담사 🧘": ("개인의 고민이나 심리적 문제를 전문적으로 상담해주는 직업", 4000),
    "작가 ✍️": ("소설, 에세이, 기사 등 글을 창작하거나 집필하는 직업", 3500),
    "유튜버 📹": ("영상 콘텐츠를 제작하여 유튜브 플랫폼에 게시하는 크리에이터", 3000),
    "탐험가 🧭": ("미지의 장소를 조사하고 기록하는 모험가적 성향의 직업", 2000),
    "공무원 🏛️": ("국가기관에서 국민을 위해 공공 업무를 수행하는 직업", 4500),
    "간호사 🏥": ("환자의 건강을 돌보고 치료를 보조하는 의료 전문직", 4200),
    "기계공 🛠️": ("기계의 제작, 유지, 보수를 담당하는 기술자", 4300),
    "사진작가 📷": ("사진을 예술적으로 촬영하고 편집하는 직업", 3700),
    "연예인 🎤": ("노래, 연기, 예능 등에서 대중 앞에 서는 직업", 7000),
}

# 🔗 MBTI - 직업 추천 매핑
mbti_jobs = {
    "INTJ": ["데이터 과학자 📊", "전략 컨설턴트 🧠", "AI 연구자 🤖", "UX 디자이너 🎨"],
    "INTP": ["이론 물리학자 ⚛️", "프로그래머 💻", "게임 디자이너 🎮"],
    "ENTJ": ["CEO 🏢", "전략 컨설턴트 🧠", "프로그래머 💻"],
    "ENTP": ["유튜버 📹", "게임 디자이너 🎮", "탐험가 🧭"],
    "INFJ": ["상담사 🧘", "작가 ✍️", "UX 디자이너 🎨"],
    "INFP": ["작가 ✍️", "사진작가 📷", "탐험가 🧭"],
    "ENFJ": ["상담사 🧘", "작가 ✍️", "프로그래머 💻"],
    "ENFP": ["유튜버 📹", "작가 ✍️", "게임 디자이너 🎮"],
    "ISTJ": ["공무원 🏛️", "프로그래머 💻", "기계공 🛠️"],
    "ISFJ": ["간호사 🏥", "공무원 🏛️", "상담사 🧘"],
    "ESTJ": ["CEO 🏢", "공무원 🏛️", "프로그래머 💻"],
    "ESFJ": ["간호사 🏥", "작가 ✍️", "UX 디자이너 🎨"],
    "ISTP": ["기계공 🛠️", "프로그래머 💻", "사진작가 📷"],
    "ISFP": ["사진작가 📷", "작가 ✍️", "탐험가 🧭"],
    "ESTP": ["유튜버 📹", "기계공 🛠️", "프로그래머 💻"],
    "ESFP": ["연예인 🎤", "사진작가 📷", "유튜버 📹"]
}

# 🎛 사용자 입력
selected_mbti = st.selectbox("📌 당신의 MBTI 유형을 선택하세요!", mbti_types)
top3_only = st.checkbox("🔥 TOP 3 직업만 보기", value=True)
num_jobs = st.slider("🔢 추천 직업 개수 선택", min_value=1, max_value=10, value=3)

# 📊 추천 직업 출력
if selected_mbti:
    st.markdown("---")
    st.markdown(f"## 🧭 {selected_mbti} 유형 추천 직업")

    jobs = mbti_jobs.get(selected_mbti, [])
    display_jobs = jobs[:3] if top3_only else jobs[:num_jobs]

    for i, job in enumerate(display_jobs, 1):
        description, salary = job_info.get(job, ("정보 없음", 0))
        st.markdown(f"""
        <div style="border: 2px solid {theme_color}; padding: 10px; border-radius: 10px; margin-bottom: 10px;">
            <h4 style="color: {theme_color};">🔹 {i}. {job}</h4>
            <p>📝 <b>설명:</b> {description}</p>
            <p>💰 <b>평균 연봉:</b> {salary:,}만원</p>
        </div>
        """, unsafe_allow_html=True)

    st.success("💖 당신에게 어울리는 진로가 눈에 보이시나요?")
    st.balloons()

# 🪧 바닥글
st.markdown(f"""
<hr>
<div style='text-align: center; color: gray;'>
    Made with ❤️ by 미래진로교육랩 | 2025
</div>
""", unsafe_allow_html=True)
