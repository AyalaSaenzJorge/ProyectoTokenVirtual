DROP TABLE IF EXISTS tokens;

CREATE TABLE tokens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    token_value INT,
    created_since BIGINT,
    times_used SMALLINT
)  ENGINE=INNODB;



