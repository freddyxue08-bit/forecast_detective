import json


def build_clues(daily):
    hottest = max(daily["temperature_2m_max"])
    hottest_i = daily["temperature_2m_max"].index(hottest)

    coldest = min(daily["temperature_2m_min"])
    coldest_i = daily["temperature_2m_min"].index(coldest)

    total_rain = round(sum(daily["precipitation_sum"]), 1)

    shortest_daylight=seconds_to_hours(min(daily["daylight_duration"]))
    longest_daylight =seconds_to_hours(max(daily["daylight_duration"]))

    return {
        "hottest": {"date": daily["time"][hottest_i], "temp_c": hottest},
        "coldest": {"date": daily["time"][coldest_i], "temp_c": coldest},
        "total_rain_mm": total_rain,
        "daylight_hours": {"shortest": shortest_daylight,
        "longest": longest_daylight}
    }

def seconds_to_hours(seconds):
    return round(seconds/3600,1)
if __name__ == "__main__":
    with open("tests/fixtures/toronto_2025.json") as f:
        weather = json.load(f)
    print(build_clues(weather["daily"]))
