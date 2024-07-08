import pandas as pd
import re

def extract_data_from_xml(xml_file, excel_file, column_name='Description', sheet_name='Sheet1'):
    # Read data from XML file
    with open(xml_file, 'r', encoding='utf-8') as file:
        data = file.read()
    
    # Use regex to find all occurrences of the pattern z_description="..."/>
    pattern = r'z_description="(.*?)"/>'
    matches = re.findall(pattern, data)
    
    # Create a DataFrame
    df = pd.DataFrame(matches, columns=[column_name])
    
    # Write DataFrame to Excel file
    df.to_excel(excel_file, index=False, sheet_name=sheet_name)
    
    print(f"Data from {xml_file} has been written to {excel_file} in column '{column_name}'.")

# Usage example
xml_file = r'C:\Packages\Diagnostics_Java_Package_Merge_New\01_PlanSpec\DIAG\CAPL\F02_Standard_DiagnosticsPackage.xml'
excel_file = r'C:\Packages\Diagnostics_Java_Package_Merge_New\01_PlanSpec\DIAG\CAPL\F02_Gap.xlsx'

extract_data_from_xml(xml_file, excel_file)
