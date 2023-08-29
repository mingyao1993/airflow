INSERT INTO table1 (
    column1,
    column2,
    column3
)
VALUES
    (1, 'value1', 'value2'),
    (2, 'value3', 'value4'),
    (3, 'value5', 'value6')
ON CONFLICT (column1) DO UPDATE
    SET
        column2 = EXCLUDED.column2,
        column3 = EXCLUDED.column3;
