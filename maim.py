import streamlit as st
st.title('나의 첫 웹앱')
st.write('이걸 내가 만들었다고?')
import streamlit as st
import random

# MBTI별 연애 추천 문구 💘
recommendations = {
    "INTJ": "✨ 전략적이고 진지한 당신! 계획적인 데이트와 깊은 대화를 즐기는 파트너가 잘 맞아요 🧠❤️",
    "INTP": "🌀 자유로운 영혼! 창의적인 데이트(보드게임, 전시회)에서 두뇌 자극 대화가 최고 🖼️🎲",
    "ENTJ": "🔥 리더십 강한 당신! 주도적으로 여행✈️이나 액티비티를 기획하면 매력 200%",
    "ENTP": "🤣 유머감각 폭발! 깜짝 이벤트와 장난꾸러기 같은 데이트가 찰떡 🎭🎉",
    "INFJ": "💫 영혼의 교감! 조용한 카페에서 진심 어린 대화와 깊은 눈맞춤 ☕💞",
    "INFP": "🌸 순수하고 감성적! 손편지💌, 별 보며 산책🌌 같은 로맨틱 무드가 어울려요",
    "ENFJ": "🤝 배려심 넘치는 리더! 파트너를 위한 이벤트 서프라이즈🎁가 찰떡",
    "ENFP": "🌈 모험심 가득! 즉흥 여행🚗, 페스티벌🎶에서 에너지가 폭발",
    "ISTJ": "📅 성실한 책임감! 안정적인 루틴 데이트(맛집 탐방🍜, 주말 산책🚶‍♂️)이 잘 맞아요",
    "ISFJ": "🛡️ 따뜻한 수호자! 세심한 배려가 돋보이는 핸드메이드 선물🎀",
    "ESTJ": "🏆 추진력 만점! 팀플 데이트(쿠킹 클래스🍳, 스포츠 경기⚽)에 강해요",
    "ESFJ": "🎀 사랑꾼! 다 같이 어울리는 파티🎉, 친구와 함께하는 더블데이트도 굿",
    "ISTP": "🛠️ 현실주의 모험가! 드라이브🚗, 액티비티 스포츠(클라이밍 🧗‍♂️)가 어울려요",
    "ISFP": "🎨 감성 아티스트! 전시회🖌️, 감성 카페☕, 소소한 피크닉🍱",
    "ESTP": "⚡ 에너지 폭발! 클럽🎶, 놀이공원🎢, 즉흥 여행✈️에서 매력 발산",
    "ESFP": "🌟 파티의 중심! 노래방🎤, 댄스파티💃, 불꽃놀이🎆 데이트가 찰떡"
}

# 페이지 설정 🎨
st.set_page_config(page_title="MBTI 연애 추천기", page_icon="💘", layout="centered")

st.title("💘 MBTI 유형별 연애 추천기 💘")
st.markdown("""
### 당신의 MBTI 유형을 선택하면, 찰떡궁합 연애법을 추천해드려요 ✨
이모지 듬뿍 넣어서 귀엽고 재밌게~ 🥰
""")

# MBTI 선택 🎯
mbti_types = list(recommendations.keys())
selected = st.selectbox("당신의 MBTI는 무엇인가요?", ["선택하기"] + mbti_types)

# 버튼 클릭 시 추천 🥳
if selected != "선택하기":
    if st.button("💘 나의 연애 스타일 확인하기 💘"):
        st.success(recommendations[selected])

        # 재미있는 효과 랜덤 🎉
        effects = [st.balloons, st.snow, st.toast]
        effect = random.choice(effects)
        
        if effect == st.toast:
            effect("✨ 사랑은 바로 지금부터 시작! ✨")
        else:
            effect()
