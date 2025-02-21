CREATE DATABASE bookdb;
GRANT ALL PRIVILEGES ON bookdb.* TO ohgiraffers@'%';

USE bookdb;

CREATE TABLE naver_book(
	book_code INT AUTO_INCREMENT PRIMARY KEY,
	book_title VARCHAR(300),
    book_image VARCHAR(300),
    author VARCHAR(100),
    publisher VARCHAR(100),
    isbn VARCHAR(100),
    book_description VARCHAR(3000),
    pub_date DATETIME
	) ENGINE=innodb;
    
SELECT * FROM naver_book;