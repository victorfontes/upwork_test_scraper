SELECT
    events.name as event_name,
    events.date as event_date,
    f1.name as f1,
    f2.name as f2
FROM
    event_fights
INNER JOIN events  as events on (event_fights.event_id = events.id)
INNER JOIN fighters as f1 on (event_fights.fighter1_id = f1.id)
INNER JOIN fighters as f2 on (event_fights.fighter2_id = f2.id);