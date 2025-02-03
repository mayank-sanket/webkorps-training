CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- 

CREATE TABLE assets (
    id INT PRIMARY KEY REFERENCES employees(id) ON DELETE CASCADE,
    laptop_id VARCHAR(10) UNIQUE NOT NULL,
    charger_id VARCHAR(10) UNIQUE NOT NULL,
    keyboard_id VARCHAR(10) UNIQUE NOT NULL,
    mouse_id VARCHAR(10) UNIQUE NOT NULL
);

-- 

CREATE SEQUENCE laptop_seq START 1;
CREATE SEQUENCE charger_seq START 1;
CREATE SEQUENCE keyboard_seq START 1;
CREATE SEQUENCE mouse_seq START 1;

-- 

CREATE OR REPLACE FUNCTION insert_assets()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO assets (id, laptop_id, charger_id, keyboard_id, mouse_id)
    VALUES (
        NEW.id,
        'LP' || LPAD(nextval('laptop_seq')::TEXT, 5, '0'),
        'CG' || LPAD(nextval('charger_seq')::TEXT, 5, '0'),
        'KB' || LPAD(nextval('keyboard_seq')::TEXT, 5, '0'),
        'MS' || LPAD(nextval('mouse_seq')::TEXT, 5, '0')
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql

-- 
INSERT INTO employees (name, age, department, salary, email) VALUES ('vishal', 22, 'CS', 1200, 'vishal@gmail.com')

-- 
CREATE TRIGGER after_employee_insert
AFTER INSERT ON employees
FOR EACH ROW EXECUTE FUNCTION insert_assets();

-- 
select * from assets;
select * from employees;
-- 