-- Day 27: 서브쿼리 기초
-- 학습 목표: "쿼리 안에 쿼리" 개념 완전 이해

/*
=== 서브쿼리(Subquery)란? ===

1. 정의: 다른 SQL 쿼리 안에 포함된 SELECT 쿼리
2. 특징: 
   - 반드시 괄호 () 안에 작성
   - 안쪽 쿼리(서브쿼리)가 먼저 실행
   - 그 결과를 바깥쪽 쿼리(메인쿼리)가 사용

3. 실생활 비유:
   "우리 반에서 평균 키보다 큰 학생들을 찾아줘"
   → 1단계: 우리 반 평균 키 계산 (서브쿼리)
   → 2단계: 평균보다 큰 학생 찾기 (메인쿼리)

4. 언제 사용?
   - 동적인 값으로 비교할 때 (평균, 최댓값 등)
   - 미리 계산된 값이 필요할 때
   - 복잡한 조건을 만들 때
*/

-- 예제 1: 평균 가격보다 비싼 메뉴 찾기
SELECT name, price 
FROM menus 
WHERE price > (SELECT AVG(price) FROM menus);

-- 동작 과정:
-- 1단계: (SELECT AVG(price) FROM menus) → 평균 가격 계산
-- 2단계: WHERE price > 평균가격 → 조건 필터링



-- 실습: 가장 비싼 메뉴와 같은 가격인 메뉴 찾기
-- 힌트: MAX() 함수 사용

SELECT name, price
FROM menus
WHERE price = (SELECT MAX(price) FROM menus);

-- 문제 2: 가장 싼 메뉴보다 비싼 모든 메뉴 찾기  
-- 힌트: MIN() 함수 사용
SELECT name, price FROM menus WHERE price > (SELECT MIN(price) FROM menus);