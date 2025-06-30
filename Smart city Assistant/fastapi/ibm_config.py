from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

creds = Credentials(
    api_key="Your_ibm key Make sure your project as watsonx Machine Learning Associated services",
    url="https://us-south.ml.cloud.ibm.com"
)

model = ModelInference(
    model_id="ibm/granite-3-2b-instruct",
    credentials=creds,
    project_id="Your project_Id"
)

params = {
    "decoding_method": "greedy",
    "max_new_tokens": 1024
}
