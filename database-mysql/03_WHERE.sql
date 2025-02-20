# WHERE

-- 1) 비교연산자
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
	WHERE orderable_status='Y'; -- 해당 문자열이나 원소가 같은 컬럼을 추출

SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
	WHERE orderable_status <> 'Y'; -- 해당 문자열이나 원소가 다른 컬럼을 추출
    
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
	WHERE menu_price <= 10000; -- 해당 문자열이나 원소보다 작거나 같은 컬럼을 추출
    
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
	WHERE 10000 < menu_price <= 20000; -- 사잇값을 가진 컬럼 추출
    
-- 2) AND
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
	WHERE 10000 < menu_price 
    AND menu_price <= 20000; -- 조건 AND 조건을 모두 만족시키는 컬럼 추출

-- 3) OR
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
	WHERE menu_price > 30000 
    OR menu_price <= 20000; -- 조건 OR 조건 들중 하나라도 만족시키는 컬럼 추출

-- 4) BETWEEN
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
	WHERE menu_price BETWEEN 10000 AND 20000; -- 사잇값을 가진 컬럼 추출

SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
	WHERE menu_price NOT BETWEEN 10000 AND 20000; -- 사잇값을 가지지 않는 컬럼 추출

-- 5) LIKE
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
	WHERE menu_name LIKE '%김치%'; -- 해당 문자열을 포함한 컬럼 추출
    
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
	WHERE menu_name NOT LIKE '%김치%'; -- 해당 문자열을 포함하지 않은 컬럼 추출

-- 6) IN
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
	WHERE category_code=4
    OR category_code=5
    OR category_code=6; 
    
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
    WHERE category_code IN (4,5,6); -- IN ( 해당하는 원소) 를 가진 컬럼을 추출 (다수)
    
SELECT menu_name, menu_price, orderable_status
	FROM tbl_menu
    WHERE category_code NOT IN (4,5,6); -- IN ( 해당하는 원소) 를 가지지 않은 컬럼을 추출 (다수)

-- 7) IS NULL
SELECT category_code, category_name, ref_category_code
	FROM tbl_category
    WHERE ref_category_code IS NULL; -- 해당 원소가 NULL인 컬럼을 추출
    
SELECT category_code, category_name, ref_category_code
	FROM tbl_category
    WHERE ref_category_code IS NOT NULL; -- 해당 원소가 NULL이 아닌 컬럼을 추출
    