SELECT 
    customer_id,
    customer_name,
    'Verified' AS account_status
FROM {{ ref('my_first_dbt_model') }}