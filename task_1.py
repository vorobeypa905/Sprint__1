time_str = '1h 45m,360s,25m,30m 120s,2h 60s'
periods = time_str.split(',')
total_sum = 0

for period in periods:
    segments = period.split()
    segment_minutes = 0
    for segment in segments:
        if 'h' in segment:
            hours = int(segment.replace('h', ''))
            segment_minutes += hours * 60
        elif 'm' in segment:
            minutes = int(segment.replace('m', ''))
            segment_minutes += minutes
        elif 's' in segment:
            seconds = int(segment.replace('s', ''))
            segment_minutes += seconds // 60
    total_sum += segment_minutes

print(total_sum)


