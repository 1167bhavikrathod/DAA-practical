"""Solve the Activity Selection problem where
activities have given start and finish times."""

def activitySelection(activities):
    activities.sort(key=lambda i : i[1])
    
    selected = []
    last_finish = -1

    for start,finish in activities:
        if start>=last_finish:
            selected.append((start,finish))
            last_finish = finish
    return selected

activities = [(1.00, 3.00), (2.00, 5.00), (0.00, 6.00), (5.00, 7.00), (8.00, 9.00), (5.00, 9.00)]
selected_activities = activitySelection(activities)
print(f"maximum activities: {len(selected_activities)}")
for act in selected_activities:
    print(act)