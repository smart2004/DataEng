-- Пример использования оконной функции для ранжирования сотрудников по зарплате
SELECT name, salary,
RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;

-- Пример использования оконной функции для вычисления средней зарплаты по отделам
SELECT name, salary, department_id,
AVG(salary) OVER (PARTITION BY department_id) AS avg_department_salary
FROM employees;
