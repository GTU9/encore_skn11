# ORDER BY

SELECT menu_code, menu_name, menu_price
	FROM tbl_menu
ORDER BY menu_name ASC; -- dfault 오름차순 정렬, 생략 가능

SELECT menu_code, menu_name, menu_price
	FROM tbl_menu
ORDER BY menu_name DESC; -- 내림차순 정렬

SELECT menu_code, menu_name, menu_price
	FROM tbl_menu
ORDER BY menu_price, menu_name; -- 1차 정렬후 2차정렬

SELECT menu_code, menu_name, menu_price, menu_code * menu_price
	FROM tbl_menu
ORDER BY menu_code * menu_price; -- 수식 결과 정렬도 가능

SELECT menu_code, menu_name, menu_price, menu_code * menu_price AS '연산결과'
	FROM tbl_menu
ORDER BY '연산결과'; -- 별칭 기준 정렬도 가능

SELECT category_code, category_name, ref_category_code
	FROM tbl_category
ORDER BY ref_category_code IS NULL; -- IS NULL 입력 오름차순 정렬시 NULL이 맨 끝으로 정렬

SELECT category_code, category_name, ref_category_code
	FROM tbl_category
ORDER BY ref_category_code IS NULL DESC, ref_category_code DESC; -- NULL 맨처음으로 정렬하면서도 역순정렬