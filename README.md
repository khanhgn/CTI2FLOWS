# Convert CTI to Mitre ATT&CK Flow

## Introduction

This project provides a framework for converting Cyber Threat Intelligence (CTI) data into Mitre ATT&CK framework-compatible flows. The process involves several steps, and the following instructions guide you through the framework setup and execution.

## Prerequisites

- [Google Colab](https://colab.research.google.com/) account for running the notebooks.

## Getting Started

### Step 1: Summarize and Run TRAM

1. Open the notebook [Tram2flow_fin.ipynb](link-to-your-nb).
2. Execute the code within the notebook.
3. Follow the prompts and instructions to summarize and run TRAM.
4. Save the output for further analysis.

### Step 2: Run LLM Analysis

1. Open the notebook [operator.ipynb](link-to-your-nb).
2. Execute the code within the notebook.
3. Follow the prompts and instructions to perform LLM analysis.
4. Save the generated results for subsequent steps.

### Step 3: Run Convert DataFrame to STIX

1. Open the notebook [LLM_output_to_Image.ipynb](link-to-your-nb).
2. Execute the code within the notebook.
3. Follow the prompts and instructions to convert DataFrame to STIX format.
4. Save the generated STIX file.

### Step 4: Run Convert STIX to PNG

1. Open the notebook [Json_to_PNG.ipynb](link-to-your-nb).
2. Execute the code within the notebook.
3. Follow the prompts and instructions to convert STIX to PNG images.
4. Save the generated PNG files representing Mitre ATT&CK Flows.

## Conclusion

By following these steps, you will successfully convert CTI data into Mitre ATT&CK Flow representations. Ensure that you save the outputs at each step for reference and analysis.

## Issues and Support

For any issues or inquiries, please open an [issue](link-to-issues) in this repository.

## License

This project is licensed under the [MIT License](link-to-license).
