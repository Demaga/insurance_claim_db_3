DECLARE
    rows NUMBER(5) := 3;
    TYPE age IS VARRAY(3) OF NUMBER(10, 2);
    TYPE zip IS VARRAY(3) OF NUMBER(10, 2);
    TYPE sex IS VARRAY(3) OF VARCHAR2(50 CHAR);
    TYPE education_type_name IS VARRAY(3) OF VARCHAR2(50 CHAR);
    TYPE policy_number IS VARRAY(3) OF NUMBER(10, 2);
    age_arr age := age(54, 24, 95);
    zip_arr zip := zip(41254, 124424, 12495);
    sex_arr sex := sex('M', 'F', 'F');
    education_type_name_arr education_type_name := education_type_name('PhD', 'MD', 'High School');
    policy_number_arr policy_number := policy_number(1011, 1012, 1013);
BEGIN

    FOR i in 1..rows LOOP
        INSERT INTO policy
        VALUES(policy_number_arr(i), NULL, 'OH');
        
        INSERT INTO customer
        VALUES (age_arr(i), zip_arr(i), sex_arr(i), education_type_name_arr(i), policy_number_arr(i));

        INSERT INTO incident
        VALUES (NULL, NULL, policy_number_arr(i), 'Single Vehicle Collision', '?', '15.01.2020');
    END LOOP;
END;
