# Write your MySQL query statement below
Select customer_id,count(v.visit_id) as count_no_trans from Visits as v left join Transactions as t on (t.visit_id=v.visit_id) where t.visit_id is NULL group by (customer_id)