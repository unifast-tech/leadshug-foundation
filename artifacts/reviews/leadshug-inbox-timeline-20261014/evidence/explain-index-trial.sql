\set ON_ERROR_STOP on
CREATE INDEX messages_conversation_created_at_id_timeline_trial_idx ON messages (conversation_id, created_at DESC, id DESC);
ANALYZE messages;
SELECT created_at AS anchor_created_at, id AS anchor_id FROM messages WHERE conversation_id='f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' ORDER BY created_at DESC, id DESC OFFSET 10000 LIMIT 1 \gset
\echo === EXACT_DEEP_CURSOR_WITH_CANDIDATE_INDEX ===
EXPLAIN (ANALYZE, BUFFERS, SUMMARY) SELECT id, direction, message_type, content, channel_origin, author_name, created_at FROM messages WHERE conversation_id = 'f0619bbd-9e54-418f-9bf9-a5cc0b6c5673' AND (created_at < :'anchor_created_at'::timestamptz OR (created_at = :'anchor_created_at'::timestamptz AND id < :'anchor_id'::text)) ORDER BY created_at DESC, id DESC LIMIT 51;
