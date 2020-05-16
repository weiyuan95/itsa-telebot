CREATE TABLE users (
  username VARCHAR(255) PRIMARY KEY,
  chat_id VARCHAR(255) NOT NULL
);

INSERT INTO users VALUES ('foo', 'bar');