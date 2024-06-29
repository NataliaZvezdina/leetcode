with t as (
    select num, id,
        lead(num) over(order by id) as nxt_num,
        lead(num, 2) over(order by id) as nxt2_num,
        lead(id) over(order by id) as nxt_id,
        lead(id, 2) over(order by id) as nxt2_id 
    from logs
)
select distinct num as ConsecutiveNums
from t
where num = nxt_num and num = nxt2_num
  and nxt_id = id + 1 and nxt2_id = id + 2;