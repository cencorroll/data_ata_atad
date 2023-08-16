-- Data required to complete some sections of the project is missing from the Employee_Payroll_2023.csv dataset --

-- Salary Analysis --
select avg(total_pay) from payment;
select max(total_pay) from payment;
select min(total_pay) from payment;

select 
	e.employee_no, 
    j.job_title, 
    p.total_pay 
from payroll_index pi
join employee_info e on pi.employee_no = e.employee_no
join job j on pi.job_data_id = j.job_data_id
join payment p on pi.payment_data_id = p.payment_data_id
where p.total_pay = (select max(total_pay) from payment);

select 
	e.employee_no, 
    j.job_title, 
    p.total_pay 
from payroll_index pi
join employee_info e on pi.employee_no = e.employee_no
join job j on pi.job_data_id = j.job_data_id
join payment p on pi.payment_data_id = p.payment_data_id
where p.total_pay = (select min(total_pay) from payment);

select 
	d.department_title, 
    round(avg(p.total_pay),2) as average_total_pay
from payroll_index pi
join department d on pi.department_data_id = d.department_data_id
join payment p on pi.payment_data_id = p.payment_data_id
group by d.department_title
order by average_total_pay asc;

select 
	d.department_title, 
    round(min(p.total_pay),2) as lowest_total_pay, 
    round(max(p.total_pay),2) as highest_total_pay
from payroll_index pi
join department d on pi.department_data_id = d.department_data_id
join payment p on pi.payment_data_id = p.payment_data_id
group by d.department_title
order by lowest_total_pay asc;

select 
	j.job_title, 
    round(avg(p.total_pay),2) as average_total_pay
from payroll_index pi
join job j on pi.job_data_id = j.job_data_id
join payment p on pi.payment_data_id = p.payment_data_id
group by j.job_title
order by average_total_pay asc;

select 
	j.job_title, 
	round(min(p.total_pay),2) as lowest_total_pay, 
    round(max(p.total_pay),2) as highest_total_pay
from payroll_index pi
join job j on pi.job_data_id = j.job_data_id
join payment p on pi.payment_data_id = p.payment_data_id
group by j.job_title
order by lowest_total_pay asc;

-- Employee demographics --
select 
	gender, 
    count(gender) 
from employee_info
group by gender;

select 
	ethnicity, 
    count(ethnicity) 
from employee_info
group by ethnicity;

select 
	d.department_title, 
	count(distinct(e.ethnicity)) as number_of_ethnicities, 
    count(e.ethnicity) as number_of_employees
from payroll_index pi
join employee_info e on pi.employee_no = e.employee_no
join department d on pi.department_data_id = d.department_data_id
group by d.department_title
order by d.department_title asc;

-- Overtime analysis --
select 
	e.employee_no, 
	p.overtime_pay
from payroll_index pi
join employee_info e on pi.employee_no = e.employee_no
join payment p on pi.payment_data_id = p.payment_data_id
order by p.overtime_pay desc
limit 5;

select * from payment;

-- Department analysis --
select 
	d.department_title, 
	count(e.employee_no) as number_of_employees, 
    round(sum(p.total_pay),2) as total_salaries, 
    round(sum(rb.benefit_pay),2) as total_benefits
from payroll_index pi
join department d on pi.department_data_id = d.department_data_id
join employee_info e on pi.employee_no = e.employee_no
join payment p on pi.payment_data_id = p.payment_data_id
join retirement_and_benefits rb on pi.rb_data_id = rb.rb_data_id
group by d.department_title;

select 
	department_title, 
    number_of_employees, 
    total_salaries,
	round(total_salaries / number_of_employees, 2) as cost_per_employee
from(
	select 
		d.department_title, 
		count(e.employee_no) as number_of_employees, 
		sum(p.total_pay) as total_salaries
	from payroll_index pi
	join department d on pi.department_data_id = d.department_data_id
	join employee_info e on pi.employee_no = e.employee_no
	join payment p on pi.payment_data_id = p.payment_data_id
	group by d.department_title
)
as outer_query
order by cost_per_employee desc;

select 
	department_title, 
    number_of_employees, 
    total_salaries,
	ROUND(total_salaries / number_of_employees, 2) as cost_per_employee
from(
	select 
		d.department_title, 
		count(e.employee_no) as number_of_employees, 
		sum(p.total_pay) as total_salaries
	from payroll_index pi
	join department d on pi.department_data_id = d.department_data_id
	join employee_info e on pi.employee_no = e.employee_no
	join payment p on pi.payment_data_id = p.payment_data_id
	group by d.department_title
)
as outer_query
order by cost_per_employee asc;