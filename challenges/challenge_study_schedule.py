def study_schedule(permanence_periods, target_time):
    if not target_time or not permanence_periods:
        return None

    students = 0

    for period in permanence_periods:
        if not all(isinstance(time, int) for time in period):
            return None
        start_time, end_time = period
        if start_time <= target_time <= end_time:
            students += 1

    return students
