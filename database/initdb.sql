-- Postgres
CREATE TABLE IF NOT EXISTS brt_data (
    id                      SERIAL PRIMARY KEY,
    codigo                  VARCHAR(30),
    placa                   VARCHAR(10),
    linha                   VARCHAR(80),
    latitude                FLOAT,
    longitude               FLOAT,
    datahora                TIMESTAMP,
    velocidade              FLOAT,
    id_migracao_trajeto     VARCHAR(50),
    sentido                 VARCHAR(10),
    trajeto                 VARCHAR(80),
    hodometro               FLOAT,
    direcao                 VARCHAR(10),
    created_at              TIMESTAMP DEFAULT current_timestamp
);