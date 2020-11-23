import json
import csv


def to_csv(input_file, output_file):
    print("Opening file")
    f = open(input_file)
    properties = json.load(f)
    f.close()

    print("Cleaning up data")
    toRemove = []
    requiredVals = ["building_size", "beds",
                    "baths_full", "baths_half", "price"]
    for property in properties:
        # Check to make sure all required fields are here
        removeThis = False
        for val in requiredVals:
            if not val in property:
                toRemove.append(property)
                removeThis = True
                break

        if removeThis:
            continue

        # Remove unecessary data
        property["building_size"] = property["building_size"]["size"]
        property.pop("year_built", None)
        property.pop("property_id", None)
        property.pop("listing_id", None)
        property.pop("prop_type", None)
        property.pop("list_date", None)
        property.pop("last_update", None)
        property.pop("prop_status", None)
        property.pop("address", None)
        property.pop("mls", None)
        property.pop("client_display_flags", None)
        property.pop("sold_history", None)
        property.pop("office", None)
        property.pop("agents", None)
        property.pop("rdc_web_url", None)
        property.pop("rdc_app_url", None)
        property.pop("data_source_name", None)
        property.pop("page_no", None)
        property.pop("rank", None)
        property.pop("list_tracking", None)
        property.pop("is_new_construction", None)
        property.pop("photo_count", None)
        property.pop("photos", None)
        property.pop("lot_size", None)
        property.pop("price_reduced_date", None)
        property.pop("garage", None)
        property.pop("baths", None)
        if property["baths_half"] == None:
            property["baths_half"] = 0

    for property in toRemove:
        properties.remove(property)

    print("Writing to output file")
    f = open(output_file, "w")
    writer = csv.writer(f)

    count = 0

    for property in properties:
        if count == 0:
            # Writing headers of CSV file
            header = property.keys()
            writer.writerow(header)
            count += 1

        # Writing data of CSV file
        writer.writerow(property.values())
