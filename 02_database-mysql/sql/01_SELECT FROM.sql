# SELECT FROM

use menudb;

SELECT menu_name
	FROM tbl_menu; 
    
SELECT menu_code, menu_name, menu_price, category_code, orderable_status
	FROM tbl_menu;
    
SELECT *
	FROM tbl_menu;
    
SELECT 12 + 17; -- Oracle에서는 SELECT절은 FROM과 항상 같이 있어야함
SELECT 12 - 17;
SELECT 12 * 17;
SELECT 12 / 17;