import streamlit as st
import pandas as pd
import altair as alt
import os

st.set_page_config(page_title="MBTI 국가별 비율 Top 10", layout="wide")
st.title("🌍 MBTI 유형별 국가 Top 10 분석")

# 파일 경로 설정
default_path = "countriesMBTI_16types.csv"
df = None

# 1️⃣ 기본 파일이 같은 폴더에 있으면 자동으로 불러오기
if os.path.exists(default_path):
    st.success(f"기본 데이터 파일을 불러왔습니다: {default_path}")
    df = pd.read_csv(default_path)
else:
    # 2️⃣ 없으면 업로드 기능 사용
    uploaded_file = st.file_uploader("📂 CSV 파일 업로드", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)

if df is not None:
    # MBTI 컬럼들 자동 감지
    mbti_types = [
        "INTJ","INTP","ENTJ","ENTP",
        "INFJ","INFP","ENFJ","ENFP",
        "ISTJ","ISFJ","ESTJ","ESFJ",
        "ISTP","ISFP","ESTP","ESFP"
    ]
    country_col = "Country"
    mbti_cols = [c for c in df.columns if c in mbti_types]

    # 국가별 총합 및 비율 계산
    df["_total"] = df[mbti_cols].sum(_]()_]()
