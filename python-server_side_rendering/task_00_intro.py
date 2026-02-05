import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees should be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Placeholders to replace
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            processed_template = processed_template.replace(f"{{{key}}}", str(value))
        
        # Generate output files
        filename = f"output_{i}.txt"
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists. Overwriting.")
            
        with open(filename, 'w') as f:
            f.write(processed_template)
