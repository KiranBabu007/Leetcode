# Write your MySQL query statement below
Select c.name as Customers from Customers as c left join Orders as o on c.id=o.customerID where O.customerId IS NULL