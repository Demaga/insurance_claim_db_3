-- Generated by Oracle SQL Developer Data Modeler 19.4.0.350.1424
--   at:        2020-05-09 18:04:17 EEST
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g



CREATE TABLE collision_type (
    collision_type_name VARCHAR2(100) NOT NULL
);

ALTER TABLE collision_type ADD CONSTRAINT collision_type_pk PRIMARY KEY ( collision_type_name );

CREATE TABLE customer (
    age                  NUMBER(10),
    zip                  VARCHAR2(100),
    sex                  VARCHAR2(100),
    education_type_name  VARCHAR2(100) NOT NULL,
    policy_number        NUMBER(10) NOT NULL
);

ALTER TABLE customer ADD CONSTRAINT customer_pk PRIMARY KEY ( policy_number );

CREATE TABLE education (
    education_type_name VARCHAR2(100) NOT NULL
);

ALTER TABLE education ADD CONSTRAINT education_pk PRIMARY KEY ( education_type_name );

CREATE TABLE incident (
    capital_gains        NUMBER(10),
    capital_loss         NUMBER(10),
    policy_number        NUMBER(10) NOT NULL,
    incident_type_name   VARCHAR2(100) NOT NULL,
    collision_type_name  VARCHAR2(100) NOT NULL,
    incident_date        DATE NOT NULL
);

ALTER TABLE incident ADD CONSTRAINT incident_pk PRIMARY KEY ( policy_number,
                                                              incident_date );

CREATE TABLE incident_type (
    incident_type_name VARCHAR2(100) NOT NULL
);

ALTER TABLE incident_type ADD CONSTRAINT incident_type_pk PRIMARY KEY ( incident_type_name );

CREATE TABLE policy (
    policy_number  NUMBER(10) NOT NULL,
    bind_date      DATE,
    state_name     VARCHAR2(100) NOT NULL
);

ALTER TABLE policy ADD CONSTRAINT policy_pk PRIMARY KEY ( policy_number );

CREATE TABLE state (
    state_name VARCHAR2(100) NOT NULL
);

ALTER TABLE state ADD CONSTRAINT state_pk PRIMARY KEY ( state_name );

ALTER TABLE customer
    ADD CONSTRAINT customer_education_fk FOREIGN KEY ( education_type_name )
        REFERENCES education ( education_type_name );

ALTER TABLE customer
    ADD CONSTRAINT customer_policy_fk FOREIGN KEY ( policy_number )
        REFERENCES policy ( policy_number );

ALTER TABLE incident
    ADD CONSTRAINT incident_collision_type_fk FOREIGN KEY ( collision_type_name )
        REFERENCES collision_type ( collision_type_name );

ALTER TABLE incident
    ADD CONSTRAINT incident_incident_type_fk FOREIGN KEY ( incident_type_name )
        REFERENCES incident_type ( incident_type_name );

ALTER TABLE incident
    ADD CONSTRAINT incident_policy_fk FOREIGN KEY ( policy_number )
        REFERENCES policy ( policy_number );

ALTER TABLE policy
    ADD CONSTRAINT policy_state_fk FOREIGN KEY ( state_name )
        REFERENCES state ( state_name );



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             7
-- CREATE INDEX                             0
-- ALTER TABLE                             13
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
