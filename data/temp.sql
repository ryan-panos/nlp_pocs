do $$ 
declare 
  _upgrade int; 
begin 
  select 123 into _upgrade; 
  if schema_upgrade_needed(_upgrade) then  

    create table if not exists entity_sentiment     (
      entity_sentiment_id        bigserial   not null  PRIMARY KEY 
      , entity_id                bigint      not null  REFERENCES entities (entity_id)
      , sentiment_id             bigint      not null  REFERENCES d_sentiment (sentiment_id)
      unique (entity_id, sentiment_id)
    );


    -- NEEDED?
    create unique index entity_sentiment on entities (category, entity);

  perform schema_upgrade_completed(_upgrade);
end if;
end $$;