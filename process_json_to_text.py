import json

def create_tool_record(tool_info, section_name):
    """Formats a single tool's information into a string."""
    
    name = tool_info.get('name', 'N/A')
    description = tool_info.get('description', 'N/A')
    if description is None or description == "":
        description = "No description available."
        
    is_compatible = tool_info.get('is_workflow_compatible', False)

    return (
        f"NAME: {name}\n"
        f"DESCRIPTION: {description}\n"
        f"IS_WORKFLOW_COMPATIBLE: {is_compatible}\n"
        f"PANEL_SECTION_NAME: {section_name}\n\n"
    )

def process_tools_summary(input_path='data/tools_summary.json', output_path='data/tools.txt'):
    """
    Reads a JSON file with tool information, processes it, and writes
    the formatted data to a text file.
    """
    try:
        with open(input_path, 'r') as f_in:
            data = json.load(f_in)
    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_path}'")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{input_path}'")
        return

    with open(output_path, 'w') as f_out:
        for section in data:
            section_name = section.get('name', 'Unnamed Section')
            if 'elems' in section and isinstance(section['elems'], list):
                for tool in section['elems']:
                    # Ensure the tool is a dictionary before processing
                    if isinstance(tool, dict):
                        record = create_tool_record(tool, section_name)
                        f_out.write(record)

if __name__ == '__main__':
    process_tools_summary()
    print("Processing complete. Output written to tools.txt")
