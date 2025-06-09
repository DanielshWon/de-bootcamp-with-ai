#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Cell 1: 테스트용 데이터 준비
import pandas as pd

# 승환님이 직접 작성해보세요!
# 카페 매출 데이터 (날짜, 메뉴, 가격, 수량)
# 예: [["2025-01-01", "아메리카노", 4500, 2], ...]

data = [
    ["2025-05-01", "아메리카노", 4500, 2],
    ["2025-06-01", "카페라떼", 5000, 3],
    ["2025-06-02", "아이스크림", 5000, 1],
]
df = pd.DataFrame(data, columns=["날짜", "메뉴", "가격", "수량"])

print(df)


# In[5]:


# Cell 2: CSV 파일로 저장하기
# 승환님이 직접 작성해보세요!
# 힌트: df.to_csv("파일명.csv", ...)

df.to_csv("cafe_sales.csv", index=False)


# In[10]:


# Cell 3: 파일 읽기 함수 만들기
def read_cafe_sales(filename):
    # 승환님이 직접 작성해보세요!
    # CSV 파일을 읽어서 DataFrame으로 반환
    # 힌트: pd.read_csv() 사용
    df = pd.read_csv(filename)
    return df


# In[11]:


# Cell 4: 함수 테스트
result = read_cafe_sales("cafe_sales.csv")
print(result)


# In[12]:


# Cell 5: 없는 파일 읽기 시도해보기
# 일부러 에러를 확인해봐요!
try:
    result = read_cafe_sales("없는파일.csv")
    print("성공!")
except FileNotFoundError:
    print("파일이 없어요!")


# In[17]:


# Cell 6: pytest로 예외 상황 테스트
import pytest


def test_file_not_found():
    # 승환님이 직접 작성해보세요!
    # 힌트: pytest.raises() 사용
    # 없는 파일을 읽으려 할 때 FileNotFoundError가 나오는지 테스트
    assert read_cafe_sales("cafe_sales.csv")


# In[18]:


def test_file_not_found():
    # 이렇게 써요!
    with pytest.raises(FileNotFoundError):
        read_cafe_sales("없는파일.csv")


# In[19]:


# Cell 7: 테스트 실행
test_file_not_found()
print("테스트 완료!")


# In[24]:


# Cell 8: 정상 케이스 테스트
def test_normal_file_reading():
    # 승환님이 직접 작성해보세요!
    # 정상적인 파일을 읽었을 때 DataFrame이 나오는지 테스트
    # 힌트: assert isinstance(결과, pd.DataFrame)
    assert isinstance(df, pd.DataFrame)


test_normal_file_reading()


# In[28]:


## 정답


def test_normal_file_reading():
    # 1단계: 함수 호출해서 결과 받기
    result = read_cafe_sales("cafe_sales.csv")

    # 2단계: 그 결과가 DataFrame인지 확인
    assert isinstance(result, pd.DataFrame)
    print("정상 읽기 테스트 성공!")


test_normal_file_reading()

# 브랜치 테스트 - add-new-tests에서 추가한 코드
def test_branch_experiment():
    print("이 코드는 add-new-tests 브랜치에서만 보여요!")
    assert True