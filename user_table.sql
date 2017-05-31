

CREATE TABLE users (
    ID SERIAL UNIQUE PRIMARY KEY,
    username character varying(255) NOT NULL UNIQUE,
    registration_time timestamp without time zone NOT NULL DEFAULT NOW(),
    reputation INT NOT NULL
);

INSERT INTO users (username, reputation) VALUES ('mokamiki', 12);
INSERT INTO users (username, reputation) VALUES ('misimokus', 25);
INSERT INTO users (username, reputation) VALUES ('susuasarkany', 40);
INSERT INTO users (username, reputation) VALUES ('hipsztermertbenceakarta', -22);
INSERT INTO users (username, reputation) VALUES ('vizipok88', -2);
INSERT INTO users (username, reputation) VALUES ('brucewayne', 0);
