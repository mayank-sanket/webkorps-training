-- Create customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create products table with explicit product IDs
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

-- Create orders table (Many-to-Many relation between customers and products)
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id) ON DELETE CASCADE,
    product_id INT REFERENCES products(product_id) ON DELETE CASCADE,
    quantity INT CHECK (quantity > 0),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample customers
INSERT INTO customers (name, email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Charlie Brown', 'charlie@example.com');

-- Insert sample products with specific IDs
INSERT INTO products (product_id, name, price) VALUES
(101, 'Laptop', 1200.00),
(102, 'Smartphone', 800.00),
(103, 'Headphones', 150.00);

-- Insert sample orders referencing the specific product IDs
INSERT INTO orders (customer_id, product_id, quantity) VALUES
(1, 101, 1),  -- Alice buys 1 Laptop
(2, 102, 2),  -- Bob buys 2 Smartphones
(3, 103, 1),  -- Charlie buys 1 Headphones
(1, 103, 3);  -- Alice buys 3 Headphones

-- Verify the data
SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM orders;


select p.product_id, p.name as product_name, count(distinct o.customer_id) as customer_count
from orders o
join products p on o.product_id = p.product_id
group by (p.product_id);


