PRAGMA foreign_keys = ON;
CREATE TABLE profiles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    PHONE TEXT NOT NULL,
    password TEXT NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    age INTEGER CHECK (age > 0),
    profile_id INTEGER UNIQUE,
    FOREIGN KEY (profile_id) REFERENCES profiles (id)
);
CREATE TABLE roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT  UNIQUE NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE users_roles (
    user_id INTEGER,
    role_id INTEGER,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (role_id) REFERENCES roles (id)
);
CREATE TABLE permissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE roles_permissions (
    role_id INTEGER,
    permission_id INTEGER,
    PRIMARY KEY (role_id, permission_id),
    FOREIGN KEY (role_id) REFERENCES roles (id),
    FOREIGN KEY (permission_id) REFERENCES permissions (id)
);
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    price REAL CHECK (price > 0),
    description TEXT,
    pages_num INTEGER,
    binding_format TEXT,
    age_restriction INTEGER,
    quantity_available INTEGER,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE books_genres (
    book_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (book_id, genre_id),
    FOREIGN KEY (book_id) REFERENCES books (id),
    FOREIGN KEY (genre_id) REFERENCES genres (id)
);
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT UNIQUE NOT NULL,
    birth_date NUMERIC,
    death_date NUMERIC,
    info TEXT,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE books_authors (
    book_id INTEGER,
    author_id INTEGER,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books (id),
    FOREIGN KEY (author_id) REFERENCES authors (id)
);
CREATE TABLE baskets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    basket_status TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
CREATE TABLE books_baskets (
    book_id INTEGER,
    basket_id INTEGER,
    PRIMARY KEY (book_id, basket_id),
    FOREIGN KEY (book_id) REFERENCES books (id),
    FOREIGN KEY (basket_id) REFERENCES baskets (id)
);
CREATE TABLE bank_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    cvc INTEGER,
    expiry_month_year TEXT,
    user_id INTEGER,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    basket_id INTEGER,
    bank_card_id INTEGER,
    final_amount REAL,
    delivery_address TEXT,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (basket_id) REFERENCES baskets (id),
    FOREIGN KEY (bank_card_id) REFERENCES bank_cards (id)
);
CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);
CREATE TABLE cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries (id)
);
CREATE TABLE addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_id INTEGER,
    city_id INTEGER,
    street TEXT,
    house_num TEXT,
    user_id INTEGER,
    created_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    update_at NUMERIC DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (country_id) REFERENCES countries (id),
    FOREIGN KEY (city_id) REFERENCES cities (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
