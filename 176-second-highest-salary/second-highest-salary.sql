with t as (
    select salary, dense_rank() over(order by salary desc) as sal_rank
    from Employee
)
select max(salary) as SecondHighestSalary
from t
where sal_rank = 2;