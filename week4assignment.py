def calculate_calories_burned(exercise_type, duration_minutes, intensity):
    if exercise_type == "cardio":
        if intensity == "low":
            calories_per_min = 8
        elif intensity == "medium":
            calories_per_min = 12
        else:
            calories_per_min = 16
    elif exercise_type == "strength":
        if intensity == "low":
            calories_per_min = 6
        elif intensity == "medium":
            calories_per_min = 9
        else:
            calories_per_min = 12
    elif exercise_type == "flexibility":
        if intensity == "low":
            calories_per_min = 3
        elif intensity == "medium":
            calories_per_min = 5
        else:
            calories_per_min = 7
    else:
        calories_per_min = 0

    total_calories = calories_per_min * duration_minutes
    return total_calories


def calculate_heart_rate_zone(age, resting_hr, exercise_hr):
    max_hr = 220 - age
    heart_rate_reserve = max_hr - resting_hr
    intensity_percent = (exercise_hr - resting_hr) / heart_rate_reserve * 100
    return intensity_percent


def determine_training_zone(intensity_percent):
    if intensity_percent < 50:
        return "Warm-up Zone"
    elif intensity_percent < 60:
        return "Fat Burn Zone"
    elif intensity_percent < 70:
        return "Cardio Zone"
    elif intensity_percent <= 85:
        return "Performance Zone"
    else:
        return "Maximum Effort Zone"


def calculate_workout_score(calories, duration, zone_multiplier):
    base_score = calories * 0.1 + duration * 2
    final_score = base_score * zone_multiplier
    return round(final_score, 1)


def needs_rest_day(consecutive_days, total_minutes, avg_intensity):
    if consecutive_days >= 6:
        return True
    elif total_minutes > 450 and avg_intensity > 70:
        return True
    elif consecutive_days >= 4 and avg_intensity > 80:
        return True
    else:
        return False


def generate_workout_report(name, exercise_type, duration, intensity, age, resting_hr, exercise_hr, consecutive_days):
    
    print(f"Workout Report for: {name}")
    print("----------------------------------------")
    print(f"Exercise Type: {exercise_type}")
    print(f"Duration: {duration} minutes")
    print(f"Intensity Level: {intensity}")

    calories = calculate_calories_burned(exercise_type, duration, intensity)
    print(f"Calories Burned: {calories}")

    intensity_percent = calculate_heart_rate_zone(age, resting_hr, exercise_hr)
    zone = determine_training_zone(intensity_percent)

    print("Heart Rate Analysis:")
    print(f"  Age: {age}, Resting HR: {resting_hr}, Exercise HR: {exercise_hr}")
    print(f"  Intensity: {round(intensity_percent, 1)}%")
    print(f"  Training Zone: {zone}")

    if zone == "Warm-up Zone":
        zone_multiplier = 0.5
    elif zone == "Fat Burn Zone":
        zone_multiplier = 1.0
    elif zone == "Cardio Zone":
        zone_multiplier = 1.2
    elif zone == "Performance Zone":
        zone_multiplier = 1.5
    else:
        zone_multiplier = 1.8

    score = calculate_workout_score(calories, duration, zone_multiplier)
    print(f"Workout Score: {score}")

    total_minutes = duration
    avg_intensity = intensity_percent
    rest_needed = needs_rest_day(consecutive_days, total_minutes, avg_intensity)

    print(f"Consecutive Training Days: {consecutive_days}")
    if rest_needed:
        print("Rest Day Recommended: Yes")
    else:
        print("Rest Day Recommended: No")
    print()


print("FITNESS PERFORMANCE TRACKER")
print("========================================")

generate_workout_report("Alex", "cardio", 45, "high", 28, 65, 155, 3)
print("========================================")

generate_workout_report("Jordan", "strength", 60, "medium", 35, 70, 140, 5)
print("========================================")

generate_workout_report("Casey", "flexibility", 30, "low", 42, 68, 95, 7)
