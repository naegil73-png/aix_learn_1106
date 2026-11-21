select * from employees;

-- select문 : 검색 기능
-- insert문 : 입력 기능
-- update문 : 수정 기능
-- delete문 : 삭제 기능

-- sql언어 : 
 -- ddl(테이블 관할언어, 복구 불가) - create, alter, drop
 -- dml(실행취소(commit rollback) 가능, 명령구문 마지막에 commit을 해야 실행됨) - 주요 업무권한일 듯
 -- dcl(권한부여)
 
 select * from employees;
 select employee_id, emp_name from employees;
 
 
 -- 삭제
drop table member; -- 실행하면 복구 불가
 
 
create table member(
id varchar2(20) primary key, 
pw varchar2(100) not null,
name varchar2(50),
phone varchar2(20)
);

select * from member;
insert into member(id,pw,name,phone) values(
'aaa','1111','홍길동','010-1111-1111'
);


insert into member values (
'bbb','1111','유관순','010-1111-1111'
);

insert into member values (
'ddd','1111','이순신','010-1111-1111'
);

select * from member;
commit;


-- 삭제

delete from member;

select * from member;
commit;
rollback;


delete from member where id='ccc';

select * from member;
commit;
rollback;


-- 수정

-- 아랫줄과 같이 하면 모든 비번이 0000이 됨
update member set pw='0000'; 
-- ccc만 비번을 0000으로 변경
update member set pw='0000' where id ='ccc';

update member set pw='4444' where id ='ddd';

select * from member;
commit;
rollback;






desc employees;


-- 사원번호

select emplployee_id, emp_name, hire_date, salary from employees;













-- 연산자 : 문자열은 +만 가능, 날짜는 +,-만 가능
-- 연산은 가급적 DB에서 하는 것이 좋음, sql로 계산 -> 아래와 같이 간단히 계산 가능

desc employees;

select salary+1000 from employees;
select salary-1000 from employees;
select salary*1000 from employees;
select salary/1000 from employees;


-- 이름, 사원번호, 월급과 연봉을 동시에 출력

select emp_name, employee_id, salary, salary*12 from employees;

-- 월급이 달러인데, 원화로 변경 -> 사원번호, 이름, 월급, 원화월급
select employee_id, emp_name, salary, salary*1329.8 from employees;


-- null은 미확정값(무한대) -> 사칙연산 불가

select emp_name,salary,salary+(salary*commission_pct) from employees;

-- 이 경우, 인센티브는 없으나, 월급은 있는데, null로 처리될 수 있음 -> null을 0으로 처리 필요

select emp_name, salary, nvl(commission_pct,0) as nvl,
salary+(salary*nvl(commission_pct, 0)) as last_salary
from employees;


select * from departments;

-- null 값 출력
-- manager가 100인 사원들을 출력하시오.
-- select 컬럼 from 테이블 조건절 where
select * from departments where manager_id=100;

-- manager가 200보다 작은 사원들을 출력하시오.
select * from departments where manager_id<=200;

-- null값인 사람을 찾으려면
select * from departments where manager_id is null; 


-- 2개의 컬럼ㅇ르 1개의 컬럼으로 출력하는 방법
select * from employees;
select emp_name,email from employees;
select emp_name || email as total from employees;
select concat(emp_name,email) from employees;


-- 매니저 아이디로 순차정렬, 역순정렬(desc)
-- distinct : 중복제거
select distinct(manager_id) from employees;
order by manager_id;

-- 갯수 출력
select count(*) from employees;



desc employees;
-- job_id를 중복제거해서 출력하시오
-- departments_id를 중복제거해서 출력하시오
-- 부서가 몇개 있는 지 출력하시오.
select distinct(job_id) from employees;
select distinct(department_id) from employees;
order by department_id;
select count(department_id) from employees;

select department_id from departments;


select emp_name, salary from employees
where salary>=5000;

select count(*) from employees
where salary>=5000;

select emp_name, salary from employees
where salary<=5000 or salary>=9000;

select count(*) from employees;

