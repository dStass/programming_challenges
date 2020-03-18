MINUTES_IN_ONE_HOUR = 60

def return_slots(timetable1, bound1, timetable2, bound2, meeting_time):
    lower_bound = bound1[0] if convert_time_to_total_minutes(bound1[0]) > convert_time_to_total_minutes(bound2[0]) else bound2[0]
    upper_bound = bound1[1] if convert_time_to_total_minutes(bound1[1]) < convert_time_to_total_minutes(bound2[1]) else bound2[1]
    bounds = [lower_bound, upper_bound] 

    timetables = [timetable1, timetable2]  # contains pairs of each index and individual timetable
    combined_schedule = generate_combined_schedule(timetables)
    combined_schedule = enforce_bounds(combined_schedule, bounds) 
    
    # combined schedule intuitively means times unavailable for a meeting
    unavailable = combined_schedule

    # get the opposite available times for meeting
    available = get_available_from_unavailable(unavailable)

    # filter out slots that are at least meeting_time length
    available_meetings = [a for a in available if convert_time_to_total_minutes(a[1]) - convert_time_to_total_minutes(a[0]) >= meeting_time]

    return available_meetings


def difference(time1, time2):

    # ensure time2 > time1
    if convert_time_to_total_minutes(time1) > convert_time_to_total_minutes(time2):
        time1, time2 = time2, time1

    time1_split = time1.split(':')
    hours1 = int(time1_split[0])
    minutes1 = int(time1_split[1])

    time2_split = time2.split(':')
    hours2 = int(time2_split[0])
    minutes2 = int(time2_split[1])

    minute_difference = minutes2 - minutes1
    hours_difference = hours2 - hours1
    if minute_difference < 0:
        minute_difference = minute_difference % MINUTES_IN_ONE_HOUR
        hours_difference -= 1

    time = str(hours_difference) + ':' + str(minute_difference)
    return convert_time_to_total_minutes(time)



def convert_time_to_total_minutes(time):
    time_split = time.split(':')
    hours = int(time_split[0])
    minutes = int(time_split[1])
    return hours * MINUTES_IN_ONE_HOUR + minutes



def generate_combined_schedule(timetables):
    combined = []

    # generate a long combined list of non-availabilities
    while timetables:
        index = 0
        first_timetable = timetables[0]
        first_slot = first_timetable[0]
        first_start = first_slot[0]
        min_time = convert_time_to_total_minutes(first_start)  # first timetable, second position, first time_slot
        
        # let x = extract the next earliest meeting occurence using the fact that each timetables are sorted by meeting_from time
        # we then build a combined meetings timetable/schedule
        # done by either: 
        #   if x is inside the LAST combined slot (ie x.from <= last.to) {x.from <= last.from is assumed due to assumption }
        #   extending slots (changing the to of each meeting if they overlap) so that
        # 
        for i, timetable in enumerate(timetables):
            curr_slot = timetable[0]
            curr_start = curr_slot[0]
            curr_start_time = convert_time_to_total_minutes(curr_start)
            if curr_start_time < min_time:
                index = i
                min_time = curr_start_time

        if not combined:
            timetable = timetables[index]
            first_slot = [timetable[0][0], timetable[0][1]]
            combined.append(first_slot)
            timetable.pop(0)

            # if timetable doesn't exist, remove it from timetables
            if not timetable:
                timetables.pop(index)
            continue
        
        # combined exists ie not first time running, run following . . . 

        # get latest combined time slot and split into from and to
        last_combined = combined[-1]
        last_from = last_combined[0]
        last_to = last_combined[1]

        # get new data
        timetable = timetables[index]
        new_slot = [timetable[0][0], timetable[0][1]]
        new_from = new_slot[0]
        new_to = new_slot[1]

        # handle logic, first_slot_from MUST be atleast combined[-1]_from
        # if first_slot_from > combined[-1]_to then add a new time to combined
        # else change combined[-1]_to to first_slot_to
        if convert_time_to_total_minutes(new_from) > convert_time_to_total_minutes(last_to):
            combined.append(new_slot)
        else:
            if convert_time_to_total_minutes(new_to) > convert_time_to_total_minutes(last_to):
                combined[-1][1] = new_to
        
        timetable.pop(0)
        if not timetable:
            timetables.pop(index)

    return combined


def enforce_bounds(combined, bounds):
    # combined = [[HH:MM, HH:MM], ...],  bounds = [HH:MM, HH:MM]
    EARLIEST = '00:00'
    LATEST = '23:59'
    bound_from_val = convert_time_to_total_minutes(bounds[0])
    bound_to_val = convert_time_to_total_minutes(bounds[1])

    # remove blocks with ending time earlier than bounds_from
    combined = [c for c in combined if convert_time_to_total_minutes(c[1]) >= bound_from_val]
    
    # similarly remove blocks with starting time AFTER bound to
    combined = [c for c in combined if convert_time_to_total_minutes(c[0]) <= bound_to_val]

    first = combined[0]
    first_from_val = convert_time_to_total_minutes(first[0])
    last = combined[-1]
    last_to_val = convert_time_to_total_minutes(last[-1])


    if first_from_val > bound_from_val:
        combined.insert(0, [EARLIEST, bounds[0]])
    else:
        combined[0][0] = bounds[0]
    
    if last_to_val < bound_to_val:
        combined.append([bounds[1], LATEST])
    else:
        combined[-1][1] = bounds[1]


    # print("comb=", combined)

    return combined 


def get_available_from_unavailable(unavailable):
    available = []
    for i in range (1, len(unavailable)):
        prev = unavailable[i-1]
        curr = unavailable[i]
        available.append([prev[1], curr[0]])
    return available


print(return_slots(
    [['9:00', '10:30'],   ['12:00', '13:00'],   ['16:00', '18:00']],
    ['8:00', '20:00'],

    [['10:00', '11:30'],   ['12:30', '14:30'],   ['14:30', '15:00'],   ['16:00', '17:00']],
    ['9:00', '19:30'],

    30
    ))