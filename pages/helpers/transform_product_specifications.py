import pandas as pd


def transform_product_specifications(product_specifications):
    provider_cats = ["Telstra", "Optus", "Vodafone"]
    plan_type_cats = ["Month to Month", "Pre-Paid Cap", "Pre-Paid Bulk Buy"]
    coverage_cats = [
        "Full Coverage",
        "Broad Coverage",
        "Partial Coverage",
    ]  # Even if Broad isn't used

    product_specifications["Provider"] = pd.Categorical(
        product_specifications["Provider"], categories=provider_cats
    )
    product_specifications["Plan Type"] = pd.Categorical(
        product_specifications["Plan Type"], categories=plan_type_cats
    )
    product_specifications["Network Coverage"] = pd.Categorical(
        product_specifications["Network Coverage"], categories=coverage_cats
    )

    # Use get_dummies
    scenario_reflected_data = pd.get_dummies(
        product_specifications, columns=["Provider", "Plan Type", "Network Coverage"]
    )

    # Rename to match spec if needed (optional)
    scenario_reflected_data = scenario_reflected_data.rename(
        columns={
            "On/Off": "On/Off",
            "Product": "Product",
            "Provider_Telstra": "Telstra",
            "Provider_Optus": "Optus",
            "Provider_Vodafone": "Vodafone",
            "Plan Type_Month to Month": "Month to Month",
            "Plan Type_Pre-Paid Cap": "Pre-Paid Cap",
            "Plan Type_Pre-Paid Bulk Buy": "Pre-Paid Bulk Buy",
            "Network Coverage_Full Coverage": "Full Coverage",
            "Network Coverage_Broad Coverage": "Broad Coverage",
            "Network Coverage_Partial Coverage": "Partial Coverage",
            "Minimum Monthly Spend": "Minimum Monthly Spend",
        }
    )

    # # Final column order
    final_columns = [
        "On/Off",
        "Product",
        "Telstra",
        "Optus",
        "Vodafone",
        "Month to Month",
        "Pre-Paid Cap",
        "Pre-Paid Bulk Buy",
        "Full Coverage",
        "Broad Coverage",
        "Partial Coverage",
        "Minimum Monthly Spend",
    ]

    scenario_reflected_data_final = scenario_reflected_data[final_columns]
    return scenario_reflected_data_final
