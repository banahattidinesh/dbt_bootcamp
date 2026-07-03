SELECT
    match_id,
    season,
    team1,
    team2,
    winner,
    win_by_runs
FROM {{ source('my_raw_data', 'ipl_raw_stats') }}