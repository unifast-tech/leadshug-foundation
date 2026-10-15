\set ON_ERROR_STOP on
DROP INDEX IF EXISTS messages_conversation_created_at_id_timeline_trial_idx;
ANALYZE messages;
SELECT created_at AS deep_created_at, id AS deep_id FROM messages WHERE conversation_id='f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' ORDER BY created_at DESC, id DESC OFFSET 10000 LIMIT 1 \gset
SELECT created_at AS tie_created_at, id AS tie_id FROM messages WHERE conversation_id='f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' ORDER BY created_at DESC, id DESC OFFSET 500 LIMIT 1 \gset
\echo === RECENT production-equivalent, conversation_id + order + limit+1 ===
EXPLAIN (ANALYZE, BUFFERS, SUMMARY) SELECT id, direction, message_type, content, channel_origin, author_name, created_at FROM messages WHERE conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' ORDER BY created_at DESC, id DESC LIMIT 51;
\echo === DEEP production-equivalent cursor constants ===
EXPLAIN (ANALYZE, BUFFERS, SUMMARY) SELECT id, direction, message_type, content, channel_origin, author_name, created_at FROM messages WHERE conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' AND (created_at < :'deep_created_at'::timestamptz OR (created_at = :'deep_created_at'::timestamptz AND id < :'deep_id'::text)) ORDER BY created_at DESC, id DESC LIMIT 51;
\echo === LARGE_TIMESTAMP_TIE production-equivalent cursor constants ===
EXPLAIN (ANALYZE, BUFFERS, SUMMARY) SELECT id, direction, message_type, content, channel_origin, author_name, created_at FROM messages WHERE conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' AND (created_at < :'tie_created_at'::timestamptz OR (created_at = :'tie_created_at'::timestamptz AND id < :'tie_id'::text)) ORDER BY created_at DESC, id DESC LIMIT 51;
