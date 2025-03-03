# LIMIT

use menudb;

SELECT menu_code, menu_name, menu_price
	FROM tbl_menu
	ORDER BY menu_price DESC;
    
SELECT menu_code, menu_name, menu_price
	FROM tbl_menu
	ORDER BY menu_price DESC
    LIMIT 7; -- LIMIT x => 첫번쨰 행부터 x개의 튜플을 추출
    
-- offset= 2, row count= 5
SELECT menu_code, menu_name, menu_price
	FROM tbl_menu
	ORDER BY menu_price DESC
    LIMIT 2, 5; -- LMIT x, y  => x+1 번째 행부터 y개의 튜플을 추출