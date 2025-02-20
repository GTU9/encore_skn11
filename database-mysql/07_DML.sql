# DML

SELECT menu_code, menu_name, menu_price, category_code, orderable_status
	FROM tbl_menu;

# INSERT
-- INSERT INTO 테이블명 VALUES (컬럼순으로, 삽입할, 데이터, 나열, ...)

INSERT INTO tbl_menu VALUES (null,'슈팅스타곰탕',9500, 6,'Y'); -- 속성 값을 설정하지 않고 순서대로 데이터 삽입

-- INSERT INTO 테이블명(속성명, 속성명, 속성명)
-- VALUES (값, 값, 값)
INSERT INTO tbl_menu(menu_code,menu_name, menu_price, orderable_status, category_code) 
	VALUES(null,'그냥뜨거운냉면',15000,'Y',6); -- 속성 값을 정한 데이터 삽입
    
INSERT INTO tbl_menu(menu_code,menu_name, menu_price, category_code, orderable_status) 
	VALUES(null,'민트초코송편',5600,7,'Y'); -- 기존 속성과 순서가 달라도 매치되서 데이터 삽입

-- multi insert value
INSERT INTO tbl_menu
	VALUES
    (null, '양념치킨맛라떼', 6900, 7 ,'Y'),
    (null, '간장치킨맛라떼', 7500, 7 ,'Y'),
    (null, '훈제치킨맛라떼', 9500, 7 ,'Y'); -- 하나의 insert절로 여러 데이터 삽입
    
-- INSERT INTO tbl_menu
-- 	VALUES (1,'1번 음식',100, 10, 'Y'); -- 기본키 제약조건에 의해 중복된 데이터는 삽입되지 않는다.

INSERT INTO tbl_menu
	VALUES (100,'100번 음식',100, 10, 'Y'); 
INSERT INTO tbl_menu
	VALUES (null,'101번 음식',100, 10, 'Y'); -- AUTO INCREMENT 값은 가장 높은 값을 기준으로 1씩 늘어남
    
# UPDATE
-- UPDATE 테이블명
-- 	SET 컬럼명1 = 수정할 데이터,
-- 		컬럼명2 = 수정할 데이터,
--      ...
-- [ WHERE 수정 대상 데이터 조건 ];

UPDATE tbl_menu
	SET menu_name = '100번이었던 음식',
		menu_price = 19000
	WHERE menu_code=100; -- SAFE UPDATE MODE가 설정되어 있으면 WHERE절 없이 수정이 불가하다.
    
# DELETE
-- DELETE 
-- 	FROM 테이블명 [WHERE 삭제 조건];

DELETE
	FROM tbl_menu
    WHERE menu_code=101;
    
DELETE
	FROM tbl_menu
    ORDER BY menu_code DESC
    LIMIT 3; -- 역정렬 후 3번째 행 튜플까지 삭제
    
DELETE
	FROM tbl_menu;
    -- WHERE menu_code=26; -- SAFE UPDATE MODE가 설정되어 특정 튜플을 지정하지 않고는 삭제가 불가하다.
    
# REPLACE
REPLACE INTO tbl_menu VALUES(100,'100번 음식 REPLACE!!!',100,10,'Y'); -- 중복되는 값에 대한 경우엔 데이터를 덮어씌움
REPLACE tbl_menu VALUES(120,'없는 메뉴 REPLACE!!!',11111,8,'Y'); -- 중복되는 값이 없는 경우는 INSERT를 실행 ,INTO 생략가능