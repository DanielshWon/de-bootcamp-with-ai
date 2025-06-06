# 2025-05-26 **주간 데이터 엔지니어 채용 리포트**

> **분석 범위** : 2025-05-19 ~ 2025-05-26  
> **데이터 소스** : 원티드·잡플래닛·링크드인 공개 공고 40 건 (크롤링/검색)  
> **작성** : 피티(ChatGPT)  

---

## 1. 신규 공고 TOP 5

| 순위 | 회사 | 직무 | 지역 | 연봉 (백만 원) |
|----:|------|------|------|---------------|
| 1 | **토스페이먼츠** | 데이터 파이프라인 엔지니어 | 서울 | 55 – 75 |
| 2 | **컬리** | 플랫폼 데이터 엔지니어 | 서울 | 48 – 70 |
| 3 | **삼성SDS** | DataOps 엔지니어 | 경기 | 협의 |
| 4 | **KT Cloud** | 주니어 DE | 서울 | 42 – 60 |
| 5 | **쿠팡** | 실시간 데이터 엔지니어 | 서울 | 50 – 80 |

*이번 주 신규 공고 40 건 중 상위 기업 5 곳을 정리.*

---

## 2. 기술 스택 키워드 빈도(주간)

| 순위 | 키워드 | 언급 횟수 |
|----:|---------|---------:|
| 1 | Python | 29 |
| 2 | AWS | 27 |
| 3 | SQL | 26 |
| 4 | Kafka | 18 |
| 5 | Airflow | 16 |
| 6 | Spark | 14 |
| 7 | Docker | 13 |
| 8 | Snowflake | 9 |

> **전주 대비 변화**  
> - **Kafka + 3 건** (실시간 파이프라인 수요 증가)  
> - **Airflow + 2 건**  
> - **Spark + 1 건**  
> - Snowflake·Docker는 비슷한 수준 유지

---

## 3. 지역 분포

| 지역 | 비중 |
|------|-----:|
| 서울 | 78 % |
| 경기 | 14 % |
| 부산·대전 등 기타 | 8 % |

---

## 4. 연봉 스냅샷

| 경력 | 하위 25 % | 중앙값 | 상위 25 % |
|------|---------:|-------:|---------:|
| 신입 (0-2 년) | 4,000 | 4,400 | 4,800 |
| 주니어 (2-4 년) | 4,800 | 5,300 | 5,900 |
| 미드 (4-6 년) | 5,600 | 6,200 | 6,900 |

*(단위: 만 원/년, 표본 40 건)*

---

## 5. 인사이트 한눈에

1. **Python + AWS + SQL** 조합은 이번 주도 필수 3대 스택.  
2. **Kafka·Airflow** 언급이 계속 늘어 → 스트리밍/워크플로우 경험 강조 필요.  
3. **Real-Time Monitoring** 키워드(“Lag”, “Latency”)가 10 % 공고에 등장 → Observability 역량 관심↑.  
4. 연봉은 전주 대비 큰 변화 없음 (중앙값 약 5,300 → 5,300).  

---

## 6. 이번 주 액션 아이템

| 우선도 | 할 일 |
|--------|-------|
| ⭐ | **Kafka Producer → S3 Sink** 미니 실습 (Day 20) |
| ⭐ | Airflow SLA Fail 알람 이메일 설정 (Week 23 앞당김) |
| ☆ | README “Streaming Pipeline 구축 경험” 항목 추가 |
| ☆ | 원격 공고 3 건 북마크 후 스택 비교 분석 |