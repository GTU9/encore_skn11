# GROUP BY

use menudb;

-- 단일 컬럼 GROUP BY + COUNT 함수
SELECT category_code, COUNT(*) -- 그룹에 따른 튜플 개수
	FROM tbl_menu
    GROUP BY category_code; 
    
-- 단일 컬럼 GROUP BY + SUM 함수
SELECT category_code, SUM(menu_price) -- 그룹에 따른 해당 속성 값의 총합
	FROM tbl_menu
    GROUP BY category_code;

-- 단일 컬럼 GROUP BY + AVG 함수
SELECT category_code, AVG(menu_price) -- 그룹에 따른 해당 속성의 평균
	FROM tbl_menu
    GROUP BY category_code;

-- 다중 컬럼 GROUP BY + count 함수
SELECT category_code, menu_price, COUNT(*)
	FROM tbl_menu
    GROUP BY category_code, menu_price -- GROUP BY x,y => x와 y 를 곱합 조합 그룹을 기준으로 묶음
    ORDER BY category_code, menu_price;
    
# HAVING

SELECT category_code, COUNT(*)
	FROM tbl_menu
    GROUP BY category_code
    HAVING category_code BETWEEN 5 AND 8; -- 기존의 GROUP BY에 조건절을 추가해서 조건 만족 그룹을 추출
    
# ROLLUP

-- 컬럼 한 개를 활용해 GROUP BY 후 ROLLUP -> 총계(합계)
SELECT category_code, SUM(menu_price)
	FROM tbl_menu
	GROUP BY category_code
    WITH ROLLUP;	-- 속성 값의 총계를 추가해줌
    
-- 컬럼 두 개를 활용해 GROUP BY 후 ROLLUP -> 중간 합계 + 총계
-- 먼저 나온 컬럼의 총합을 구하고, 이후에 나오는 컬럼의 총합까지 구하는 방식
SELECT category_code, menu_price, COUNT(menu_price)
	FROM tbl_menu
	GROUP BY category_code, menu_price
    WITH ROLLUP;