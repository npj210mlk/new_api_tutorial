import os
import json
from dotenv import load_dotenv
import requests
import pandas as pd
import numpy as np
import tiktoken
from datetime import datetime, timedelta

# set up the log for our cat api calls
cat_api_call_log = []

def garfield(save_path = "preened_cat_api_data.csv",
        limit = 10,
        verbose = False
            ):
    """
    Single function that calls The Cat API, flattens the JSON, and returns an easy-to-read .csv file for facilitated Prompt Engineering
    """

    global cat_api_call_log
    
    load_dotenv()
    cat_apikey = os.environ.get("cat_apikey")
    if not cat_apikey:
        raise ValueError("There is no 'cat_apikey' in your environment variables.")
    url = f"https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit={limit}"
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': cat_apikey
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        call_response = response.json()

        # track the call time and put it in the 'cat_api_call_log'
        now = datetime.now()
        cat_api_call_log.append(now)

        # number of api calls the past 24 hours
        cutoff = now - timedelta(days=1)
        recent_calls = [call for call in cat_api_call_log if call > cutoff]
        print(f"Number of API calls the last 24 hours: {len(recent_calls)}")

        
    except requests.exceptions.RequestException as e:
        print(f"Sorry. We could not execute your API call properly: {e}")
        return pd.DataFrame()  # empty fallback

    if verbose:
        print(json.dumps(call_response, indent=2))


    # running token count
    encoding = tiktoken.get_encoding("cl100k_base")
    token_count = len(encoding.encode(json.dumps(call_response)))

    print(f"Your api call consumed {token_count} tokens.")

    # flatten out the data
    data = []
    for item in call_response:
        for breed in item.get("breeds", []):
            data.append({
                "id": breed.get("id"),
                "name": breed.get("name"),
                "cfa_url": breed.get("cfa_url"),
                "vetstreet_url": breed.get("vetstreet_url"),
                "vcahospitals_url": breed.get("vcahospitals_url"),
                "temperament": breed.get("temperament"),
                "origin": breed.get("origin"),
                "country_codes": breed.get("country_codes"),
                "country_code": breed.get("country_code"),
                "description": breed.get("description"),
                "life_span": breed.get("life_span"),
                "indoor": breed.get("indoor"),
                "lap": breed.get("lap"),
                "alt_names": breed.get("alt_names"),
                "adaptability": breed.get("adaptability"),
                "affection_level": breed.get("affection_level"),
                "child_friendly": breed.get("child_friendly"),
                "dog_friendly": breed.get("dog_friendly"),
                "cat_friendly": breed.get("cat_friendly"),
                "energy_level": breed.get("energy_level"),
                "grooming": breed.get("grooming"),
                "health_issues": breed.get("health_issues"),
                "intelligence": breed.get("intelligence"),
                "shedding_level": breed.get("shedding_level"),
                "social_needs": breed.get("social_needs"),
                "stranger_friendly": breed.get("stranger_friendly"),
                "vocalisation": breed.get("vocalisation"),
                "experimental": breed.get("experimental"),
                "hairless": breed.get("hairless"),
                "natural": breed.get("natural"),
                "rare": breed.get("rare"),
                "rex": breed.get("rex"),
                "bidability": breed.get("bidability"),
                "suppressed_tail": breed.get("suppressed_tail"),
                "short_legs": breed.get("short_legs"),
                "wikipedia_url": breed.get("wikipedia_url"),
                "hypoallergenic": breed.get("hypoallergenic"),
                "reference_image_id": breed.get("reference_image_id"),
                "weight.imperial": breed.get("weight", {}).get("imperial"),
                "weight.metric": breed.get("weight", {}).get("metric"),
                "image_id": item.get("id"),
                "image_url": item.get("url")
            })

    api_df1 = pd.DataFrame(data)

    preferred_order = [
        "id", "name", "origin", "description", "alt_names", "temperament",
        "weight.metric", "weight.imperial", "intelligence", "child_friendly", "dog_friendly",
        "cat_friendly", "stranger_friendly", "energy_level","affection_level", "adaptability",
        "indoor", "grooming", "hypoallergenic", "shedding_level", "life_span", "health_issues",
        "social_needs", "vocalisation", "lap", "natural", "experimental", "rare", "hairless",
        "short_legs", "suppressed_tail", "bidability", "rex", "vcahospitals_url", "vetstreet_url",
        "cfa_url", "wikipedia_url", "image_url", "image_id", "reference_image_id",
        "country_code", "country_codes"
    ]

    for column in preferred_order:
        if column not in api_df1.columns:
            api_df1[column] = np.nan

    api_df2 = api_df1[preferred_order]

    api_df2.to_csv(save_path, index=False)
    
    print(f"Your easy-to-read .csv file has been exported to: {save_path}")

    return api_df2
