drop table if exists book;
drop function if exists book_trigger();

create table book (
  book_id bigserial primary key,
  url varchar not null,
  title varchar not null,
  text text not null,
  search_ix tsvector not null
);

CREATE INDEX titlesearch_ix ON book USING gin(to_tsvector('pg_catalog.english', title));

CREATE FUNCTION book_trigger() RETURNS trigger AS $$
begin
  new.search_ix :=
     setweight(to_tsvector('pg_catalog.english', new.title), 'A') ||
     setweight(to_tsvector('pg_catalog.english', new.text), 'C');
  return new;
end
$$ LANGUAGE plpgsql;

CREATE TRIGGER book_search_trigger BEFORE INSERT OR UPDATE
    ON book FOR EACH ROW EXECUTE PROCEDURE book_trigger();

CREATE INDEX booksearch_ix ON book USING gin(search_ix);

