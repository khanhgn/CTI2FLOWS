# Transforming CTI into Mitre ATT&CK Flows

## Overview

This initiative introduces a comprehensive framework to convert Cyber Threat Intelligence (CTI) data into flows compatible with the Mitre ATT&CK framework. The conversion process spans multiple steps, and the ensuing guide facilitates seamless setup and execution within this framework.

## Prerequisites

- Access to a [Google Colab](https://colab.research.google.com/) account for running the associated notebooks.

## Getting Approval for Llama 2

Before initiating the notebook, ensure you have a Pinecone account and the necessary approval for using the Llama 2 model.

### Step 1: Fill in the Llama 2 Access Request Form

1. Complete the Llama access request form, specifying the need for both the Llama 2 and Llama Chat models. Use the email associated with your HuggingFace account.
2. Typically, approval emails are received within an hour.

### Step 2: Request Access to the Llama 2 Model

1. Visit the [Llama 2 13B Chat model page](llama-2-model-page-link).
2. Submit the request form for downloading the model.
3. Approval is generally received within an hour.

## Configuring RAG with Llama 2

After securing approval, follow these steps to set up the notebook for Retrieval-Augmented Generation (RAG) with Llama 2. Replace three key strings as indicated throughout the notebook:

- **PINECONE_API_KEY:** Obtain from your Pinecone account.
- **PINECONE_ENV:** Extract from Pinecone under the Environment header.
- **HF_AUTH_TOKEN:** Generate or use an existing token from the [Access token page](hugging-face-access-token).

### Pinecone API Key

1. Create a Pinecone account if you don't have one.
2. Sign in and navigate to API Keys on the right panel.
3. Copy the PINECONE_API_KEY using the designated button.

![Copying the Pinecone API key](pinecone-api-key-image)

### Pinecone Environment

1. Copy the Pinecone environment (PINECONE_ENV) under the Environment header.

![Copying the Pinecone environment parameter](pinecone-environment-image)

### Hugging Face Authorization Token

1. Generate a new token or use an existing one from the [Access token page](hugging-face-access-token).

## Executing the Conversion Process

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

Follow these outlined steps to successfully convert CTI data into Mitre ATT&CK Flow representations. Ensure you save the outputs at each step for future reference and analysis.

## Issues and Support

For any concerns or inquiries, kindly open an [issue](link-to-issues) in this repository.

## License

This project operates under the [MIT License](link-to-license).
