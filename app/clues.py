import json


def build_clues(daily):
    hottest = max(daily["temperature_2m_max"])
    hottest_i = daily["temperature_2m_max"].index(hottest)

    coldest = min(daily["temperature_2m_min"])
    coldest_i = daily["temperature_2m_min"].index(coldest)

    total_rain = round(sum(daily["precipitation_sum"]), 1)

    return {
        "hottest": {"date": daily["time"][hottest_i], "temp_c": hottest},
        "coldest": {"date": daily["time"][coldest_i], "temp_c": coldest},
        "total_rain_mm": total_rain,
    }


if __name__ == "__main__":
    with open("tests/fixtures/toronto_2025.json") as f:
        weather = json.load(f)
    print(build_clues(weather["daily"]))
