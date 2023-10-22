CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 39e24cbb8619

INSERT INTO alembic_version (version_num) VALUES ('39e24cbb8619');

-- Running upgrade 39e24cbb8619 -> baa1ad138f14

UPDATE alembic_version SET version_num='baa1ad138f14' WHERE alembic_version.version_num = '39e24cbb8619';

