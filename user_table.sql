

CREATE TABLE users (
    ID SERIAL UNIQUE PRIMARY KEY,
    username character varying(255) NOT NULL UNIQUE,
    registration_time timestamp without time zone NOT NULL DEFAULT NOW()
);

INSERT INTO users (username) VALUES ('mokamiki' );
INSERT INTO users (username) VALUES ('misimokus');
INSERT INTO users (username) VALUES ('susuasarkany');

