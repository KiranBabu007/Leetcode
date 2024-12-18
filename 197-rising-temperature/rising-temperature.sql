# Write your MySQL query statement below
Select w2.id from Weather w1 join Weather w2 on DATEDIFF(w1.recordDate,w2.recordDate)=-1
Where w2.temperature > w1.temperature