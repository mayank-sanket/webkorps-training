CREATE TABLE parent_table (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE child_table (
    child_id SERIAL PRIMARY KEY,
    parent_id INT REFERENCES parent_table(id) ON DELETE CASCADE,
    description TEXT
);



INSERT INTO parent_table (name) VALUES ('Parent 1'), ('Parent 2');
INSERT INTO child_table (parent_id, description) VALUES 
(1, 'Child 1 of Parent 1'), (1, 'Child 2 of Parent 1'), (2, 'Child 1 of Parent 2');


SELECT * FROM parent_table;
SELECT * FROM child_table;


DELETE FROM parent_table WHERE id = 1;


-- Alternatives of CASCADE: (refer docs too)
    -- on delete restrict
    -- on delete set null
    -- on delete set default
    -- on delete no action
