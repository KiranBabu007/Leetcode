# Write your MySQL query statement below
select project_id,Round(AVG(experience_years),2) average_years from Project p join employee e using(employee_id) Group by project_id