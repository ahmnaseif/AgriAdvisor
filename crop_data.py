import pandas as pd

def generate_sentences(crop):
    # Load crop data
    crop_data = pd.read_csv("crop_data.csv")

    # Extract relevant information
    crop_info = crop_data[crop_data['crop'] == crop]
    if crop_info.empty:
        return "No information found for that crop."

    planting_season = crop_info['planting_season'].values[0]
    harvest_season = crop_info['harvest_season'].values[0]
    soil_type = crop_info['soil_type'].values[0]
    climate = crop_info['climate'].values[0]
    water_requirements = crop_info['water_requirements'].values[0]
    yield_per_unit = crop_info['yield_per_unit'].values[0]

    # Generate sentences
    sentences = [
        f"The planting season for {crop} is {planting_season}.",
        f"{crop} thrives in {soil_type} soil.",
        f"The ideal climate for {crop} is {climate}.",
        f"{crop} requires {water_requirements} for optimal growth.",
        f"The expected yield of {crop} is {yield_per_unit} per unit."
    ]

    return "\n".join(sentences)