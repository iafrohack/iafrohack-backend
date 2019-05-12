CREATE TABLE post_categories (
  id SERIAL PRIMARY KEY,
  name VARCHAR (20),
  created_at timestamp default null,
  last_updated_at timestamp DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO post_categories (id, name, created_at)
values (1, 'Software Engineering', NOW())
