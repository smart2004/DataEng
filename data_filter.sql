-- Использование WHERE для фильтрации сотрудников с зарплатой выше 70000
SELECT name, salary
FROM employees
WHERE salary > 70000;

-- Использование HAVING для фильтрации групп
SELECT d.department_name, AVG(e.salary) AS avg_salary
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.department_name
HAVING AVG(e.salary) > 60000;
