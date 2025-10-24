CREATE TABLE beneficiary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    contact TEXT
);

CREATE TABLE program (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT
);

CREATE TABLE enrollment (
    beneficiary_id INTEGER,
    program_id INTEGER,
    FOREIGN KEY(beneficiary_id) REFERENCES beneficiary(id),
    FOREIGN KEY(program_id) REFERENCES program(id)
);
