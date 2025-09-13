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
    df["_total"] = df[mbti_cols].sum(axis=1)
    df_pct = df.copy()
    for c in mbti_cols:
        df_pct[c] = df_pct[c] / df_pct["_total"]

    # 선택 박스: MBTI 유형
    selected_mbti = st.selectbox("🔎 MBTI 유형 선택", mbti_cols)

    # 선택한 MBTI 비율 Top 10 국가
    top10 = df_pct[[country_col, selected_mbti]].sort_values(
        by=selected_mbti, ascending=False
    ).head(10)

    # Altair 그래프 (붉은 계열)
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(selected_mbti, title="비율", axis=alt.Axis(format="%")),
            y=alt.Y(country_col, sort="-x"),
            tooltip=[country_col, selected_mbti],
            color=alt.Color(selected_mbti, scale=alt.Scale(scheme="reds")),
        )
        .properties(width=700, height=400, title=f"{selected_mbti} 비율 Top 10 국가")
    )

    st.altair_chart(chart, use_container_width=True)

    # 데이터 테이블 표시
    st.dataframe(top10.set_index(country_col).style.format({selected_mbti: "{:.2%}"}))

else:
    st.warning("⚠️ 기본 데이터 파일이 없으며, 업로드된 파일도 없습니다. CSV를 업로드해주세요.")
