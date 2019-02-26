SELECT 
    *
FROM 
    fighters
WHERE
    name ilike ANY('{A%,B%,C%}')
ORDER BY
    name asc