-- 총원 107명 -> 3천 아닌 105명
select salary from employees
where salary!=3000;

select salary from employees
where salary=3000 or salary=4000 or salary=5000;

select salary from employees
where salary in (3000,4000,5000);

-- 사원번호 150~200까지 출력
-- 사원번호 130번 이하, 180번 이상 출력
-- 사원번호가 110,130,140,150번을 출력

select * from employees;

select employee_id  from employees
where employee_id >=150 and employee_id <= 200;

select employee_id  from employees
where employee_id >=180 or employee_id <= 130;

select employee_id from employees
where employee_id in (110,130,140,150); 

select * from employees;

select * from employees
where email = 'DOCONNEL';

select * from employees
where emp_name = 'Donald OConneil';


-- 날짜 검색
select * from employees
where hire_date <= '2005/01/01';

select * from employees;

select employee_id from employees
where employee_id not in (110,130,140,150);


-- 급여가 5000~7000 사이 또는 8000,9000인 사원을 출력하시오.

select * from employees
where salary>=5000 and salary<=7000 or salary in (8000,9000);


-- 직급이 매니저이면서 부서번호 50인 사원을 출력(참고 : like는 포함한다는 의미)
select * from employees;
select job_id from employees where (job_id like '%man%') and department_id = 50;


-- 100~109번 사원정보를 순차적으로 출력
select * from employees
order by employee_id;

-- between은 양끝이 포함됨, not between도 있음
select * from employees
where employee_id between 100 and 109;

-- 130번부터 140번, 170번부터 180번까지 출력

select * from employees
where (employee_id between 130 and 140) or (employee_id between 170 and 180);


select * from employees
where employee_id in (110,120,130);

-- in을 쓰지 않고 위와 동일하게 출력
select * from employees
where employee_id = 110 or employee_id = 120 or employee_id =130;


-- like : 포함되어 있는, 
-- 's%' : 첫번째 글자가 s인 경우, %s는 끝글자가 s인 경우
-- '_e': 두번째 글자가 e인 것
select * from employees
where emp_name like '%s%';


-- 이름에 h가 포함된 직원

select * from employees
where emp_name like '%h%';


-- 이름의 9번째 글자가 h자인 직원

select * from employees
where emp_name like '________h%';



create table board(
-- bno,id,btitle,bcontent,bgroup,bstep,bindent,bhit,bdate,bfile
    bno number(4),
    id varchar2(30),
    btitle varchar2(1000),
    bcontent varchar2(2000),
    bgroup number(4),
    bstep number(4),
    bindent number(4),
    bhit number(4),
    bdate date,
    bfile varchar2(100)
    );
    
    drop table board;


select * from board
order by bno;








-- btitle에 사진이 들어가 있는 게시글을 출력하시오 -> 게시판의 경우 디장고로 해도 이렇게 전환해서 실행함
select * from board
where btitle like '%사진%';



-- btitle, bcontent에 사진이 들어가 있는 게시글을 출력하시오
select * from board
where btitle  like '%사진%' or bcontent like '%사진%';

select * from board
where bno between 11 and 20;


-- 함수
select lower(id) from board;


-- bdate에서 연도를 슬라이싱해서 substr로 할당
select bdate,substr(bdate,0,2) from board;

-- 월말 출력
select bdate,substr(bdate,4,2) from board;


-- 소문자, 대문자 A, a가 들어가 있는 id를 출력
select id from board
where lower(id) like '%a%';


select job_id from employees;


select job_id from employees
where job_id like '%_%';


-- null 검색
select * from employees
where manager_id is null;


-- 정렬
-- 순차정렬 order by asc, 역순정렬 order by desc
select * from board
order by bno asc;

-- 부서 id로 역순정렬, 고용일 순차정렬 : 정렬 시 null값은 순차면 제일 아래, 역순이면 맨 처음
select department_id,hire_date from employees
order by department_id desc, hire_date asc


-- 월급으로 역순정렬 출력하시오
select salary from employees
order by salary desc;



-- 사원명으로 순차정렬하시오
select emp_name from employees
order by emp_name asc;