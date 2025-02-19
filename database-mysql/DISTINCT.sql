# DISTINCT

SELECT DISTINCT category_code
	FROM tbl_menu
    ORDER BY category_code; -- 중복값을 가진 컬럼을 제거한다
    
SELECT DISTINCT ref_category_code
	FROM tbl_category;
    
SELECT DISTINCT category_code, orderable_status
	FROM tbl_menu
    ORDER BY category_code, orderable_status; -- 1차적으로 정렬 후 2차 정렬 그 후 중복값 제거