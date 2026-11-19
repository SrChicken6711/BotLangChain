/*
Datos insertados en la base de datos para pruebas

Tablas:
    - clientes
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT
        nombre TEXT NOT NULL
        apellido_1 TEXT NOT NULL
        correo TEXT UNIQUE NOT NULL

    - tecnicos
        id_tecnico INTEGER PRIMARY KEY AUTOINCREMENT
        nombre TEXT NOT NULL
        apellido_1 TEXT NOT NULL
        apellido_2 TEXT
        correo TEXT UNIQUE NOT NULL

    - tickets
        id_ticket INTEGER PRIMARY KEY AUTOINCREMENT
        id_cliente INTEGER NOT NULL
        id_tecnico INTEGER
        motivo TEXT NOT NULL
        estado DEFAULT 'Abierto'
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        fecha_cierre TIMESTAMP
        FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
        FOREIGN KEY (id_tecnico) REFERENCES tecnicos(id_tecnico)
*/

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido_1 TEXT NOT NULL,
    apellido_2 TEXT,
    correo TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS tecnicos(        
    id_tecnico INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido_1 TEXT NOT NULL,
    apellido_2 TEXT,
    correo TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS tickets(
    id_ticket INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    id_tecnico INTEGER,
    motivo TEXT NOT NULL,
    estado TEXT DEFAULT 'Abierto',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_cierre TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_tecnico) REFERENCES tecnicos(id_tecnico)
);

INSERT INTO clientes (nombre, apellido_1, apellido_2, correo) VALUES
('Carlos', 'Mendoza', 'Ruiz', 'carlos.mendoza@ejemplo.com'),
('Ana', 'Salazar', NULL, 'ana.salazar@ejemplo.com'),
('Luis', 'Torres', 'Vega', 'luis.torres@ejemplo.com'),
('Mariana', 'Castillo', 'Ortega', 'mariana.castillo@ejemplo.com'),
('Jorge', 'Ramos', NULL, 'jorge.ramos@ejemplo.com');

INSERT INTO tecnicos (nombre, apellido_1, apellido_2, correo) VALUES
('Roberto', 'Gómez', 'Silva', 'roberto.soporte@empresa.com'),
('Elena', 'Navarro', 'Cruz', 'elena.soporte@empresa.com'),
('Diego', 'Paredes', NULL, 'diego.soporte@empresa.com');

INSERT INTO tickets (id_cliente, id_tecnico, motivo, estado, fecha_cierre) VALUES
(1, NULL, 'No puedo iniciar sesión en el portal, marca error de credenciales aunque restablecí mi contraseña.', 'Abierto', NULL),
(2, 1, 'La factura del mes pasado aparece con un monto duplicado en el sistema.', 'En proceso', NULL),
(3, 2, 'Solicitud de cambio de correo electrónico vinculado a la cuenta principal.', 'Cerrado', '2026-11-15 14:30:00'),
(1, 1, 'La aplicación móvil se cierra inesperadamente al intentar descargar reportes en PDF.', 'En proceso', NULL),
(4, NULL, 'No recibo los códigos de verificación de dos pasos en mi bandeja de entrada.', 'Abierto', NULL),
(5, 3, 'Consulta sobre cómo dar de baja la suscripción anual antes de la renovación.', 'Cerrado', '2026-11-17 18:15:00');