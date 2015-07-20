drop table if exists book;

create table book (
  book_id bigserial primary key,
  url varchar not null,
  title varchar not null,
  text text not null
);

create index on book(title);
