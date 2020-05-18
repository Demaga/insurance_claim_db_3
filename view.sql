CREATE OR REPLACE VIEW customer_education_incident AS
SELECT 
    policy_number,
    customer.education_type_name,
    incident.capital_loss,
    policy.bind_date
FROM
    customer
LEFT JOIN incident
USING (policy_number)
JOIN policy
USING (policy_number);