-- Crear tabla
CREATE TABLE Clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    ciudad VARCHAR(100)
);

-- Insertar 500 registros con repetidos y nulos
INSERT INTO Clientes (nombre, ciudad)
SELECT 
    CASE 
        WHEN random() < 0.1 THEN NULL
        ELSE nombres[(floor(random()*10)+1)::int]
    END AS nombre,
    
    CASE 
        WHEN random() < 0.15 THEN NULL
        ELSE ciudades[(floor(random()*8)+1)::int]
    END AS ciudad

FROM generate_series(1,500),
LATERAL (
    SELECT 
        ARRAY['Ana','Luis','Carlos','Maria','Juan','Sofia','Pedro','Laura','Miguel','Elena'] AS nombres,
        ARRAY['CDMX','Guadalajara','Monterrey','Puebla','Tijuana','Mérida','León','Querétaro'] AS ciudades
) datos;
SELECT * FROM Clientes