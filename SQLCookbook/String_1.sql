-- 6.1 문자열 짚어보기
-- emp 테이블의 ename인 'KING'을 4개 행으로 표시, 각 행은 KING 문자열만 포함한다.
select substr(e.ename,iter.pos,1) as C
from (select ename from emp where ename='KING')as e,
     (select id as pos from t10) iter
where iter.pos <= length(e.ename)

select ename, iter.pos
from (select ename from emp where ename='KING')as e,
     (select id as pos from t10) iter

select substr(e.ename, iter.pos) a,
       substr(e.ename, length(e.ename)-iter.pos+1) b
from (select ename from emp where ename = 'KING') e,
     (select id pos from t10) iter
where iter.pos <= length(e.ename)

-- 6.2 문자열에 따옴표 포함하기 - 값이 안나옴
--select 'apples core', 'apple','s core', case when '' is null then 0 else 1 end
--from t1

-- 6.3 문자열에서 특정 문자의 발생 횟수 계산하기
-- '10,CLARK,MANAGER' 이 문장에서 쉼표가 몇개 있는지 확인
select(length('10,CLARK,MANAGER')) - length(replace('10,CLARK,MANAGER', ',', ''))/length(',') as cnt
from t1
-- -> 전체 문자 개수 - 쉼표를 제거한 문자 개수 = 쉼표의 개수
-- 나누기를 하는 이유 : 찾고 있는 문자열의 길이가 1보다 클 때 필요하다.

select
    (length('HELLO HELLO') - length(replace('HELLO HELLO', 'LL', '')))/length('LL') as correct_cnt,
    length('HELLO HELLO') - length(replace('HELLO HELLO', 'LL', '')) as incorrect_cnt
from t1

select
       (length('HELLO HELLO')- length(replace('HELLO HELLO','LL','')))/length('LL')
       as correct_cnt,
       (length('HELLO HELLO')-
       length(replace('HELLO HELLO','LL',''))) as incorrect_cnt
from t1

-- 6.4 문자열에서 원하지 않는 문자 제거
select ename, replace(translate(ename, 'aaaa', 'AEIOU'), 'a', '') as stripped1, sal, replace(cast(sal as char(4)) , '0', '') as stripped2
from emp

-- 6.5 숫자 및 문자 데이터 분리하기

select replace(
        translate(data, '0123456789', '0000000000'), '0', '') as ename,
        cast(
            replace(
            translate(lower(data),
                     'abcdefghijklmnopqrstuvwxyz',
                      rpad('z',26,'z')),'z','') as integer) as sal
from (
    select ename||sal as data
    from emp
) x

select data, translate(lower(data), 'abcdefghijklmnopqrstuvwxyz', rpad('z',26,'z')) sal
from (select ename||sal as data from emp) x


--6.6 문자열의 영숫자 여부 확인하기
-- 숫자와 문자 이외의 문자가 포함되지 않을 때만 테이블에서 행을 반환

create view v4 as
    select ename as data
    from emp
    where deptno = 10
    union all 
    select ename||', $'|| cast(sal as char(4)) ||'.00' as data
    from emp
    where deptno = 20
    union all 
    select ename || cast (deptno as char(4)) as data
    from emp
    where deptno = 30

select * from v4

select data
from v4
where translate(lower(data),
                '0123456789abcdefghijklmnopqrstuvwxyz',
                rpad('a', 36, 'a')) = rpad('a', length(data), 'a')
                
select data, translate(lower(data), '0123456789abcdefghijklmnopqrstuvwxyz', rpad('a', 36, 'a'))
from v4

select data, 
       translate(lower(data), '0123456789abcdefghijklmnopqrstuvwxyz', rpad('a', 36, 'a')) translated,
       rpad('a', length(data), 'a') fixed
from v4

-- 6.7 이름에서 이니셜 추출
select translate(replace('Stewie Griffin', '.', ''),
                 '0123456789abcdefghijklmnopqrstuvwxyz',
                 rpad('#', 26, '#'))
from t1

select replace( 
       translate(replace('Stewie Griffin', '.', ''),
                 '0123456789abcdefghijklmnopqrstuvwxyz',
                 rpad('#', 26, '#')), '#', '')
from t1

select replace(
            replace(
                translate(replace('Stewie Griffin', '.', ''), 
                '0123456789abcdefghijklmnopqrstuvwxyz',
                rpad('#', 26, '#') ), '#', ''),' ', '.') || '.'
from t1

-- 6.8 문자열 일부를 정렬하기
select ename from emp

select ename from emp
order by substr(ename, length(ename)-1,2)

-- 6.9 문자열의 숫자로 정렬하기
create view v5 as
    select e.ename || ' '||
           cast(e.empno as char(4))|| ' '||
           d.dname as data
    from emp e, dept d
    where e.deptno = d.deptno

select * from v5

select data
from v5
order by
    cast(replace(translate(data,
      replace(translate(data,'0123456789','##########'),'#',''), rpad('#',20,'#')),'#','') as integer)
      
-- 6.10 테이블 행으로 구분된 목록
select deptno, ename as emps from emp

-- deptno가 같은 사람을 쉼표로 구분된 값으로 반환한다. 
-- 예제 실행 안됨
--select deptno, string_agg(ename order by empno separator, ',') as emps
--from emp e 
--group by deptno

-- 값 나오게 수정함
select deptno, string_agg(ename, ',' order by ename) as emps
from emp e 
group by deptno
order by deptno

select deptno, ename, row_number() over (partition by deptno order by empno) rn, count(*) over (partition by deptno) cnt
from emp