CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) 
RETURNS TABLE (Salary INT) 
AS $$
BEGIN
  RETURN QUERY
    with t as (
        select e.salary, 
               dense_rank() over(order by e.salary desc) as sal_rank
        from Employee e
    )
    select distinct(t.salary)
    from t
    where sal_rank = N  
  ;
END;
$$ LANGUAGE plpgsql;