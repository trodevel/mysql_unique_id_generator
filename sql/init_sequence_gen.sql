INSERT INTO sequence_gen (id)
SELECT 0
WHERE NOT EXISTS (SELECT * FROM sequence_gen);
