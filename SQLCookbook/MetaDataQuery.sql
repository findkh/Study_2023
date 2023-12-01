-- 5.1 스키마의 테이블 목록 보기
-- SEMAGOL 스키마에서 작업한다고 가정

select table_name
from information_schema.tables
where table_schema = 'SMEAGOL'

-- 5.2 테이블의 열 나열하기
select column_name, data_type, ordinal_position
from information_schema.columns
where table_schema = 'SMEAGOL' and table_name = 'EMP'

-- 5.3 테이블의 인덱싱된 열 나열하기
select a.tablename, a.indexname, b.column_name
from pg_catalog.pg_indexes a, information_schema.columns b
where a.schemaname = 'SMEAGOL' and a.tablename = b.table_name

-- 5.4 테이블의 제약조건 나열
select a.table_name, a.constraint_name, b.column_name, a.constraint_type
from information_schema.table_constraints a,
     information_schema.key_column_usage b
where a.table_name      = 'EMP'
  and a.table_schema    = 'SMEAGOL'
  and a.table_name      = b.table_name
  and a.table_schema    = b.table_schema
  and a.constraint_name = b.constraint_name
  
-- 5.5 관련 인덱스가 없는 외래 키 나열하기
select fkeys.table_name, fkeys.constraint_name, fkeys.column_name, ind_cols.indexname
from(
    select a.constraint_schema, a.table_name, a.constraint_name, a.column_name
    from information_schema.key_column_usage a,
         information_schema.referential_constraints b
    where a.constraint_name = b.constraint_name
      and a.constraint_schema = b.constraint_schema
      and a.constraint_schema = 'SMEAGOL'
      and a.table_name        = 'EMP'
) fkeys
    left join(
        select a.schemaname, a.tablename, a.indexname, b.column_name
        from pg_catalog.pg_indexes a, information_schema.columns b
        where a.tablename = b.table_name
          and a.schemaname = b.table_schema
    ) ind_cols 
    on (
        fkeys.constraint_schema = ind_cols.schemaname
        and fkeys.table_name    = ind_cols.tablename
        and fkeys.column_name   = ind_cols.column_name
    )
where ind_cols.indexname is null
  