SET autocommit = OFF;

START TRANSACTION;

UPDATE sequence_gen SET id=LAST_INSERT_ID(id+1);
SELECT LAST_INSERT_ID();

COMMIT;
