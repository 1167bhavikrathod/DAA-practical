"""1. Implement the Activity Selection problem to find
the maximum number of activities a single person
can perform."""

def activitySelection(activities):
    activities.sort(key=lambda i : i[1])
    
    selected = []
    last_finish = -1

    for start,finish in activities:
        if start>=last_finish:
            selected.append((start,finish))
            last_finish = finish
    return selected

activities = [(1, 3), (2, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
selected_activities = activitySelection(activities)
print(f"maximum activities: {len(selected_activities)}")
for act in selected_activities:
    print(act)