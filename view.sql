CREATE OR REPLACE VIEW customer_education_incident AS
SELECT 
    policy_number,
    customer.education_type_name,
    customer.sex,
    incident.capital_loss,
    incident.incident_date,
    policy.bind_date
FROM
    customer
LEFT JOIN incident
USING (policy_number)
JOIN policy
USING (policy_number);
